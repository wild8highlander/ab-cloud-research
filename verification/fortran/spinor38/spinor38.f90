! spinor38.f90 — Test 38: 64 spinor structures of the Klein quartic (Fortran port)
! Self-implemented cyclic Jacobi eigenvalue algorithm (no LAPACK).
! Build: gfortran -O2 -o spinor38 spinor38.f90
! Run:   ./spinor38 [repo-root]
program spinor38
  implicit none
  integer, parameter :: N = 56, MAXC = 64, MAXE = 84
  character(len=4096) :: dd, line, root
  character(len=64) :: fname
  integer :: ios, i, k, u, v, nclasses, nodd, nzero, nzero_ref, repcls, nsp, nr
  integer :: cls_idx(MAXC), orbit(MAXC), arf(MAXC)
  double precision :: signs(MAXC, MAXE), A(N,N), eig(N), spectra(N, 40)
  double precision :: rep(N), lam(N), dsp(N), rsum, rmean, isomax, d1, d2
  double precision :: r_ref
  integer :: eu(MAXE), ev(MAXE), nedges
  logical :: ok, rok, iok

  ! ---- data dir ----
  dd = '.'
  if (command_argument_count() .ge. 1) then
    call get_command_argument(1, root)
    dd = trim(root)
  end if
  do i = 1, 6
    fname = trim(dd) // '/verification/spinor64/data/spinor_classes.csv'
    open(unit=10, file=fname, status='old', iostat=ios, action='read')
    if (ios == 0) exit
    dd = trim(dd) // '/..'
    if (i == 6) then
      write(*,*) 'data dir not found; pass repo root as argument'
      stop 2
    end if
  end do
  close(10)

  ! ---- classes ----
  fname = trim(dd) // '/verification/spinor64/data/spinor_classes.csv'
  open(unit=10, file=fname, status='old', action='read')
  read(10, '(A)') line
  nclasses = 0
  do
    read(10, '(A)', iostat=ios) line
    if (ios /= 0) exit
    if (len_trim(line) == 0) cycle
    nclasses = nclasses + 1
    call parse_class_line(line, cls_idx(nclasses), orbit(nclasses), &
         arf(nclasses), signs(nclasses, :))
  end do
  close(10)

  ! ---- edges ----
  fname = trim(dd) // '/verification/spinor64/data/klein_graph_edges.csv'
  open(unit=10, file=fname, status='old', action='read')
  read(10, '(A)') line
  nedges = 0
  do
    read(10, '(A)', iostat=ios) line
    if (ios /= 0) exit
    if (len_trim(line) == 0) cycle
    nedges = nedges + 1
    call parse_edge_line(line, eu(nedges), ev(nedges))
  end do
  close(10)

  ! ---- reference stats ----
  fname = trim(dd) // '/verification/spinor64/data/reference_stats.json'
  open(unit=10, file=fname, status='old', action='read')
  r_ref = 0; nzero_ref = 0; repcls = 0
  do
    read(10, '(A)', iostat=ios) line
    if (ios /= 0) exit
    if (index(line, '"r_mean_reference"') > 0) &
      r_ref = json_number(line)
    if (index(line, '"n_zero_modes"') > 0) &
      nzero_ref = nint(json_number(line))
    if (index(line, '"representative_class"') > 0) &
      repcls = nint(json_number(line))
  end do
  close(10)

  nodd = 0
  do i = 1, nclasses
    if (orbit(i) == 0) nodd = nodd + 1
  end do

  ! ---- spectra of all odd-orbit classes ----
  k = 0
  rep = 0
  do i = 1, nclasses
    if (orbit(i) /= 0) cycle
    A = 0
    do nsp = 1, nedges
      u = eu(nsp) + 1; v = ev(nsp) + 1
      A(u, v) = signs(i, nsp)
      A(v, u) = signs(i, nsp)
    end do
    call jacobi_eigen(A, eig)
    k = k + 1
    spectra(:, k) = eig
    if (cls_idx(i) == repcls) rep = eig
  end do

  ! ---- isospectrality ----
  isomax = 0
  do i = 1, k
    do nsp = i + 1, k
      do u = 1, N
        d1 = abs(spectra(u, i) - spectra(u, nsp))
        if (d1 > isomax) isomax = d1
      end do
    end do
  end do

  ! ---- zero modes and <r> of the representative (fold |lambda|) ----
  nzero = 0
  do i = 1, N
    lam(i) = abs(rep(i))
    if (abs(rep(i)) < 1d-8) nzero = nzero + 1
  end do
  call sort_d(lam, N)
  nsp = 0
  do i = 1, N - 1
    d1 = lam(i + 1) - lam(i)
    if (d1 > 1d-8) then
      nsp = nsp + 1
      dsp(nsp) = d1
    end if
  end do
  rsum = 0
  nr = 0
  do i = 1, nsp - 1
    d1 = dsp(i); d2 = dsp(i + 1)
    if (d1 > d2) then
      rsum = rsum + d2 / d1
    else
      rsum = rsum + d1 / d2
    end if
    nr = nr + 1
  end do
  rmean = rsum / nr

  iok = isomax < 1d-9
  rok = abs(rmean - r_ref) < 1d-6
  ok = iok .and. rok .and. (nzero == nzero_ref)

  write(*,'(A)') 'Test 38 - 64 spinor structures of the Klein quartic (Fortran port)'
  write(*,'(A,I0,A,I0,A)') 'classes loaded: ', nclasses, ' | odd-orbit members: ', nodd, ''
  write(*,'(A,ES10.3,A,A)') 'isospectrality within the odd orbit: max|dlambda| = ', &
       isomax, ' -> ', merge('PASS', 'FAIL', iok)
  write(*,'(A,I0,A,I0,A)') 'zero modes (representative): ', nzero, &
       ' (expected ', nzero_ref, ')'
  write(*,'(A,F10.10,A,A)') '<r> (representative): ', rmean, &
       ' (reference 0.4515710793) -> ', merge('PASS', 'FAIL', rok)
  write(*,'(A,A)') 'VERDICT: ', merge('PASS', 'FAIL', ok)
  if (.not. ok) stop 1

