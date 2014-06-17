## Get git version.
init python:
    def git_version():
        from os import path

        # Use stored git revision in e.g. builds.
        if hasattr(store, 'git_revision'):
            return store.git_revision

        # Query git directory.
        git_dir = path.join(config.gamedir, '..', '.git')
        if path.isdir(git_dir):
            # Query the current release HEAD.
            head = path.join(git_dir, 'HEAD')
            with open(head, 'r') as f:
                parts = f.read().strip().split()

            # Does it reference a different tag or branch?
            if parts[0] == 'ref:':
                ref = path.join(git_dir, parts[1])

                try:
                    with open(ref, 'r') as f:
                        rev = f.read().strip()
                except IOError:
                    return None
            else:
                rev = parts[0]

            # Return first 7 characters, should be unique enough.
            return rev[:7]

        return None
