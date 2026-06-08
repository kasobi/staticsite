from f_recursive_static_to_private import r_static_to_private
from f_recursive_generate_pages import r_generate_pages
import os
import shutil

static_dir = "static"
public_dir = "public"
content_dir = "content"

def main():

    if os.path.exists(public_dir):
         shutil.rmtree(public_dir)

    r_static_to_private(static_dir, public_dir)


    r_generate_pages(content_dir, 'template.html', public_dir)



if __name__ == "__main__":
   main()