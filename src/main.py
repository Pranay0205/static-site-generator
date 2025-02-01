import os
import shutil
from copy_static import copy_files_recursive
from markdown_parser import markdown_to_html_node
from textnode import TextNode
from textnode import TextType

dir_static = "./static"
dir_public = "./public"
markdown_file = "./content/index.md"
template_file = "./template.html"


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {
          dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_file, "r") as f:
        template = f.read()

    html = markdown_to_html_node(markdown)

    print(html.to_html())


generate_page(markdown_file, template_file, './something')


def main():
    print("Deleting public directory...")

    if os.path.exists(dir_public):
        shutil.rmtree(dir_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_static, dir_public)


# main()
