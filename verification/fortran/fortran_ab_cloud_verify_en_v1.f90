!===============================================================================
! AB-CLOUD VERIFICATION SUITE — THIN ENGLISH WRAPPER (CANON_SPEC §10)
!===============================================================================
! This file contains NO math and NO message text.  It only pins the report
! language at compile time and pulls in the single Fortran source of truth:
!
!   #define FORCE_LANG_EN  ->  the included program ignores --lang / $LANG
!                             and prints the EN catalog.
!
! Build (the preprocessor is REQUIRED — gfortran runs cpp with -cpp):
!   gfortran -cpp -O2 -o ab_cloud_verify_en ab_cloud_verify_en.f90
!
! The binary produced here is byte-for-byte the same program as
! ab_cloud_verify.f90 compiled directly; only the language pin differs.
! Duplicated kernels are how the old suite drifted apart — do not copy math
! back into this file.
!===============================================================================

#define FORCE_LANG_EN
#include "ab_cloud_verify.f90"
