import os
import shutil


def r_static_to_private(origin, destination):
    if os.path.isdir(origin):
        if not os.path.exists(destination):
            os.mkdir(destination)
            print(f"made directory: {destination}")
        for path in os.listdir(origin):
            r_static_to_private(os.path.join(origin, path), os.path.join(destination, path))
    elif os.path.isfile(origin):
        shutil.copy(origin, destination)
        print(f"copied file: {origin}")


    