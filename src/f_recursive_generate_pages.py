from f_markdown_to_html_node import markdown_to_html_node
from f_extract_title import extract_title
from f_recursive_static_to_private import r_static_to_private
import os


def r_generate_pages(from_path, template_path, dest_path):
    if os.path.isdir(from_path):
        if not os.path.exists(dest_path):
            os.mkdir(dest_path)
            print(f"made directory: {dest_path}")
        for path in os.listdir(from_path):
            r_generate_pages(os.path.join(from_path, path), template_path, os.path.join(dest_path, path))
            
    else:
        print(f"Generating page from {from_path} to {dest_path} using {template_path}")
        with open(from_path) as from_file:
            origin_content = from_file.read()
        with open(template_path) as template_file:
            template_content = template_file.read()
        
        html_from_origin = markdown_to_html_node(origin_content).to_html()

        title = extract_title(origin_content)

        new_page = template_content.replace("{{ Title }}", title)
        new_page = new_page.replace("{{ Content }}", html_from_origin)

        dest_path = os.path.splitext(dest_path)[0] + ".html"
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        with open(dest_path, 'w') as dest_file:
            dest_file.write(new_page)

    