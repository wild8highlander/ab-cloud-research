# dashboards/

Grafana / Superset / Metabase manifests are planned exports of the registry.
The live interactive surface today is the [web laboratory](../../07_web_lab/index.html)
(offline, no server needed). The registry JSON is directly loadable into any
of the three tools; `06_code/python/run.py analyze --out=out` produces a
flattened CSV for quick import.
