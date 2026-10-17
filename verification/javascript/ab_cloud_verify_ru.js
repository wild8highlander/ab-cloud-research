'use strict';
// Thin language pin (CANON_SPEC §10): Russian output. No duplicated math.
// Usage: node ab_cloud_verify_ru.js [--zeros N] [--source S] [--objection X] [--data-dir D]
process.argv.push('--lang', 'ru');
const v = require('./ab_cloud_verify.js');
v.main();
