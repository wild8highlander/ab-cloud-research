"""Example plugin for the AB-Cloud unified CLI.

Plugins are plain Python modules with a `register(app, ctx)` function.
The review protocol applies: a plugin that weakens the honesty layer
(rh_status must stay 'blocked'; does_not_prove fields are inviolable)
is rejected at registration.
"""

def register(app, ctx):
    @app.command()
    def hello():
        "Example plugin command."
        print("hello from the example plugin - the wall is at locality")
