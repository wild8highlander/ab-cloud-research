function results = ab_cloud_verify_en(varargin)
%AB_CLOUD_VERIFY_EN English-pinned thin wrapper (CANON_SPEC §10).
%   All computation lives in ab_cloud_verify.m — a single canonical kernel
%   with the frozen golden anchors and no duplicated math (duplicated kernels
%   are how the old suite drifted apart). This wrapper only pins the output
%   language to English so that LANG/locale cannot change it.
%
%   Usage:
%     results = ab_cloud_verify_en();
%     results = ab_cloud_verify_en('zeros', 50000, 'objection', 'all');
%
%   Name/value parameters are identical to ab_cloud_verify; the pinned
%   language is appended last, so it always wins over the LANG environment.

    results = ab_cloud_verify(varargin{:}, 'lang', 'en');
end
