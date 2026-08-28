!===============================================================================
! AB-CLOUD VERIFICATION SUITE — ENGLISH
! Fortran 2018 | Modern, Implicit None, Well-Documented
!===============================================================================
! Three objections against the Riemann Hypothesis:
!   Objection 1: b(N) → 0?  (Gram point deviation convergence)
!   Objection 2: GUE spacing KS test (level spacing distribution)
!   Objection 3: Large-T decay slope ≈ -0.5
!===============================================================================
program ab_cloud_verify_en
  use, intrinsic :: iso_fortran_env, only: dp => real64, int64
  implicit none

  real(dp), parameter :: PI      = 3.14159265358979323846264338327950288_dp
  real(dp), parameter :: TWO_PI  = 6.28318530717958647692528676655900577_dp

  real(dp), allocatable :: gammas(:)
  integer(int64)        :: n_loaded
  integer               :: n_zeros, objection_id, lang_id
  character(len=64)     :: source_name
  real(dp)              :: b_n, ks_stat, ks_pval, decay_slope
  logical               :: pass_obj1, pass_obj2, pass_obj3
  real(dp)              :: t_start, t_end

  call cpu_time(t_start)

  n_zeros      = 10000
  source_name  = "auto"
  objection_id = 0
  lang_id      = 1

  call parse_args(n_zeros, source_name, objection_id)

  write(*,'(A)') ""
  write(*,'(A)') "  +=================================================+"
  write(*,'(A)') "  |  AB-CLOUD VERIFICATION — RIEMANN HYPOTHESIS     |"
  write(*,'(A)') "  |  Three objections: b(N), GUE KS, Large-T        |"
  write(*,'(A)') "  +=================================================+"
  write(*,'(A)') ""

  call load_zeros(gammas, n_loaded, n_zeros, source_name)
  write(*,'(A,I0,A)') "  Zeros loaded: ", n_loaded, " (gamma ordinates)"

  if (objection_id == 0 .or. objection_id == 1) &
    call compute_objection1(gammas, n_loaded, b_n, pass_obj1)
  if (objection_id == 0 .or. objection_id == 2) &
    call compute_objection2(gammas, n_loaded, ks_stat, ks_pval, pass_obj2)
  if (objection_id == 0 .or. objection_id == 3) &
    call compute_objection3(gammas, n_loaded, decay_slope, pass_obj3)

  call print_summary(objection_id, b_n, pass_obj1, ks_stat, ks_pval, pass_obj2, &
                     decay_slope, pass_obj3)

  call cpu_time(t_end)
  write(*,'(A,F8.3,A)') "  Total time: ", t_end - t_start, " s"

  deallocate(gammas)

