import os
import shutil
from copy_static import copy_files_recursive
from markdown_parser import markdown_to_html_node
from textnode import TextNode
from textnode import TextType
from title_extractor import extract_title

dir_static = "./static"
dir_public = "./public"
markdown_file = "./content/index.md"
template_file = "./template.html"
index_html_file = "index.html"


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {
          dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_file, "r") as f:
        template = f.read()

    html_nodes = markdown_to_html_node(markdown)

    html = html_nodes.to_html()

    title = extract_title(markdown)

    with open(template_file, "r") as f:
        template_html = f.read()

    replacements = {"Title": title, "Content": html}

    for key, value in replacements.items():
        template_html = template_html.replace("{{ " + key + " }}", value)

    with open(dest_path, "w") as f:
        # Ensure directory exists
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

        f.write(template_html)


def main():
    print("Deleting public directory...")

    if os.path.exists(dir_public):
        shutil.rmtree(dir_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_static, dir_public)

    generate_page(markdown_file, template_file,
                  os.path.join(dir_public, index_html_file))


main()