contains

  subroutine parse_class_line(ln, ci, ob, af, sg)
    character(len=*), intent(in) :: ln
    integer, intent(out) :: ci, ob, af
    double precision, intent(out) :: sg(:)
    integer :: p1, p2, p3, j, ios2, tlen
    character(len=:), allocatable :: tail
    p1 = index(ln, ',')
    p2 = index(ln(p1+1:), ',') + p1
    p3 = index(ln(p2+1:), ',') + p2
    read(ln(1:p1-1), *) ci
    read(ln(p1+1:p2-1), *) ob
    read(ln(p2+1:p3-1), *) af
    tail = trim(adjustl(ln(p3+1:)))
    j = 0
    p1 = 1
    tlen = len_trim(tail)
    do while (p1 <= tlen)
      p2 = p1
      do while (p2 <= tlen .and. tail(p2:p2) /= ' ')
        p2 = p2 + 1
      end do
      j = j + 1
      read(tail(p1:p2-1), *, iostat=ios2) sg(j)
      p1 = p2 + 1
    end do
  end subroutine

  subroutine parse_edge_line(ln, e1, e2)
    character(len=*), intent(in) :: ln
    integer, intent(out) :: e1, e2
    integer :: p1, p2
    p1 = index(ln, ',')
    p2 = index(ln(p1+1:), ',') + p1
    read(ln(p1+1:p2-1), *) e1
    read(ln(p2+1:), *) e2
  end subroutine

  double precision function json_number(ln)
    character(len=*), intent(in) :: ln
    integer :: p, q
    p = index(ln, ':')
    q = index(ln(p+1:), ',')
    if (q == 0) q = len_trim(ln(p+1:)) + 1
    read(ln(p+1:p+q-1), *) json_number
  end function

  subroutine sort_d(arr, n2)
    integer, intent(in) :: n2
    double precision, intent(inout) :: arr(n2)
    integer :: a2, b2
    double precision :: tmp
    do a2 = 2, n2
      tmp = arr(a2)
      b2 = a2 - 1
      do while (b2 >= 1 .and. arr(b2) > tmp)
        arr(b2 + 1) = arr(b2)
        b2 = b2 - 1
      end do
      arr(b2 + 1) = tmp
    end do
  end subroutine

  subroutine jacobi_eigen(Ain, w)
    double precision, intent(inout) :: Ain(N, N)
    double precision, intent(out) :: w(N)
    integer :: sweep, p2, q2, kk
    double precision :: off, tau, t2, c2, s2, akp, akq, apk, aqk
    do sweep = 1, 200
      off = 0
      do p2 = 1, N
        do q2 = p2 + 1, N
          off = off + Ain(p2, q2) ** 2
        end do
      end do
      if (off < 1d-24) exit
      do p2 = 1, N
        do q2 = p2 + 1, N
          if (abs(Ain(p2, q2)) < 1d-15) cycle
          tau = (Ain(q2, q2) - Ain(p2, p2)) / (2 * Ain(p2, q2))
          t2 = sign(1d0, tau) / (abs(tau) + sqrt(1d0 + tau * tau))
          c2 = 1d0 / sqrt(1d0 + t2 * t2)
          s2 = t2 * c2
          do kk = 1, N
            akp = Ain(kk, p2); akq = Ain(kk, q2)
            Ain(kk, p2) = c2 * akp - s2 * akq
            Ain(kk, q2) = s2 * akp + c2 * akq
          end do
          do kk = 1, N
            apk = Ain(p2, kk); aqk = Ain(q2, kk)
            Ain(p2, kk) = c2 * apk - s2 * aqk
            Ain(q2, kk) = s2 * apk + c2 * aqk
          end do
        end do
      end do
    end do
    do kk = 1, N
      w(kk) = Ain(kk, kk)
    end do
    call sort_d(w, N)
  end subroutine

end program spinor38
