# FAIR principles checklist

**Findable**
- [x] DOI of record (10.5281/zenodo.21825394) in CITATION.cff, .zenodo.json, codemeta.json, datacite.xml
- [x] Descriptive metadata (title, author, ORCID, keywords) in 4 metadata formats
- [x] Machine-readable manifest (00_meta/manifest.json)

**Accessible**
- [x] All content retrievable from the public repository
- [x] Standard, open protocols (git, https)
- [x] Data in open formats (CSV, JSON, MD, SVG, PNG)

**Interoperable**
- [x] Schemas published (config.schema.json, 02_data/schemas/*.json)
- [x] RDF/OWL taxonomy (00_meta/taxonomy/ontology.ttl)
- [x] RO-Crate metadata (ro-crate-metadata.json)
- [x] Multilingual glossary aligned across RU/EN/ZH

**Reusable**
- [x] Clear component licences (MIT / CC BY 4.0 / ODbL + umbrella)
- [x] Provenance recorded (provenance.jsonl)
- [x] Reuse-ready CLI (6 languages, one contract)
- [x] Data dictionary + codebook + datacard
- [x] **Provenance of the honesty clause**: derivatives must preserve
  `does_not_prove` fields verbatim (see LICENSE §3)
