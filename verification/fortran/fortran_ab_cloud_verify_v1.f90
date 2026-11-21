!===============================================================================
! AB-CLOUD VERIFICATION SUITE — Fortran port (canonical spec v3.0)
!===============================================================================
! Single source of truth for the Fortran language copy.
!
!   ab_cloud_verify.f90    <- this file: the complete kernel + bilingual catalog
!   ab_cloud_verify_en.f90 <- THIN wrapper:  #define FORCE_LANG_EN + #include
!   ab_cloud_verify_ru.f90 <- THIN wrapper:  #define FORCE_LANG_RU + #include
!
! Compile (preprocessor REQUIRED for the wrappers):
!   gfortran -cpp -O2 -o ab_cloud_verify    ab_cloud_verify.f90
!   gfortran -cpp -O2 -o ab_cloud_verify_en ab_cloud_verify_en.f90
!   gfortran -cpp -O2 -o ab_cloud_verify_ru ab_cloud_verify_ru.f90
!
! The main binary selects the language at runtime:  --lang en|ru (default en,
! with auto-detection from the LANG environment variable).  The wrapper
! binaries pin the language at compile time (CANON_SPEC §10, no duplicated
! math — they are the same source text).
!
! Spec implemented (verification/CANON_SPEC.md, v3.0):
!   §1 Lambert W (principal branch, Newton; fp-guard + small-x seed per the
!      canonical Python reference — the naive spec seed hits fp == 0 at x=1/e)
!   §2 gram_point: seed 2*pi*k/W(k/e), then 8 Newton iterations on the 5-term
!      Riemann–Siegel theta expansion          (NOT the old 2*pi*W(n/e) formula)
!   §3 b(N), b(N;offset) with sequential summation order (bit-parity)
!   §4 normalized spacings
!   §5 GUE CDF via 32768-point interpolation table, SMAX = 5
!   §6 KS (two-sided D, lambda-corrected p), CvM, AD (1e-300 / 1-1e-16 clamps),
!      <r> adjacent-gap ratio, mean/var (n-1)
!   §7 objection protocol 1/2/3 with honest, branch-selected verdicts
!   §8 selfcheck with frozen anchors; exit code 1 if any anchor fails
!   §9 CLI: --zeros N --source NAME --objection X --lang L --data-dir D
!
! Fortran 2008 subset; iso_fortran_env real64; no external dependencies.
!===============================================================================

#ifdef FORCE_LANG_EN
# define FORCED_LANG_PINNED 1
#else
# ifdef FORCE_LANG_RU
#  define FORCED_LANG_PINNED 2
# else
#  define FORCED_LANG_PINNED 0
# endif
#endif

program ab_cloud_verify
  use, intrinsic :: iso_fortran_env, only: dp => real64, error_unit
  use, intrinsic :: ieee_arithmetic, only: ieee_value, ieee_quiet_nan
  implicit none

  ! --- Mathematical constants (rounded to the nearest double) ---------------
  real(dp), parameter :: PI      = 3.14159265358979323846264338327950288_dp
  real(dp), parameter :: TWO_PI  = 6.28318530717958647692528676655900577_dp
  real(dp), parameter :: E_E     = 2.71828182845904523536028747135266250_dp
  real(dp), parameter :: SQRT_2PI = 2.50662827463100050241576528481104525_dp

  ! --- GUE table parameters (spec §5) ---------------------------------------
  integer, parameter :: GUE_TN   = 32768
  real(dp), parameter :: GUE_SMAX = 5.0_dp

  ! --- CLI options -----------------------------------------------------------
  character(len=64)  :: source_name
  character(len=512) :: data_dir
  integer            :: n_zeros, objection_id, lang_id
  logical            :: skip_sc          ! --no-selfcheck

  ! --- Loaded data -----------------------------------------------------------
  real(dp), allocatable :: zeros(:)     ! 1-based, sorted ascending
  real(dp), allocatable :: pref(:)      ! prefix sums, 0..n (bit-identical bN)
  integer               :: n_loaded

  ! --- Results ---------------------------------------------------------------
  integer :: npass, nfail
  logical :: run1, run2, run3
  logical :: obj1_converged, obj2_rejected, obj3_consistent

  ! --- Misc ------------------------------------------------------------------
  real(dp) :: nan_dp
  character(len=64) :: envbuf
  logical :: run_sc

  ! --- Self-check row buffer -------------------------------------------------
  ! Lives at program level because Fortran forbids internal procedures inside
  ! internal procedures: check_row (program-level) appends rows while running
  ! inside selfcheck, and selfcheck prints them afterwards.
  integer, parameter :: SC_MAXROWS = 32
  character(len=24)  :: rname(SC_MAXROWS)
  logical            :: rok(SC_MAXROWS)
  real(dp)           :: rgot(SC_MAXROWS), rexp(SC_MAXROWS)
  real(dp)           :: rdel(SC_MAXROWS)
  integer            :: nrows

  ! Language pin (compile-time wrapper) vs runtime selection
  integer, parameter :: FORCED_LANG = FORCED_LANG_PINNED

  nan_dp = ieee_value(1.0_dp, ieee_quiet_nan)

  ! -----------------------------------------------------------------
  ! Defaults (spec §9)
  ! -----------------------------------------------------------------
  n_zeros      = 50000
  source_name  = 'auto'
  objection_id = 0                     ! 0 = all
  lang_id      = 0                     ! 0 = auto-detect
  data_dir     = '../data'
  skip_sc      = .false.
  run_sc       = .true.
  npass        = 0
  nfail        = 0

  call parse_args()
  run_sc = .not. skip_sc

  if (lang_id == 0) then
    ! auto-detect from LANG environment variable (optional per spec §9)
    envbuf = ' '
    call get_environment_variable('LANG', envbuf)
    if (index(envbuf, 'ru') > 0 .or. index(envbuf, 'RU') > 0) then
      lang_id = 2
    else
      lang_id = 1
    end if
  end if
  if (FORCED_LANG > 0) lang_id = FORCED_LANG

  ! -----------------------------------------------------------------
  ! Banner
  ! -----------------------------------------------------------------
  write(*,'(/,A)') repeat('=', 60)
  write(*,'(A)')   trim(msg('banner1'))
  write(*,'(A)')   trim(msg('banner2'))
  write(*,'(A)')   repeat('=', 60)

  ! -----------------------------------------------------------------
  ! Load zeta zeros
  ! -----------------------------------------------------------------
  call load_zeros(zeros, n_loaded, n_zeros, trim(source_name), trim(data_dir))
  if (n_loaded <= 0) stop 1

  ! Prefix sums: pref(N)/N is bit-identical to the direct sequential sum
  allocate(pref(0:n_loaded))
  call build_prefix(zeros, n_loaded, pref)

  ! -----------------------------------------------------------------
  ! Frozen-anchor self-check FIRST (spec §7 summary rule, §8 anchors)
  ! -----------------------------------------------------------------
  if (run_sc) call selfcheck(zeros, n_loaded, pref, npass, nfail)

  ! -----------------------------------------------------------------
  ! Objections
  ! -----------------------------------------------------------------
  run1 = (objection_id == 0 .or. objection_id == 1)
  run2 = (objection_id == 0 .or. objection_id == 2)
  run3 = (objection_id == 0 .or. objection_id == 3)

  obj1_converged = .false.
  obj2_rejected  = .false.
  obj3_consistent = .false.

  if (run1) call verify_objection1(zeros, n_loaded, pref, obj1_converged)
  if (run2) call verify_objection2(zeros, n_loaded, obj2_rejected)
  if (run3) call verify_objection3(zeros, n_loaded, pref, obj3_consistent)

  ! -----------------------------------------------------------------
  ! Summary
  ! -----------------------------------------------------------------
  call print_summary(npass, nfail, run_sc, run1, run2, run3, &
                     obj1_converged, obj2_rejected, obj3_consistent)

  ! Exit code: nonzero if any frozen anchor failed (spec §8)
  if (nfail > 0) stop 1

