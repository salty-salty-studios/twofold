init -10 python:
    ## The session class.

    # Ren'Py session class for non-rollbackable per-playthrough storage.
    class Session(renpy.python.NoRollback):
        @classmethod
        def _setup(cls):
            store.session = cls()

    config.start_callbacks.append(Session._setup)
