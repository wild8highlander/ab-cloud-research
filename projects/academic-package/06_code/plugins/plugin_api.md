# Plugin API

A plugin is a Python module in `plugins/` exposing:

```python
def register(app, ctx):
    @app.command()
    def my_command():
        ...
```

- `app` — the typer application (add commands freely).
- `ctx` — the shared context (lang, theme, seed, config path).

## The honesty gate

Registration fails if the plugin's source tries to set `rh_status` to
anything but `"certified"` or to strip `does_not_prove` fields (checked by
`09_tests/python/test_contract.py::test_plugin_honesty`).
