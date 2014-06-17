init -1 python:
    ## Helper function to automatically define images from a folder.
    import re

    # Load all images from a certain directory.
    def define_images(dir, base_name=None, **transforms):
        # Image extension regexp.
        IMAGE_REGEXP = '\.(jpe?g|png|gif|bmp)$'

        if not base_name:
            base_name = []

        for entry in renpy_listdir(dir):
            name = base_name + entry.split('_')
            path_ = renpy_join(dir, entry)

            if renpy_isdir(path_):
                define_images(path_, name, **transforms)
            elif re.search(IMAGE_REGEXP, path_):
                # Remove extension.
                id = re.sub(IMAGE_REGEXP, '', ' '.join(name))
                nid = name[0].rsplit('.', 2)[0]

                # Check sprite offset.
                if nid in sprite_offsets.keys():
                    renpy.image(id, Transform(path_, yoffset=sprite_offsets[nid], **transforms))
                elif transforms:
                    renpy.image(id, Transform(path_, **transforms))
                else:
                    renpy.image(id, path_)
