from f_recursive_static_to_private import r_static_to_private
from f_recursive_generate_pages import r_generate_pages
import os
import shutil
import sys

basepath = "/"

if len(sys.argv) > 1:
    basepath = sys.argv[1]

static_dir = "static"
public_dir = "docs"
content_dir = "content"


def main():
    print(f"sys.argv is = {sys.argv}")
    print(f"basepath = {basepath}")
    if os.path.exists(public_dir):
         shutil.rmtree(public_dir)

    r_static_to_private(static_dir, public_dir)


    r_generate_pages(basepath, content_dir, 'template.html', public_dir)



if __name__ == "__main__":
   main()