contains

  !=============================================================================
  ! Bilingual message catalog (EN + RU), keyed lookup.
  !=============================================================================
  function msg(key) result(s)
    character(len=*), intent(in) :: key
    character(len=400)           :: s

    select case (key)
      ! --- banner ----------------------------------------------------------
      case ('banner1')
        if (lang_id == 2) then
          s = "AB-CLOUD ПРОВЕРОЧНЫЙ ПАКЕТ (Fortran) — канон v3.0"
        else
          s = "AB-CLOUD VERIFICATION SUITE (Fortran) — canon v3.0"
        end if
      case ('banner2')
        if (lang_id == 2) then
          s = "Три возражения: b(N), GUE-статистика, убывание при больших T"
        else
          s = "Three objections: b(N), GUE statistics, large-T decay"
        end if

      ! --- loader ----------------------------------------------------------
      case ('load_a')
        if (lang_id == 2) then; s = "Загрузка"; else; s = "Loading"; end if
      case ('load_b')
        if (lang_id == 2) then; s = "нулей из '"; else; s = "zeros from '"; end if
      case ('loaded_a')
        if (lang_id == 2) then; s = "Загружено"; else; s = "Loaded"; end if
      case ('loaded_b')
        if (lang_id == 2) then; s = "нулей из '"; else; s = "zeros from '"; end if
      case ('loaded_c')
        s = "'  |  T in ["
      case ('asel_a')
        if (lang_id == 2) then
          s = "Авто-выбор '"
        else
          s = "Auto-selected '"
        end if
      case ('asel_b')
        if (lang_id == 2) then; s = "' (нужно >="; else; s = "' (needs >="; end if
      case ('asel_c')
        if (lang_id == 2) then
          s = " нулей, файл содержит "
        else
          s = " zeros, file has "
        end if
      case ('err_nosrc')
        if (lang_id == 2) then
          s = "ОШИБКА: Нет источника данных для нулей: "
        else
          s = "ERROR: No data source available for zeros: "
        end if
      case ('err_notfound')
        if (lang_id == 2) then
          s = "ОШИБКА: Файл данных не найден: "
        else
          s = "ERROR: Data file not found: "
        end if
      case ('err_open')
        if (lang_id == 2) then
          s = "ОШИБКА: Не удалось открыть файл данных: "
        else
          s = "ERROR: Cannot open data file: "
        end if
      case ('err_gz')
        if (lang_id == 2) then
          s = "ОШИБКА: распаковка gzip не удалась (gzip -dc): "
        else
          s = "ERROR: gzip decompression failed (gzip -dc): "
        end if

      ! --- selfcheck -------------------------------------------------------
      case ('sc_title')
        if (lang_id == 2) then
          s = "Само-проверка golden — замороженные якоря "// &
              "(канон: meridian-spectral-observatory, selftest 199/199)"
        else
          s = "Golden self-check — frozen anchors (canon: "// &
              "meridian-spectral-observatory, selftest 199/199)"
        end if
      case ('sc_comp')
        if (lang_id == 2) then; s = "вычислено = "; else; s = "computed = "; end if
      case ('sc_exp')
        if (lang_id == 2) then; s = ", ожидание = "; else; s = ", expected = "; end if
      case ('sc_pass')
        if (lang_id == 2) then; s = "ПРОЙДЕНО"; else; s = "PASS"; end if
      case ('sc_fail')
        if (lang_id == 2) then; s = "СБОЙ"; else; s = "FAIL"; end if
      case ('sc_skip')
        if (lang_id == 2) then; s = "ПРОПУСК"; else; s = "SKIP"; end if
      case ('sc_need')
        if (lang_id == 2) then; s = "  (нужно "; else; s = "  (needs "; end if
      case ('sc_have')
        if (lang_id == 2) then; s = " нулей, есть "; else; s = " zeros, have "; end if
      case ('sc_result')
        if (lang_id == 2) then; s = "Само-проверка:"; else; s = "Self-check:"; end if
      case ('sc_passed')
        if (lang_id == 2) then; s = "пройдено,"; else; s = "passed,"; end if
      case ('sc_failed')
        if (lang_id == 2) then; s = "провалено"; else; s = "failed"; end if

      ! --- objection 1 -----------------------------------------------------
      case ('o1_title')
        if (lang_id == 2) then
          s = "Возражение 1: Численная устойчивость b(N)"
        else
          s = "Objection 1: Numerical Stability of b(N)"
        end if
      case ('o1_conv')
        if (lang_id == 2) then
          s = "Таблица сходимости — b(N) = (1/N) Sum|gamma_k - gtilde_k|"
        else
          s = "Convergence table — b(N) = (1/N) Sum|gamma_k - gtilde_k|"
        end if
      case ('o1_fit_a')
        if (lang_id == 2) then
          s = "  Эмпирический закон:  b(N) ~= "
        else
          s = "  Empirical law:  b(N) ~ "
        end if
      case ('o1_fit_b')
        if (lang_id == 2) then; s = " · N^(-"; else; s = " · N^(-"; end if
      case ('o1_fit_c')
        if (lang_id == 2) then; s = ")   (R2 = "; else; s = ")   (R^2 = "; end if
      case ('o1_honest')
        if (lang_id == 2) then
          s = "  b(N) монотонно убывает по таблице — сходимость подтверждена" // &
              " на доступном" // char(10) // &
              "  диапазоне. Убывание ЭМПИРИЧЕСКОЕ, это не O(1/sqrt(N))" // &
              " (см. Возражение 3)."
        else
          s = "  b(N) decreases monotonically over the table — convergence" // &
              " confirmed on" // char(10) // &
              "  the accessible range. The decay is EMPIRICAL, not O(1/sqrt(N))" // &
              " (see Objection 3)."
        end if
      case ('o1_honest_bad')
        if (lang_id == 2) then
          s = "  b(N) НЕ монотонно по таблице — сходимость на этом диапазоне" // &
              " НЕ подтверждена." // char(10) // &
              "  Убывание ЭМПИРИЧЕСКОЕ, это не O(1/sqrt(N)) (см. Возражение 3)."
        else
          s = "  b(N) is NOT monotone across the table — convergence is NOT" // &
              " demonstrated" // char(10) // &
              "  on this range. The decay is EMPIRICAL, not O(1/sqrt(N))" // &
              " (see Objection 3)."
        end if

      ! --- objection 2 -----------------------------------------------------
      case ('o2_title')
        if (lang_id == 2) then
          s = "Возражение 2: Статистическая значимость GUE-распределения"
        else
          s = "Objection 2: GUE Spacing Statistical Significance"
        end if
      case ('o2_count_a')
        if (lang_id == 2) then; s = "Вычислено"; else; s = "Computed"; end if
      case ('o2_count_b')
        if (lang_id == 2) then
          s = "нормированных спейсингов"
        else
          s = "normalized spacings"
        end if
      case ('o2_mean_a')
        if (lang_id == 2) then
          s = "Средний спейсинг: "
        else
          s = "Spacing mean: "
        end if
      case ('o2_mean_b')
        if (lang_id == 2) then; s = "  дисперсия: "; else; s = "  var: "; end if
      case ('o2_ks_a')
        if (lang_id == 2) then
          s = "Колмогоров-Смирнов:  D = "
        else
          s = "Kolmogorov-Smirnov:  D = "
        end if
      case ('o2_ks_b')
        if (lang_id == 2) then
          s = ",  p-значение = "
        else
          s = ",  p-value = "
        end if
      case ('o2_cvm_a')
        if (lang_id == 2) then
          s = "Крамер-фон Мизес:    W2 = "
        else
          s = "Cramer-von Mises:    W2 = "
        end if
      case ('o2_ad_a')
        if (lang_id == 2) then
          s = "Андерсон-Дарлинг:     A2 = "
        else
          s = "Anderson-Darling:   A2 = "
        end if
      case ('o2_rm_a')
        if (lang_id == 2) then
          s = "<r> (отношение соседних): "
        else
          s = "<r> (adjacent-ratio): "
        end if
      case ('o2_rm_b')
        if (lang_id == 2) then
          s = ", GUE ~= 0.5992)"
        else
          s = ", GUE surmise ~ 0.5992)"
        end if
      case ('o2_res_a')
        if (lang_id == 2) then
          s = "H0 (GUE-распределение): "
        else
          s = "H0 (GUE distribution): "
        end if
      case ('o2_rej')
        if (lang_id == 2) then; s = "ОТВЕРГНУТА"; else; s = "REJECTED"; end if
      case ('o2_norej')
        if (lang_id == 2) then
          s = "НЕ ОТВЕРГНУТА"
        else
          s = "NOT REJECTED"
        end if
      case ('o2_note1')
        if (lang_id == 2) then
          s = "  Примечание: при больших n точная GUE-сурьмида формально" // &
              " отвергается — это"
        else
          s = "  Note: at large n the exact GUE surmise is formally rejected" // &
              " — the"
        end if
      case ('o2_note2')
        if (lang_id == 2) then
          s = "  известные поправки конечных T у нулей дзеты, а не дефект данных"
        else
          s = "  known finite-T corrections of the zeta zeros, not a data artifact"
        end if
      case ('o2_note3')
        if (lang_id == 2) then
          s = "  (среднее ~ 1 подтверждает развёртку; якоря golden)."
        else
          s = "  (mean ~ 1 validates the unfolding; golden-anchored)."
        end if

      ! --- objection 3 -----------------------------------------------------
      case ('o3_title')
        if (lang_id == 2) then
          s = "Возражение 3: Скорость убывания при больших T"
        else
          s = "Objection 3: Large-T Decay Rate"
        end if
      case ('o3_calc')
        if (lang_id == 2) then
          s = "  Вычисление b(N) для нескольких N ..."
        else
          s = "  Computing b(N) at multiple N values ..."
        end if
      case ('o3_fit_a')
        if (lang_id == 2) then
          s = "  Линейная аппроксимация  log(b(N)) = "
        else
          s = "  Linear fit  log(b(N)) = "
        end if
      case ('o3_mid')
        s = " * log(N) + "
      case ('o3_r2')
        if (lang_id == 2) then; s = "  R2 = "; else; s = "  R^2 = "; end if
      case ('o3_expect')
        if (lang_id == 2) then
          s = "  Ожидаемый наклон ~ -0.5  (b(N) = O(1/sqrt(N)))"
        else
          s = "  Expected slope ~ -0.5  (b(N) = O(1/sqrt(N)))"
        end if
      case ('o3_ci_a')
        if (lang_id == 2) then
          s = "  95% ДИ для наклона: ["
        else
          s = "  95% CI for slope: ["
        end if
      case ('o3_verd_a')
        if (lang_id == 2) then
          s = "  Наклон "
        else
          s = "  Slope "
        end if
      case ('o3_within')
        if (lang_id == 2) then; s = "внутри"; else; s = "within"; end if
      case ('o3_outside')
        if (lang_id == 2) then; s = "вне"; else; s = "outside"; end if
      case ('o3_cons')
        if (lang_id == 2) then
          s = "СОГЛАСУЕТСЯ с O(1/sqrt(N))"
        else
          s = "CONSISTENT with O(1/sqrt(N))"
        end if
      case ('o3_incons')
        if (lang_id == 2) then
          s = "НЕ СОГЛАСУЕТСЯ с O(1/sqrt(N))"
        else
          s = "INCONSISTENT with O(1/sqrt(N))"
        end if
      case ('o3_warn')
        if (lang_id == 2) then
          s = "  ПРЕДУПРЕЖДЕНИЕ: недостаточно точек для регрессии"
        else
          s = "  WARNING: Not enough data points for regression"
        end if

      ! --- summary ---------------------------------------------------------
      case ('sum_title')
        if (lang_id == 2) then
          s = "Итоги проверки"
        else
          s = "Verification Summary"
        end if
      case ('sum_obj')
        if (lang_id == 2) then; s = "Возражение"; else; s = "Objection"; end if
      case ('s_pass')
        if (lang_id == 2) then; s = "ПРОЙДЕНО"; else; s = "PASS"; end if
      case ('s_fail')
        if (lang_id == 2) then; s = "СБОЙ"; else; s = "FAIL"; end if
      case ('s_warn')
        if (lang_id == 2) then; s = "ПРЕДУПР."; else; s = "WARN"; end if

      case default
        s = '?'
    end select
  end function msg

  !=============================================================================
  ! CLI parsing (spec §9): --zeros N --source NAME --objection X --lang L
  !                        --data-dir D
  !=============================================================================
  subroutine parse_args()
    integer           :: i, nargs, ios
    character(len=256):: arg

    nargs = command_argument_count()
    i = 1
    do while (i <= nargs)
      call get_command_argument(i, arg)
      select case (trim(arg))
        case ('--zeros')
          if (i < nargs) then
            i = i + 1
            call get_command_argument(i, arg)
            read(arg, *, iostat = ios) n_zeros
            if (ios /= 0) n_zeros = 50000
          end if
        case ('--source')
          if (i < nargs) then
            i = i + 1
            call get_command_argument(i, arg)
            source_name = adjustl(arg)
          end if
        case ('--objection')
          if (i < nargs) then
            i = i + 1
            call get_command_argument(i, arg)
            select case (trim(arg))
              case ('all'); objection_id = 0
              case ('1');   objection_id = 1
              case ('2');   objection_id = 2
              case ('3');   objection_id = 3
              case default  ! ignore unknown values, keep default 'all'
            end select
          end if
        case ('--lang')
          if (i < nargs) then
            i = i + 1
            call get_command_argument(i, arg)
            if (trim(arg) == 'ru') then
              lang_id = 2
            else if (trim(arg) == 'en') then
              lang_id = 1
            end if
          end if
        case ('--data-dir')
          if (i < nargs) then
            i = i + 1
            call get_command_argument(i, arg)
            data_dir = adjustl(arg)
          end if
        case ('--no-selfcheck')
          skip_sc = .true.
        case ('--help', '-h')
          call print_usage()
          stop 0
        case default
          ! unknown flags are ignored (lenient CLI)
      end select
      i = i + 1
    end do
  end subroutine parse_args

  !=============================================================================
  ! Usage line (--help / -h).
  !=============================================================================
  subroutine print_usage()
    write(*, '(A)') 'AB-Cloud Verification Suite (Fortran port, canon v3.0)'
    write(*, '(A)') 'Usage: ab_cloud_verify [options]'
    write(*, '(A)') '  --zeros N          number of zeros to load (default 50000; 0 = all)'
    write(*, '(A)') '  --source NAME      auto|50k|50k_full|500k|2M|highT|2M_gz|csv|zeros6'
    write(*, '(A)') '  --objection X      1|2|3|all  (default all)'
    write(*, '(A)') '  --lang L           en|ru  (default: auto-detect from $LANG)'
    write(*, '(A)') '  --data-dir D       path to data/ (default ../data)'
    write(*, '(A)') '  --no-selfcheck     skip the frozen-anchor self-check'
    write(*, '(A)') '  --help             show this help'
  end subroutine print_usage

  !=============================================================================
  ! Zero loader (spec §9 source registry).
  ! Sources: 50k, 50k_full, 500k, 2M, highT (BLOCK offset format), 2M_gz
  ! (decompressed via gzip -dc into a temporary file), csv, zeros6.
  ! auto = smallest file whose approximate count >= requested zeros.
  !=============================================================================
  subroutine load_zeros(z, n_out, nreq, source, datadir)
    real(dp), allocatable, intent(out) :: z(:)
    integer, intent(out)          :: n_out
    integer, intent(in)           :: nreq
    character(len=*), intent(in)  :: source
    character(len=*), intent(in)  :: datadir

    integer, parameter               :: NSRC = 8
    character(len=16)                :: sname(NSRC)
    character(len=40)                :: sfile(NSRC)
    integer                          :: savail(NSRC)
    character(len=640)               :: filepath
    character(len=64)                :: fname
    integer                          :: fmt_id        ! 1 plain, 2 highT, 3 csv
    integer                          :: best, i, avail
    integer                          :: u, ios, cnt, cap, nkeep
    real(dp), allocatable            :: zbuf(:)
    real(dp)                         :: val, base_off
    character(len=1024)              :: line
    integer                          :: ll, c1, c2, p
    integer                          :: gzs
    character(len=640)               :: gzcmd, tmpname
    character(len=9)                 :: tmpsuf
    integer                          :: dtv(8)
    logical                          :: file_exists

    sname(1) = '50k';     sfile(1) = 'zeta_zeros_50000.txt'
    savail(1) = 13661
    sname(2) = '50k_full'; sfile(2) = 'zeta_zeros_50000_embedded.txt'
    savail(2) = 50000
    sname(3) = '500k';    sfile(3) = 'zeta_zeros_500k_odlyzko.txt'
    savail(3) = 500000
    sname(4) = '2M';      sfile(4) = 'zeta_zeros_2M_odlyzko.txt'
    savail(4) = 2001052
    sname(5) = 'highT';   sfile(5) = 'zeta_zeros_highT_blocks.txt'
    savail(5) = 30000
    sname(6) = '2M_gz';   sfile(6) = 'zeta_zeros_2M_odlyzko.txt.gz'
    savail(6) = 2001052
    sname(7) = 'csv';     sfile(7) = 'zeta_zeros_50000.csv'
    savail(7) = 13661
    sname(8) = 'zeros6';  sfile(8) = 'zeros6.txt'
    savail(8) = 2001052

    n_out = 0

    ! --- source selection ----------------------------------------------------
    if (trim(source) == 'auto') then
      best = 0
      avail = 0
      do i = 1, NSRC
        if (savail(i) >= nreq) then
          if (best == 0 .or. savail(i) < avail) then
            best = i
            avail = savail(i)
          end if
        end if
      end do
      if (best == 0) then
        write(error_unit, '(A,I0)') trim(msg('err_nosrc')), nreq
        return
      end if
      fname = sfile(best)
      write(*, '(2X,A,A,A,I0,A,I0,A)') trim(msg('asel_a')), trim(sname(best)), &
         trim(msg('asel_b')), nreq, trim(msg('asel_c')), savail(best), ")"
    else
      best = 0
      do i = 1, NSRC
        if (trim(sname(i)) == trim(source)) then
          best = i
          exit
        end if
      end do
      if (best == 0) then
        write(error_unit, '(A,I0)') trim(msg('err_nosrc')), nreq
        return
      end if
      fname = sfile(best)
    end if

    filepath = trim(datadir)
    if (len_trim(filepath) > 0 .and. filepath(len_trim(filepath):len_trim(filepath)) /= '/') then
      filepath = trim(filepath) // '/'
    end if
    filepath = trim(filepath) // trim(fname)

    write(*, '(2X,A,1X,I0,1X,A,A,A)') trim(msg('load_a')), nreq, &
        trim(msg('load_b')), trim(fname), "' ..."

    inquire(file = trim(filepath), exist = file_exists)
    if (.not. file_exists) then
      write(error_unit, '(A,A)') trim(msg('err_notfound')), trim(filepath)
      return
    end if

    ! --- format dispatch -----------------------------------------------------
    fmt_id = 1
    if (trim(fname) == 'zeta_zeros_highT_blocks.txt') fmt_id = 2
    if (trim(fname) == 'zeta_zeros_50000.csv')        fmt_id = 3

    ! --- 2M_gz: decompress via gzip -dc into a temp file ---------------------
    if (fmt_id == 1 .and. fname(len_trim(fname)-2:len_trim(fname)) == '.gz') then
      call date_and_time(values = dtv)
      write(tmpsuf, '(I2.2,I2.2,I2.2,I3.3)') dtv(5), dtv(6), dtv(7), dtv(8)
      tmpname = '/tmp/abcv_zeros_' // trim(tmpsuf) // '.txt'
      gzcmd = 'gzip -dc "' // trim(filepath) // '" > "' // trim(tmpname) // '"'
      call execute_command_line(trim(gzcmd), wait = .true., exitstat = gzs)
      if (gzs /= 0) then
        write(error_unit, '(A,A,A,I0,A)') trim(msg('err_gz')), trim(fname), &
            " (exit ", gzs, ")"
        return
      end if
      filepath = tmpname
    end if

    open(newunit = u, file = trim(filepath), status = 'old', action = 'read', &
         iostat = ios, form = 'formatted')
    if (ios /= 0) then
      write(error_unit, '(A,A)') trim(msg('err_open')), trim(filepath)
      return
    end if

    ! --- single pass, growable buffer ----------------------------------------
    cap = 65536
    allocate(zbuf(cap))
    cnt = 0
    base_off = 0.0_dp

    do
      read(u, '(A)', iostat = ios) line
      if (ios /= 0) exit

      ! strip trailing CR (CRLF-safe)
      ll = len_trim(line)
      do while (ll >= 1 .and. line(ll:ll) == achar(13))
        line(ll:ll) = ' '
        ll = ll - 1
      end do
      line = adjustl(line)
      if (len_trim(line) == 0) cycle

      select case (fmt_id)
        case (1)                                  ! plain: one float per line
          if (line(1:1) == '#') cycle
          read(line, *, iostat = ios) val
          if (ios /= 0) cycle
          call push_val(zbuf, cap, cnt, val)

        case (2)                                  ! highT BLOCK-offset format
          if (line(1:1) == '#') then
            p = index(line, 'BLOCK')
            c1 = index(line, 'offset=')
            if (p > 0 .and. c1 > 0) then
              read(line(c1+7:), *, iostat = ios) base_off
              if (ios /= 0) base_off = 0.0_dp
            end if
            cycle
          end if
          read(line, *, iostat = ios) val
          if (ios /= 0) cycle
          call push_val(zbuf, cap, cnt, base_off + val)

        case (3)                                  ! csv: 2nd column is t
          if (line(1:1) == '#') cycle
          c1 = index(line, ',')
          if (c1 == 0) cycle
          c2 = index(line(c1+1:), ',')
          if (c2 == 0) cycle
          read(line(c1+1:c1+c2-1), *, iostat = ios) val
          if (ios /= 0) cycle
          call push_val(zbuf, cap, cnt, val)
      end select
    end do
    close(u)

    ! --- sort ascending, truncate to nreq ------------------------------------
    call sort_real64(zbuf(1:cnt))

    ! Truncate to the requested count (nreq <= 0 -> keep everything).
    nkeep = cnt
    if (nreq > 0 .and. nreq < nkeep) nkeep = nreq
    if (nkeep <= 0) then
      deallocate(zbuf)
      return
    end if

    allocate(z(nkeep))
    z(1:nkeep) = zbuf(1:nkeep)
    deallocate(zbuf)
    n_out = nkeep

    if (fmt_id == 1 .and. fname(len_trim(fname)-2:len_trim(fname)) == '.gz') then
      open(newunit = u, file = trim(filepath), status = 'old', iostat = ios)
      if (ios == 0) close(u, status = 'delete')
    end if

    write(*, '(2X,A,1X,I0,1X,A,A,A,F12.4,A,F12.4,A)') trim(msg('loaded_a')), &
        n_out, trim(msg('loaded_b')), trim(fname), trim(msg('loaded_c')), &
        z(1), ", ", z(n_out), "]"
  end subroutine load_zeros

  !=============================================================================
  ! Growable-buffer push helper.
  !=============================================================================
  subroutine push_val(buf, cap, cnt, v)
    real(dp), allocatable, intent(inout) :: buf(:)
    integer, intent(inout) :: cap
    integer, intent(inout) :: cnt
    real(dp), intent(in)   :: v
    real(dp), allocatable  :: tmp(:)

    if (cnt >= cap) then
      allocate(tmp(2*cap))
      tmp(1:cap) = buf
      call move_alloc(tmp, buf)
      cap = 2*cap
    end if
    cnt = cnt + 1
    buf(cnt) = v
  end subroutine push_val

  !=============================================================================
  ! Bottom-up merge sort, ascending (stable, O(n log n), no recursion).
  !=============================================================================
  subroutine sort_real64(a)
    real(dp), intent(inout) :: a(:)
    real(dp), allocatable   :: tmp(:)
    integer :: nn, wdt, lo, mid, hi, l, r, k

    nn = size(a)
    if (nn < 2) return
    allocate(tmp(nn))
    wdt = 1
    do while (wdt < nn)
      lo = 1
      do while (lo <= nn)
        mid = min(lo + wdt - 1, nn)
        hi  = min(lo + 2*wdt - 1, nn)
        l = lo
        r = mid + 1
        k = lo
        do while (l <= mid .and. r <= hi)
          if (a(l) <= a(r)) then
            tmp(k) = a(l)
            l = l + 1
          else
            tmp(k) = a(r)
            r = r + 1
          end if
          k = k + 1
        end do
        do while (l <= mid)
          tmp(k) = a(l); l = l + 1; k = k + 1
        end do
        do while (r <= hi)
          tmp(k) = a(r); r = r + 1; k = k + 1
        end do
        lo = hi + 1
      end do
      a = tmp
      wdt = 2*wdt
    end do
    deallocate(tmp)
  end subroutine sort_real64

  !=============================================================================
  ! Lambert W, principal branch (spec §1; canonical reference implementation:
  ! fp-guard and small-x seed from the canonical Python port — the naive
  ! spec seed log(k/e) lands exactly on w = -1 for k = 1, where the Newton
  ! denominator vanishes).
  !=============================================================================
  function lambert_w(x) result(w)
    real(dp), intent(in) :: x
    real(dp)             :: w, ew, f, fp, delta
    integer              :: it

    if (x <= 0.0_dp) then
      w = 0.0_dp
      return
    end if
    w = log(max(x, 1.0e-30_dp))
    if (w < 0.0_dp) w = x          ! for small x, W(x) ~ x
    do it = 1, 50
      ew = exp(w)
      f  = w*ew - x
      fp = ew*(w + 1.0_dp)
      if (abs(fp) < 1.0e-30_dp) exit
      delta = f/fp
      w = w - delta
      if (abs(delta) < 1.0e-12_dp*max(abs(w), 1.0_dp)) exit
    end do
  end function lambert_w

  !=============================================================================
  ! Gram point (spec §2 — CANON): seed t = 2*pi*k / W(k/e), then 8 Newton
  ! iterations on the 5-term Riemann–Siegel theta expansion:
  !   theta(t) = (t/2) ln(t/2pi) - t/2 - pi/8 + 1/(48t) + 7/(5760 t^3)
  !=============================================================================
  function gram_point(k) result(t_out)
    integer, intent(in) :: k
    real(dp)            :: t_out, t, arg, theta, dtheta
    integer             :: it

    if (k <= 0) then
      t_out = 0.0_dp
      return
    end if
    t = (TWO_PI*real(k, dp))/lambert_w(real(k, dp)/E_E)
    do it = 1, 8
      arg = t/TWO_PI
      if (arg <= 0.0_dp) exit
      theta = (t/2.0_dp)*log(arg) - t/2.0_dp - PI/8.0_dp &
              + 1.0_dp/(48.0_dp*t) + 7.0_dp/(5760.0_dp*t*t*t)
      dtheta = 0.5_dp*log(arg) - 1.0_dp/(48.0_dp*t*t) &
               - 21.0_dp/(5760.0_dp*t*t*t*t)
      if (abs(dtheta) < 1.0e-30_dp) exit
      t = t - (theta - PI*real(k, dp))/dtheta
    end do
    t_out = t
  end function gram_point

  !=============================================================================
  ! Prefix sums for b(N): pref(N)/N is bit-identical to the direct sequential
  ! sum (spec §3, §7).  Same accumulation order as compute_bN.
  !=============================================================================
  subroutine build_prefix(z, n, pref)
    real(dp), intent(in)  :: z(:)
    integer, intent(in)   :: n
    real(dp), intent(out) :: pref(0:n)
    integer :: k

    pref(0) = 0.0_dp
    do k = 1, n
      pref(k) = pref(k-1) + abs(z(k) - gram_point(k))
    end do
  end subroutine build_prefix

  !=============================================================================
  ! b(N; offset) — zeros 1..N against Gram points offset+1 .. offset+N (spec §3)
  !=============================================================================
  function bN_offset(z, n, nzeros, off) result(v)
    real(dp), intent(in)  :: z(:)
    integer, intent(in)   :: n, nzeros, off
    real(dp)              :: v, acc
    integer               :: k

    if (nzeros <= 0 .or. off + nzeros > n) then
      v = nan_dp
      return
    end if
    acc = 0.0_dp
    do k = 1, nzeros
      acc = acc + abs(z(k) - gram_point(off + k))
    end do
    v = acc/real(nzeros, dp)
  end function bN_offset

  !=============================================================================
  ! GUE CDF (spec §5): exact closed form through a 32768-point interpolation
  ! table on [0, SMAX]; outside the table the exact form is used.
  !=============================================================================
  function gue_exact(s) result(v)
    real(dp), intent(in) :: s
    real(dp)             :: v

    v = erf(2.0_dp*s/sqrt(PI)) - (4.0_dp*s/PI)*exp(-4.0_dp*s*s/PI)
  end function gue_exact

  function gue_cdf(s) result(cdf)
    real(dp), intent(in) :: s
    real(dp)             :: cdf, x, tt
    real(dp), save       :: gtab(0:GUE_TN-1)
    logical, save        :: built = .false.
    integer              :: i

    if (s <= 0.0_dp) then
      cdf = 0.0_dp
      return
    end if
    if (s >= GUE_SMAX) then
      cdf = gue_exact(s)
      return
    end if
    if (.not. built) then
      do i = 0, GUE_TN-1
        gtab(i) = gue_exact(real(i, dp)*GUE_SMAX/real(GUE_TN-1, dp))
      end do
      built = .true.
    end if
    x = s*real(GUE_TN-1, dp)/GUE_SMAX
    i = int(floor(x))
    if (i < 0 .or. i >= GUE_TN-1) then
      cdf = gue_exact(s)
      return
    end if
    tt = x - real(i, dp)
    cdf = (1.0_dp - tt)*gtab(i) + tt*gtab(i+1)
  end function gue_cdf

  !=============================================================================
  ! Kolmogorov asymptotic p-value, lambda-corrected, two branches (spec §6).
  !=============================================================================
  function ks_asym_p(lam) result(v)
    real(dp), intent(in) :: lam
    real(dp)             :: v, s2, term
    integer              :: k, sgn

    if (lam <= 0.0_dp) then
      v = 1.0_dp
      return
    end if
    if (lam < 0.6_dp) then
      s2 = 0.0_dp
      do k = 1, 1000
        term = exp(-(((real(2*k - 1, dp)**2)*(PI**2))/(8.0_dp*lam*lam)))
        s2 = s2 + term
        if (term < 1.0e-18_dp) exit
      end do
      v = 1.0_dp - SQRT_2PI/lam*s2
    else
      s2 = 0.0_dp
      sgn = 1
      do k = 1, 100
        term = real(sgn, dp)*exp(-2.0_dp*real(k, dp)**2*lam*lam)
        s2 = s2 + term
        sgn = -sgn
        if (abs(term) < 1.0e-18_dp) exit
      end do
      v = 2.0_dp*s2
    end if
    v = max(0.0_dp, min(1.0_dp, v))
  end function ks_asym_p

  !=============================================================================
  ! KS test: two-sided D and lambda-corrected p (spec §6).
  ! Input: sorted ascending spacings sp(1:m).
  !=============================================================================
  subroutine ks_test(sp, m, D, pval)
    real(dp), intent(in)  :: sp(:)
    integer, intent(in)   :: m
    real(dp), intent(out) :: D, pval
    real(dp)              :: Fx, d1, d2, lam
    integer               :: i

    if (m <= 0) then
      D = 0.0_dp
      pval = 1.0_dp
      return
    end if
    D = 0.0_dp
    do i = 1, m
      Fx = gue_cdf(sp(i))
      d1 = abs(real(i, dp)/real(m, dp) - Fx)
      d2 = abs(real(i - 1, dp)/real(m, dp) - Fx)
      if (d1 > D) D = d1
      if (d2 > D) D = d2
    end do
    lam = (sqrt(real(m, dp)) + 0.12_dp + 0.11_dp/sqrt(real(m, dp)))*D
    pval = ks_asym_p(lam)
  end subroutine ks_test

  !=============================================================================
  ! Cramer–von Mises W2 (spec §6).  Input sorted ascending.
  !=============================================================================
  function cramer_von_mises(sp, m) result(W2)
    real(dp), intent(in) :: sp(:)
    integer, intent(in)  :: m
    real(dp)             :: W2, Fx
    integer              :: i

    if (m <= 0) then
      W2 = 0.0_dp
      return
    end if
    W2 = 1.0_dp/(12.0_dp*real(m, dp))
    do i = 1, m
      Fx = gue_cdf(sp(i))
      W2 = W2 + ((real(2*i - 1, dp)/(2.0_dp*real(m, dp))) - Fx)**2
    end do
  end function cramer_von_mises

  !=============================================================================
  ! Anderson–Darling A2 with 1e-300 / 1-1e-16 clamps (spec §6).  Sorted input.
  !=============================================================================
  function anderson_darling(sp, m) result(A2)
    real(dp), intent(in) :: sp(:)
    integer, intent(in)  :: m
    real(dp)             :: A2, acc, Fi, Fni
    integer              :: i

    if (m < 2) then
      A2 = nan_dp
      return
    end if
    acc = 0.0_dp
    do i = 1, m
      Fi  = min(max(gue_cdf(sp(i)), 1.0e-300_dp), 1.0_dp - 1.0e-16_dp)
      Fni = min(max(gue_cdf(sp(m + 1 - i)), 1.0e-300_dp), 1.0_dp - 1.0e-16_dp)
      acc = acc + real(2*i - 1, dp)*(log(Fi) + log(1.0_dp - Fni))
    end do
    A2 = -real(m, dp) - acc/real(m, dp)
  end function anderson_darling

  !=============================================================================
  ! <r> adjacent-gap ratio (spec §6): mean over adjacent gap pairs of
  ! min/max, skipping pairs where both gaps are 0.
  !=============================================================================
  subroutine mean_adjacent_ratio(z, n, r, n_r)
    real(dp), intent(in)  :: z(:)
    integer, intent(in)   :: n
    real(dp), intent(out) :: r
    integer, intent(out)  :: n_r
    real(dp)              :: acc, a, b, mx
    integer               :: i, ng

    if (n < 3) then
      r = nan_dp
      n_r = 0
      return
    end if
    ng = n - 1
    acc = 0.0_dp
    n_r = 0
    do i = 1, ng - 1
      a = z(i+1) - z(i)
      b = z(i+2) - z(i+1)
      if (a == 0.0_dp .and. b == 0.0_dp) cycle
      mx = max(a, b)
      acc = acc + min(a, b)/mx
      n_r = n_r + 1
    end do
    if (n_r == 0) then
      r = nan_dp
    else
      r = acc/real(n_r, dp)
    end if
  end subroutine mean_adjacent_ratio

  !=============================================================================
  ! Normalized spacings (spec §4), preserving order of the loaded zeros.
  ! Returns allocated sp(1:m); m = number of spacings kept.
  !=============================================================================
  subroutine compute_spacings(z, n, sp, m)
    real(dp), intent(in)              :: z(:)
    integer, intent(in)               :: n
    real(dp), allocatable, intent(out):: sp(:)
    integer, intent(out)              :: m
    integer                           :: k, cnt

    m = 0
    if (n < 2) then
      allocate(sp(0))
      return
    end if
    allocate(sp(n - 1))
    cnt = 0
    do k = 1, n - 1
      if (z(k) > 0.0_dp) then
        cnt = cnt + 1
        sp(cnt) = (z(k+1) - z(k))*log(z(k)/TWO_PI)/TWO_PI
      end if
    end do
    m = cnt
  end subroutine compute_spacings

  !=============================================================================
  ! OLS linear regression with slope stderr and R^2 (spec §7 obj1/obj3).
  !=============================================================================
  subroutine ols_fit(x, y, npts, slope, inter, se, r2)
    real(dp), intent(in)  :: x(:), y(:)
    integer, intent(in)   :: npts
    real(dp), intent(out) :: slope, inter, se, r2
    real(dp) :: sx, sy, sxx, sxy, denom, ymean, sstot, ssres, mse, yi, yhat
    integer  :: i

    slope = 0.0_dp; inter = 0.0_dp; se = 0.0_dp; r2 = 0.0_dp
    if (npts < 2) return

    sx = 0.0_dp; sy = 0.0_dp; sxx = 0.0_dp; sxy = 0.0_dp
    do i = 1, npts
      sx  = sx + x(i)
      sy  = sy + y(i)
      sxx = sxx + x(i)*x(i)
      sxy = sxy + x(i)*y(i)
    end do
    denom = real(npts, dp)*sxx - sx*sx
    if (abs(denom) < 1.0e-30_dp) return

    slope = (real(npts, dp)*sxy - sx*sy)/denom
    inter = (sy - slope*sx)/real(npts, dp)

    ymean = sy/real(npts, dp)
    sstot = 0.0_dp
    ssres = 0.0_dp
    do i = 1, npts
      yi   = y(i)
      yhat = slope*x(i) + inter
      sstot = sstot + (yi - ymean)**2
      ssres = ssres + (yi - yhat)**2
    end do
    if (sstot > 0.0_dp) r2 = 1.0_dp - ssres/sstot

    if (npts > 2) then
      mse = ssres/real(npts - 2, dp)
    else
      mse = 0.0_dp
    end if
    if (denom > 0.0_dp) se = sqrt(mse*real(npts, dp)/denom)
  end subroutine ols_fit

  !=============================================================================
  ! %.12g-style formatter for selfcheck rows.
  !=============================================================================
  function g12(v) result(s)
    real(dp), intent(in) :: v
    character(len=26)    :: s

    if (v /= v) then
      s = 'NaN'
      return
    end if
    if (v == 0.0_dp .or. (abs(v) >= 1.0e-4_dp .and. abs(v) < 1.0e12_dp)) then
      write(s, '(F26.16)') v
    else
      write(s, '(ES26.14E2)') v
    end if
    s = adjustl(s)
  end function g12

  !=============================================================================
  ! Objection 1: numerical stability of b(N) (spec §7).
  ! Grid {100,500,1000,5000,10000,50000} filtered to N <= n (fallback
  ! min(n,100)); monotone-honest verdict; optional empirical power-law fit.
  !=============================================================================
  subroutine verify_objection1(z, n, pref, converged)
    real(dp), intent(in)  :: z(:)
    integer, intent(in)   :: n
    real(dp), intent(in)  :: pref(0:n)
    logical, intent(out)  :: converged

    integer, parameter :: NG = 6
    integer  :: grid(NG), nv(NG), i, npts, cnt, nfit
    real(dp) :: bvals(NG), bN, xs(NG), ys(NG)
    real(dp) :: slope, inter, se, r2, afit, sfit
    character(len=24) :: ds
    character(len=20) :: h1, h2, h3
    logical :: mono

    grid = (/100, 500, 1000, 5000, 10000, 50000/)
    cnt = 0
    do i = 1, NG
      if (grid(i) <= n) then
        cnt = cnt + 1
        nv(cnt) = grid(i)
      end if
    end do
    if (cnt == 0) then
      cnt = 1
      nv(1) = min(n, 100)
    end if

    write(*, '(/,A)') repeat('=', 60)
    write(*, '(A)') trim(msg('o1_title'))
    write(*, '(A)') trim(msg('o1_conv'))
    h1 = 'N'
    h2 = 'b(N)'
    h3 = 'Δb = b(N)−b(prev)'
    write(*, '(A10,2X,A20,2X,A20)') adjustr(h1), adjustr(h2), adjustr(h3)
    write(*, '(A)') repeat('-', 60)

    npts = 0
    do i = 1, cnt
      bN = pref(nv(i))/real(nv(i), dp)
      npts = npts + 1
      bvals(npts) = bN
      if (npts == 1) then
        ds = repeat(' ', 24)
        ds(1:24) = '---'
      else
        write(ds, '(SP,F23.10)') bN - bvals(npts-1)
      end if
      write(*, '(I10,2X,F20.10,2X,A)') nv(i), bN, trim(adjustl(ds))
    end do

    ! Empirical power-law fit over the printed table (honest: EMPIRICAL)
    nfit = 0
    do i = 1, npts
      if (nv(i) > 1 .and. bvals(i) > 0.0_dp) then
        nfit = nfit + 1
        xs(nfit) = log(real(nv(i), dp))
        ys(nfit) = log(bvals(i))
      end if
    end do
    if (nfit >= 3) then
      call ols_fit(xs(1:nfit), ys(1:nfit), nfit, slope, inter, se, r2)
      afit = exp(inter)
      sfit = -slope
      write(*, '(A,F10.4,A,F8.4,A,F8.4,A)') trim(msg('o1_fit_a')), afit, &
          trim(msg('o1_fit_b')), sfit, trim(msg('o1_fit_c')), r2, ")"
    end if

    ! Honest verdict: monotone decrease across the table (and >= 3 rows)
    mono = .true.
    do i = 1, npts - 1
      if (bvals(i+1) >= bvals(i)) mono = .false.
    end do
    converged = (mono .and. npts >= 3)
    if (converged) then
      write(*, '(A)') trim(msg('o1_honest'))
    else
      write(*, '(A)') trim(msg('o1_honest_bad'))
    end if
  end subroutine verify_objection1

  !=============================================================================
  ! Objection 2: GUE spacing statistics on ALL loaded zeros (spec §7):
  ! mean/var, KS D+p, CvM, AD, <r> vs GUE reference 0.5992.
  ! Honest rejection note printed ONLY when H0 is actually rejected.
  !=============================================================================
  subroutine verify_objection2(z, n, rejected)
    real(dp), intent(in)  :: z(:)
    integer, intent(in)   :: n
    logical, intent(out)  :: rejected

    real(dp), allocatable :: sp(:)
    real(dp) :: mean_s, var_s, acc, D, pval, W2, A2, r
    integer  :: m, n_r, i

    write(*, '(/,A)') repeat('=', 60)
    write(*, '(A)') trim(msg('o2_title'))

    call compute_spacings(z, n, sp, m)
    write(*, '(2X,A,1X,I0,1X,A)') trim(msg('o2_count_a')), m, &
        trim(msg('o2_count_b'))

    ! mean / var (sample variance, n-1) — sequential order
    if (m > 0) then
      acc = 0.0_dp
      do i = 1, m
        acc = acc + sp(i)
      end do
      mean_s = acc/real(m, dp)
    else
      mean_s = nan_dp
    end if
    if (m > 1) then
      acc = 0.0_dp
      do i = 1, m
        acc = acc + (sp(i) - mean_s)**2
      end do
      var_s = acc/real(m - 1, dp)
    else
      var_s = nan_dp
    end if
    write(*, '(2X,A,F18.9,A,F18.9,A,I0,A)') trim(msg('o2_mean_a')), mean_s, &
        trim(msg('o2_mean_b')), var_s, "  (n = ", m, ")"

    ! KS (sorted spacings)
    call sort_real64(sp(1:m))
    call ks_test(sp, m, D, pval)
    write(*, '(2X,A,F12.6,A,ES13.6)') trim(msg('o2_ks_a')), D, &
        trim(msg('o2_ks_b')), pval

    ! Cramer–von Mises
    W2 = cramer_von_mises(sp, m)
    write(*, '(2X,A,F14.6)') trim(msg('o2_cvm_a')), W2

    ! Anderson–Darling
    A2 = anderson_darling(sp, m)
    write(*, '(2X,A,F14.6)') trim(msg('o2_ad_a')), A2

    ! <r> adjacent-gap ratio
    call mean_adjacent_ratio(z, n, r, n_r)
    write(*, '(2X,A,F12.6,A,I0,A)') trim(msg('o2_rm_a')), r, "  (n = ", n_r, &
        trim(msg('o2_rm_b'))

    ! Verdict (honest, number-driven)
    rejected = (pval < 0.05_dp)
    if (rejected) then
      write(*, '(2X,A,A,A)') trim(msg('o2_res_a')), trim(msg('o2_rej')), &
          "  (alpha = 0.05)"
      write(*, '(A)') trim(msg('o2_note1'))
      write(*, '(A)') trim(msg('o2_note2'))
      write(*, '(A)') trim(msg('o2_note3'))
    else
      write(*, '(2X,A,A,A)') trim(msg('o2_res_a')), trim(msg('o2_norej')), &
          "  (alpha = 0.05)"
    end if

    deallocate(sp)
  end subroutine verify_objection2

  !=============================================================================
  ! Objection 3: large-T decay rate (spec §7).  Grid 50*2^k while <= n, plus
  ! n itself if not already present; OLS on log b(N) vs log N; slope stderr;
  ! 95% CI (+-1.96*se); honest verdict about -0.5.
  !=============================================================================
  subroutine verify_objection3(z, n, pref, consistent)
    real(dp), intent(in)  :: z(:)
    integer, intent(in)   :: n
    real(dp), intent(in)  :: pref(0:n)
    logical, intent(out)  :: consistent

    integer, parameter :: MAXG = 64
    integer  :: grid(MAXG), ng, i, nfit
    integer  :: ncur
    real(dp) :: bN, xs(MAXG), ys(MAXG)
    real(dp) :: slope, inter, se, r2, ci_lo, ci_hi
    logical  :: already

    ng = 0
    ncur = 50
    do while (ncur <= n .and. ng < MAXG)
      ng = ng + 1
      grid(ng) = ncur
      ncur = ncur*2
    end do
    if (ng > 0) then
      already = (grid(ng) == n)
    else
      already = .true.
    end if
    if (.not. already .and. n > 100 .and. ng < MAXG) then
      ng = ng + 1
      grid(ng) = n
    end if

    write(*, '(/,A)') repeat('=', 60)
    write(*, '(A)') trim(msg('o3_title'))
    write(*, '(A)') trim(msg('o3_calc'))

    nfit = 0
    do i = 1, ng
      bN = pref(grid(i))/real(grid(i), dp)
      if (bN <= 0.0_dp) cycle
      nfit = nfit + 1
      xs(nfit) = log(real(grid(i), dp))
      ys(nfit) = log(bN)
      write(*, '(6X,A,I8,4X,A,F18.10,4X,A,F14.6)') "N =", grid(i), "b(N) =", bN, &
          "log(b) =", ys(nfit)
    end do

    if (nfit < 3) then
      write(*, '(A)') trim(msg('o3_warn'))
      consistent = .false.
      return
    end if

    call ols_fit(xs(1:nfit), ys(1:nfit), nfit, slope, inter, se, r2)
    ci_lo = slope - 1.96_dp*se
    ci_hi = slope + 1.96_dp*se

    write(*, '(A,F10.4,A,F10.4)') trim(msg('o3_fit_a')), slope, &
        trim(msg('o3_mid')), inter
    write(*, '(A,F12.6)') trim(msg('o3_r2')), r2
    write(*, '(A)') trim(msg('o3_expect'))
    write(*, '(A,F10.4,A,F10.4,A)') trim(msg('o3_ci_a')), ci_lo, ", ", ci_hi, "]"

    consistent = (abs(slope - (-0.5_dp)) <= 0.1_dp)
    if (consistent) then
      write(*, '(A,F10.4,1X,A,A,A)') trim(msg('o3_verd_a')), slope, &
          trim(msg('o3_within')), " -0.5 +/- 0.1 -> ", trim(msg('o3_cons'))
    else
      write(*, '(A,F10.4,1X,A,A,A)') trim(msg('o3_verd_a')), slope, &
          trim(msg('o3_outside')), " -0.5 +/- 0.1 -> ", trim(msg('o3_incons'))
    end if
  end subroutine verify_objection3

  !=============================================================================
  ! Frozen-anchor self-check (spec §8).  Tolerances: lambert_w 1e-12 rel;
  ! gram_point/bN 1e-6 abs; mean/var, ks.D, cvm, ad, rmean 1e-9 (ks.p 1e-6
  ! rel).  Stats anchors on the FIRST 50000 zeros only (SKIP otherwise).
  ! Prints PASS/FAIL/SKIP + delta per anchor; npass/nfail to the caller.
  !=============================================================================
  subroutine selfcheck(z, n, pref, npass_out, nfail_out)
    real(dp), intent(in)  :: z(:)
    integer, intent(in)   :: n
    real(dp), intent(in)  :: pref(0:n)
    integer, intent(out)  :: npass_out, nfail_out

    real(dp) :: xl(6), xe(6), ge(8), be(6)
    integer  :: kg(8), nb(6)
    real(dp) :: mean_s, var_s, D, pval, W2, A2, r, acc1
    real(dp), allocatable :: z5(:), sp(:)
    integer  :: i, m, n_r, np, nf
    character(len=24) :: nm, st, lwn(6)

    ! --- anchor literals (spec §8, frozen) -----------------------------------
    data xl /0.5_dp, 1.0_dp, 3.7_dp, 10.0_dp, 271.8_dp, 12345.6_dp/
    data xe /0.35173371124919584_dp, 0.5671432904097838_dp, &
             1.1599531786120223_dp,  1.7455280027406992_dp, &
             4.17576816800275_dp,    7.417247034540566_dp/
    data kg /1, 2, 3, 10, 100, 1000, 10000, 50000/
    data ge /23.17028270133466_dp, 27.670182217848343_dp, 31.71797995477886_dp, &
             54.67523744685398_dp, 238.58259051450293_dp, 1421.25638903275_dp, &
             9878.910118894457_dp, 40434.6952780045_dp/
    data nb /100, 500, 1000, 5000, 10000, 50000/
    data be /3.3321638710140165_dp, 2.3912304957476382_dp, 2.1072522951855435_dp, &
             1.6299485869022874_dp, 1.4794053414584762_dp, 1.2125526772588608_dp/
    data lwn /'lambert_w(0.5)', 'lambert_w(1.0)', 'lambert_w(3.7)', &
              'lambert_w(10.0)', 'lambert_w(271.8)', 'lambert_w(12345.6)'/

    nrows = 0

    write(*, '(/,A)') repeat('=', 60)
    write(*, '(A)') trim(msg('sc_title'))

    ! --- lambert_w (1e-12 rel) -----------------------------------------------
    do i = 1, 6
      call check_row(lwn(i), lambert_w(xl(i)), xe(i), 1.0e-12_dp, .true.)
    end do

    ! --- gram_point (1e-6 abs) -----------------------------------------------
    do i = 1, 8
      write(nm, '(A,I0,A)') 'gram_point(n=', kg(i), ')'
      call check_row(nm, gram_point(kg(i)), ge(i), 1.0e-6_dp, .false.)
    end do

    ! --- bN anchors (need N <= n) --------------------------------------------
    do i = 1, 6
      if (nb(i) <= n) then
        write(nm, '(A,I0,A)') 'bN(N=', nb(i), ')'
        call check_row(nm, pref(nb(i))/real(nb(i), dp), be(i), 1.0e-6_dp, .false.)
      else
        write(st, '(A,I0,A)') 'bN(N=', nb(i), ')'
        write(*, '(2X,A24,1X,A16,A,I0,A,I0,A)') st, trim(msg('sc_skip')), &
            trim(msg('sc_need')), nb(i), trim(msg('sc_have')), n, ")"
      end if
    end do

    ! --- bN_off(1000,500) (needs n >= 1500) ----------------------------------
    if (n >= 1500) then
      call check_row('bN(N=1000,off=500)', bN_offset(z, n, 1000, 500), &
                      624.6201618180231_dp, 1.0e-6_dp, .false.)
    else
      write(*, '(2X,A24,1X,A16,A,I0,A,I0,A)') 'bN(N=1000,off=500)', &
          trim(msg('sc_skip')), trim(msg('sc_need')), 1500, &
          trim(msg('sc_have')), n, ")"
    end if

    ! --- statistics anchors (first 50000 zeros only) --------------------------
    if (n >= 50000) then
      allocate(z5(50000))
      z5 = z(1:50000)
      call compute_spacings(z5, 50000, sp, m)

      ! mean/var on the spacings in ORIGINAL zero order first (canonical
      ! Python selfcheck sums the unsorted list; sorting happens before the
      ! order-dependent KS/CvM/AD statistics only)
      acc1 = 0.0_dp
      do i = 1, m
        acc1 = acc1 + sp(i)
      end do
      mean_s = acc1/real(m, dp)
      acc1 = 0.0_dp
      do i = 1, m
        acc1 = acc1 + (sp(i) - mean_s)**2
      end do
      var_s = acc1/real(m - 1, dp)

      call sort_real64(sp(1:m))
      call ks_test(sp, m, D, pval)
      W2 = cramer_von_mises(sp, m)
      A2 = anderson_darling(sp, m)
      call mean_adjacent_ratio(z5, 50000, r, n_r)

      call check_row('spacings.mean', mean_s, 0.999976001221201_dp, 1.0e-9_dp, .false.)
      call check_row('spacings.var', var_s, 0.1590654827835423_dp, 1.0e-9_dp, .false.)
      call check_row('ks_zeros.D', D, 0.021619337032982328_dp, 1.0e-9_dp, .false.)
      call check_row('ks_zeros.p', pval, 9.567870399361496e-21_dp, 1.0e-6_dp, .true.)
      call check_row('cvm_zeros.W2', W2, 8.177703317829403_dp, 1.0e-9_dp, .true.)
      call check_row('ad_zeros.A2', A2, 61.49242624209728_dp, 1.0e-9_dp, .true.)
      call check_row('rmean_zeros.r', r, 0.6118798907208398_dp, 1.0e-9_dp, .false.)

      deallocate(sp)
      deallocate(z5)
    else
      write(*, '(2X,A24,1X,A16,A,I0,A,I0,A)') 'spacings.mean/var', &
          trim(msg('sc_skip')), trim(msg('sc_need')), 50000, &
          trim(msg('sc_have')), n, ")"
      write(*, '(2X,A24,1X,A16,A,I0,A,I0,A)') 'ks_zeros.D/p', &
          trim(msg('sc_skip')), trim(msg('sc_need')), 50000, &
          trim(msg('sc_have')), n, ")"
      write(*, '(2X,A24,1X,A16,A,I0,A,I0,A)') 'cvm_zeros.W2', &
          trim(msg('sc_skip')), trim(msg('sc_need')), 50000, &
          trim(msg('sc_have')), n, ")"
      write(*, '(2X,A24,1X,A16,A,I0,A,I0,A)') 'ad_zeros.A2', &
          trim(msg('sc_skip')), trim(msg('sc_need')), 50000, &
          trim(msg('sc_have')), n, ")"
      write(*, '(2X,A24,1X,A16,A,I0,A,I0,A)') 'rmean_zeros.r', &
          trim(msg('sc_skip')), trim(msg('sc_need')), 50000, &
          trim(msg('sc_have')), n, ")"
    end if

    ! --- print rows -----------------------------------------------------------
    np = 0
    do i = 1, nrows
      if (rok(i)) np = np + 1
      if (rok(i)) then
        st = trim(msg('sc_pass'))
      else
        st = trim(msg('sc_fail'))
      end if
      write(*, '(2X,A24,1X,A16,2X,A,A,A,A,A,ES10.3E2)') rname(i), st, &
          trim(msg('sc_comp')), trim(g12(rgot(i))), trim(msg('sc_exp')), &
          trim(g12(rexp(i))), ", D = ", rdel(i)
    end do
    nf = nrows - np

    write(*, '(2X,A,1X,I0,1X,A,1X,I0,1X,A)') trim(msg('sc_result')), np, &
        trim(msg('sc_passed')), nf, trim(msg('sc_failed'))

    npass_out = np
    nfail_out = nf
  end subroutine selfcheck

  !=============================================================================
  ! Append one self-check row (program-level: host association gives it the
  ! row buffer; called only from selfcheck).
  !=============================================================================
  subroutine check_row(nm_in, got_in, exp_in, tol, rel)
    character(len=*), intent(in) :: nm_in
    real(dp), intent(in) :: got_in, exp_in, tol
    logical, intent(in), optional :: rel
    real(dp) :: d
    logical  :: isrel

    isrel = .false.
    if (present(rel)) isrel = rel

    nrows = nrows + 1
    rname(nrows) = nm_in
    rgot(nrows) = got_in
    rexp(nrows) = exp_in
    if (got_in /= got_in) then
      rok(nrows) = .false.
      rdel(nrows) = huge(1.0_dp)
      return
    end if
    if (isrel) then
      d = abs(got_in - exp_in)/abs(exp_in)
    else
      d = abs(got_in - exp_in)
    end if
    rdel(nrows) = d
    rok(nrows) = (d <= tol)
  end subroutine check_row

  !=============================================================================
  ! Summary (spec §7): selfcheck n/n first, then per-objection status.
  !=============================================================================
  subroutine print_summary(np_, nf_, sc_run, r1, r2_, r3, c1, rej, con)
    integer, intent(in) :: np_, nf_
    logical, intent(in) :: sc_run, r1, r2_, r3, c1, rej, con

    write(*, '(/,A)') repeat('=', 60)
    write(*, '(A)') trim(msg('sum_title'))
    if (sc_run) then
      write(*, '(2X,A,1X,I0,1X,A,1X,I0,1X,A)') trim(msg('sc_result')), np_, &
          trim(msg('sc_passed')), nf_, trim(msg('sc_failed'))
    end if
    if (r1) then
      if (c1) then
        write(*, '(2X,A,1X,I0,A,1X,A)') trim(msg('sum_obj')), 1, ':', &
            trim(msg('s_pass'))
      else
        write(*, '(2X,A,1X,I0,A,1X,A)') trim(msg('sum_obj')), 1, ':', &
            trim(msg('s_warn'))
      end if
    end if
    if (r2_) then
      if (.not. rej) then
        write(*, '(2X,A,1X,I0,A,1X,A)') trim(msg('sum_obj')), 2, ':', &
            trim(msg('s_pass'))
      else
        write(*, '(2X,A,1X,I0,A,1X,A)') trim(msg('sum_obj')), 2, ':', &
            trim(msg('s_fail'))
      end if
    end if
    if (r3) then
      if (con) then
        write(*, '(2X,A,1X,I0,A,1X,A)') trim(msg('sum_obj')), 3, ':', &
            trim(msg('s_pass'))
      else
        write(*, '(2X,A,1X,I0,A,1X,A)') trim(msg('sum_obj')), 3, ':', &
            trim(msg('s_fail'))
      end if
    end if
    write(*, '(A)') repeat('=', 60)
  end subroutine print_summary

end program ab_cloud_verify
