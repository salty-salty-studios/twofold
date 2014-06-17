init -1 python:
    ## Functions for trivial I/O inspection in Ren'Py as a replacement for the ones in os.path.
    all_files = renpy.list_files()

    def renpy_isdir(path):
        return any(x for x in all_files if x.startswith(path + '/'))

    def renpy_isfile(path):
        return path in all_files

    def renpy_exists(path):
        return renpy_isfile(path) or renpy_isdir(path)

    def renpy_join(*args):
        return '/'.join(args)

    def renpy_listdir(path, full_path=False, recursive=False):
        results = set()

        for file in all_files:
            if file.startswith(path + '/'):
                if not recursive:
                    entry = file.replace(path + '/', '', 1)
                    entry = entry.split('/', 1)[0]
                else:
                    entry = file

                if full_path:
                    results.add(path + '/' + entry)
                else:
                    results.add(entry)

        return results