contains

  subroutine parse_args(n_zeros, source_name, objection_id)
    integer, intent(inout)          :: n_zeros, objection_id
    character(len=64), intent(inout):: source_name
    integer          :: i, nargs
    character(len=256):: arg
    nargs = command_argument_count()
    i = 1
    do while (i <= nargs)
      call get_command_argument(i, arg)
      select case (trim(arg))
        case ('--zeros');   i = i + 1; call get_command_argument(i, arg); read(arg, *) n_zeros
        case ('--source');  i = i + 1; call get_command_argument(i, arg); source_name = trim(arg)
        case ('--objection')
          i = i + 1; call get_command_argument(i, arg)
          if (trim(arg) == 'all') then; objection_id = 0; else; read(arg, *) objection_id; end if
        case default; continue
      end select
      i = i + 1
    end do
  end subroutine parse_args

  subroutine load_zeros(gammas, n_loaded, n_request, source_name)
    real(dp), allocatable, intent(out) :: gammas(:)
    integer(int64), intent(out)        :: n_loaded
    integer, intent(in)                :: n_request
    character(len=64), intent(in)      :: source_name
    character(len=512) :: filepath, line
    real(dp)           :: val
    integer            :: u, ios, cnt, max_alloc

    if (trim(source_name) /= "auto") then
      filepath = "../data/" // trim(source_name)
    else if (n_request <= 13661) then
      filepath = "../data/zeta_zeros_50000.txt"
    else if (n_request <= 500000) then
      filepath = "../data/zeta_zeros_500k_odlyzko.txt"
    else if (n_request <= 2000000) then
      filepath = "../data/zeta_zeros_2M_odlyzko.txt"
    else
      filepath = "../data/zeros6.txt"
    end if
    write(*,'(A,A)') "  Data file: ", trim(filepath)

    open(newunit=u, file=trim(filepath), status='old', action='read', iostat=ios)
    if (ios /= 0) then; write(*,'(A,A)') "  ERROR: Cannot open ", trim(filepath); stop 1; end if

    cnt = 0
    do
      read(u, '(A)', iostat=ios) line
      if (ios /= 0) exit
      line = adjustl(line)
      if (len_trim(line) == 0) cycle
      if (line(1:1) == '#') cycle
      read(line, *, iostat=ios) val
      if (ios == 0 .and. val > 0.0_dp) cnt = cnt + 1
    end do
    rewind(u)

    max_alloc = min(cnt, n_request)
    allocate(gammas(max_alloc))
    n_loaded = 0
    do
      read(u, '(A)', iostat=ios) line
      if (ios /= 0) exit
      line = adjustl(line)
      if (len_trim(line) == 0) cycle
      if (line(1:1) == '#') cycle
      read(line, *, iostat=ios) val
      if (ios == 0 .and. val > 0.0_dp) then
        n_loaded = n_loaded + 1
        if (n_loaded <= int(max_alloc, int64)) then
          gammas(int(n_loaded)) = val
        else
          exit
        end if
      end if
    end do
    close(u)
    n_loaded = min(n_loaded, int(max_alloc, int64))
  end subroutine load_zeros

  function lambert_w0(x) result(w)
    real(dp), intent(in) :: x
    real(dp)             :: w
    integer              :: iter
    if (x == 0.0_dp) then; w = 0.0_dp; return; end if
    w = log(max(x, 1.0e-30_dp))
    if (w > 0.0_dp) w = log(w)
    do iter = 1, 50
      block
        real(dp) :: ew, f, fp, fpp, delta
        ew  = exp(w); f = w * ew - x; fp = ew * (w + 1.0_dp); fpp = ew * (w + 2.0_dp)
        delta = f / (fp - 0.5_dp * f * fpp / fp)
        w = w - delta
        if (abs(delta) < 1.0e-15_dp * abs(w)) exit
      end block
    end do
  end function lambert_w0

  function gram_point(n) result(gn)
    integer(int64), intent(in) :: n
    real(dp) :: gn
    gn = TWO_PI * lambert_w0(real(n, dp) / exp(1.0_dp))
  end function gram_point

  subroutine compute_objection1(gammas, n, b_n, pass)
    real(dp), intent(in) :: gammas(:)
    integer(int64), intent(in) :: n
    real(dp), intent(out) :: b_n
    logical, intent(out) :: pass
    real(dp)    :: s
    integer(int64) :: k
    s = 0.0_dp
    do k = 1, n; s = s + abs(gammas(int(k)) - gram_point(k)); end do
    b_n = s / real(n, dp)
    pass = (b_n < 1.0_dp)
    write(*,'(/,A)')  "====================================================="
    write(*,'(A)')    "  OBJECTION 1: b(N) Convergence"
    write(*,'(A)')    "  b(N) = (1/N) * Sum|gamma_k - gamma~_k|, Gram pts via Lambert W"
    write(*,'(A)')    "====================================================="
    write(*,'(A,I0)')     "    N       = ", n
    write(*,'(A,ES15.8)') "    b(N)    = ", b_n
    write(*,'(A,L1)')     "    Pass:   ", pass
  end subroutine compute_objection1

  subroutine compute_objection2(gammas, n, ks_stat, ks_pval, pass)
    real(dp), intent(in) :: gammas(:)
    integer(int64), intent(in) :: n
    real(dp), intent(out) :: ks_stat, ks_pval
    logical, intent(out) :: pass
    real(dp), allocatable :: s(:), sorted_s(:)
    real(dp)    :: log_factor, cdf_theo, cdf_emp, d_plus
    integer(int64) :: k, m
    m = n - 1
    allocate(s(int(m)))
    do k = 1, m
      log_factor = log(gammas(int(k)) / TWO_PI)
      s(int(k)) = (gammas(int(k+1)) - gammas(int(k))) * log_factor / TWO_PI
    end do
    allocate(sorted_s(int(m))); sorted_s = s; call sort_array(sorted_s)
    ks_stat = 0.0_dp
    do k = 1, m
      cdf_emp = real(k, dp) / real(m, dp)
      cdf_theo = gue_cdf(sorted_s(int(k)))
      d_plus = abs(cdf_emp - cdf_theo)
      if (d_plus > ks_stat) ks_stat = d_plus
    end do
    ks_pval = kolmogorov_pvalue(ks_stat, real(m, dp))
    pass = (ks_pval > 0.05_dp)
    write(*,'(/,A)')  "====================================================="
    write(*,'(A)')    "  OBJECTION 2: GUE Spacing KS Test"
    write(*,'(A)')    "  s_k = dg_k * log(g_k/2pi) / 2pi,  p(s) = (pi*s/2)*exp(-pi*s^2/4)"
    write(*,'(A)')    "====================================================="
    write(*,'(A,I0)')     "    Spacing count    = ", m
    write(*,'(A,ES15.8)') "    KS statistic     = ", ks_stat
    write(*,'(A,ES15.8)') "    p-value          = ", ks_pval
    write(*,'(A,L1)')     "    Pass (p>0.05):   ", pass
    deallocate(s, sorted_s)
  end subroutine compute_objection2

  function gue_cdf(s) result(cdf)
    real(dp), intent(in) :: s, cdf
    integer :: i, nsteps; real(dp) :: h, x, sum_val
    if (s <= 0.0_dp) then; cdf = 0.0_dp; return; end if
    nsteps = 200; h = s / real(nsteps, dp); sum_val = 0.0_dp
    do i = 0, nsteps
      x = real(i, dp) * h
      if (i == 0 .or. i == nsteps) then; sum_val = sum_val + gue_pdf(x)
      else if (mod(i,2) == 1) then; sum_val = sum_val + 4.0_dp * gue_pdf(x)
      else; sum_val = sum_val + 2.0_dp * gue_pdf(x); end if
    end do
    cdf = min((h / 3.0_dp) * sum_val, 1.0_dp)
  end function gue_cdf

  function gue_pdf(s) result(pdf)
    real(dp), intent(in) :: s, pdf
    pdf = (PI * s / 2.0_dp) * exp(-PI * s**2 / 4.0_dp)
  end function gue_pdf

  function kolmogorov_pvalue(d, n) result(pval)
    real(dp), intent(in) :: d, n; real(dp) :: pval, z, term; integer :: k
    z = d * sqrt(n); pval = 0.0_dp
    do k = -10, 10; term = exp(-2.0_dp * (real(2*k, dp)*z + z)**2); pval = pval + ((-1)**k) * term; end do
    pval = max(0.0_dp, min(1.0_dp, pval))
  end function kolmogorov_pvalue

  subroutine compute_objection3(gammas, n, slope, pass)
    real(dp), intent(in) :: gammas(:)
    integer(int64), intent(in) :: n
    real(dp), intent(out) :: slope; logical, intent(out) :: pass
    real(dp) :: x_mean, y_mean, sxx, sxy, x_val, y_val
    integer(int64) :: k, m; integer :: i_start
    i_start = int(n / 2_int64) + 1; m = n - int(i_start, int64)
    if (m < 10) then; slope = 0.0_dp; pass = .false.; return; end if
    x_mean = 0.0_dp; y_mean = 0.0_dp
    do k = i_start, n - 1
      x_val = log(gammas(int(k))); y_val = log(abs(gammas(int(k+1)) - gammas(int(k))))
      x_mean = x_mean + x_val; y_mean = y_mean + y_val
    end do
    x_mean = x_mean / real(m, dp); y_mean = y_mean / real(m, dp)
    sxx = 0.0_dp; sxy = 0.0_dp
    do k = i_start, n - 1
      x_val = log(gammas(int(k))); y_val = log(abs(gammas(int(k+1)) - gammas(int(k))))
      sxx = sxx + (x_val - x_mean)**2; sxy = sxy + (x_val - x_mean) * (y_val - y_mean)
    end do
    slope = sxy / sxx; pass = (abs(slope + 0.5_dp) < 0.15_dp)
    write(*,'(/,A)')  "====================================================="
    write(*,'(A)')    "  OBJECTION 3: Large-T Decay Slope"
    write(*,'(A)')    "  log|dg_k| ~ slope * log(g_k),  expected slope = -0.5"
    write(*,'(A)')    "====================================================="
    write(*,'(A,I0)')    "    Regression pts  = ", m
    write(*,'(A,F8.4)')  "    Slope           = ", slope
    write(*,'(A,F8.4)')  "    Deviation       = ", abs(slope + 0.5_dp)
    write(*,'(A,L1)')    "    Pass:           ", pass
  end subroutine compute_objection3

  subroutine sort_array(arr)
    real(dp), intent(inout) :: arr(:); real(dp) :: temp; integer :: i, j, n
    n = size(arr)
    do i = 2, n; temp = arr(i); j = i - 1
      do while (j >= 1 .and. arr(j) > temp); arr(j+1) = arr(j); j = j - 1; end do
      arr(j+1) = temp
    end do
  end subroutine sort_array

  subroutine print_summary(obj_id, b_n, p1, ks, ks_p, p2, slope, p3)
    integer, intent(in)  :: obj_id
    real(dp), intent(in) :: b_n, ks, ks_p, slope
    logical, intent(in)  :: p1, p2, p3
    character(len=6) :: s1, s2, s3
    s1 = "  -  "; if (p1) s1 = " PASS"
    s2 = "  -  "; if (p2) s2 = " PASS"
    s3 = "  -  "; if (p3) s3 = " PASS"
    if (.not. p1 .and. obj_id /= 2 .and. obj_id /= 3) s1 = " FAIL"
    if (.not. p2 .and. obj_id /= 1 .and. obj_id /= 3) s2 = " FAIL"
    if (.not. p3 .and. obj_id /= 1 .and. obj_id /= 2) s3 = " FAIL"
    write(*,'(/,A)')  "  +----------+--------------------+--------+"
    write(*,'(A)')    "  | Obj.     |    Value           | Status |"
    write(*,'(A)')    "  +----------+--------------------+--------+"
    write(*,'(A,ES12.5,A,A,A)') "  | 1:b(N)   | ", b_n, "       |", s1, " |"
    write(*,'(A,ES12.5,A,A,A)') "  | 2:KS     | ", ks, "       |", s2, " |"
    write(*,'(A,F8.4,4X,A,A,A)') "  | 3:slope  | ", slope, "       |", s3, " |"
    write(*,'(A)')    "  +----------+--------------------+--------+"
  end subroutine print_summary

end program ab_cloud_verify_en
