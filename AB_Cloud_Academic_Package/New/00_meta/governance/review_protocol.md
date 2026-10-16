# Review protocol (honesty-first)

1. **Numbers pass.** Any PR touching numbers must cite the source verdict file
   (path + key) in the PR body. Re-typed numbers are rejected on sight.
2. **Boundaries pass.** Any PR adding a claim must add its `does_not_prove`
   field. Any PR *removing* one is rejected without discussion (LICENSE §3).
3. **Registry is the funnel.** Display artefacts (monograph, report, web lab,
   CLI output) must derive from `research_registry.json`, not from local
   copies of numbers.
4. **Two eyes on translations.** A language abstract may be merged once a
   second speaker of that language has read it (the author reads RU/EN).
5. **Tests green.** `pytest 09_tests/python` is the merge gate.
6. **Negative results are not deletions.** A replicated failure of a claim is
   a *strengthening* of the record and merges as such.
