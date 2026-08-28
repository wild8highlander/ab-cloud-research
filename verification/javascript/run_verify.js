#!/usr/bin/env node
// ==============================================================================
// AB-Cloud Verification Suite — JavaScript/Node.js Runner Script
// ==============================================================================
// Usage:
//   node run_verify.js [options]
//   Options:
//     --zeros N         Number of zeros to use (0 = all)
//     --source NAME     Data source: auto|zeta_zeros_50000|zeta_zeros_500k|
//                         zeta_zeros_2M|zeta_zeros_highT|zeros6|zeta_zeros_50000_csv
//     --objection 1|2|3|all   Which objection to verify
//     --lang en|ru      Output language
//     --data-dir DIR    Data directory (default: ../data)
//     --help            Show this help
// ==============================================================================

'use strict';

const path = require('path');

// --- Parse command-line arguments --------------------------------------------

function parseArgs(argv) {
  const opts = {
    zeros:     0,
    source:    'auto',
    objection: 'all',
    lang:      'en',
    dataDir:   '../data',
  };

  const args = argv.slice(2); // strip node and script name
  let i = 0;
  while (i < args.length) {
    const flag = args[i];
    switch (flag) {
      case '--zeros':
        opts.zeros = parseInt(args[++i], 10); i++; break;
      case '--source':
        opts.source = args[++i]; i++; break;
      case '--objection':
        opts.objection = args[++i]; i++; break;
      case '--lang':
        opts.lang = args[++i]; i++; break;
      case '--data-dir':
        opts.dataDir = args[++i]; i++; break;
      case '--help':
        printHelp(); process.exit(0);
      default:
        console.error(`Unknown option: ${flag}`);
        process.exit(1);
    }
  }
  return opts;
}

function printHelp() {
  console.log(`
AB-Cloud Verification Suite — JavaScript/Node.js Runner

Usage: node run_verify.js [options]

Options:
  --zeros N           Number of zeros to use (0 = all)
  --source NAME       Data source (auto, zeta_zeros_50000, zeta_zeros_500k,
                        zeta_zeros_2M, zeta_zeros_highT, zeros6,
                        zeta_zeros_50000_csv)
  --objection 1|2|3|all   Which objection(s) to verify
  --lang en|ru        Output language
  --data-dir DIR      Path to data directory (default: ../data)
  --help              Show this help message

Examples:
  node run_verify.js --zeros 50000 --objection 1 --lang en
  node run_verify.js --source zeta_zeros_500k --objection all --lang ru
  node run_verify.js --data-dir /path/to/data --zeros 100000
`);
}

// --- Main --------------------------------------------------------------------

async function main() {
  const opts = parseArgs(process.argv);

  // Resolve the main module relative to this script's directory
  const scriptDir = __dirname;
  const mainModule = path.join(scriptDir, 'ab_cloud_verify.js');

  let abCloudVerify;
  try {
    const mod = require(mainModule);
    abCloudVerify = mod.abCloudVerify;
  } catch (err) {
    console.error(`ERROR: Cannot load ab_cloud_verify.js from: ${scriptDir}`);
    console.error(err.message);
    process.exit(1);
  }

  // Display configuration
  console.log('AB-Cloud JavaScript/Node.js Runner');
  console.log(`  Data dir:    ${path.resolve(opts.dataDir)}`);
  console.log(`  Zeros:       ${opts.zeros > 0 ? opts.zeros : 'all'}`);
  console.log(`  Source:      ${opts.source}`);
  console.log(`  Objection:   ${opts.objection}`);
  console.log(`  Language:    ${opts.lang}`);
  console.log('');

  // Run verification
  try {
    const results = await abCloudVerify({
      dataDir:   opts.dataDir,
      zeros:     opts.zeros,
      source:    opts.source,
      objection: opts.objection,
      lang:      opts.lang,
    });

    if (results === null) {
      console.error('Verification FAILED — no results returned.');
      process.exit(1);
    } else {
      process.exit(0);
    }
  } catch (err) {
    console.error('Verification ERROR:', err.message);
    process.exit(1);
  }
}

main();
