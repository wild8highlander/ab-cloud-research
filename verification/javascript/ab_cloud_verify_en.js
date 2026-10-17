'use strict';
// Thin language pin (CANON_SPEC §10): English output. No duplicated math.
// Usage: node ab_cloud_verify_en.js [--zeros N] [--source S] [--objection X] [--data-dir D]
process.argv.push('--lang', 'en');
const v = require('./ab_cloud_verify.js');
v.main();
