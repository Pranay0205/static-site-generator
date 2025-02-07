import os
import shutil
from copy_static import copy_files_recursive
from markdown_parser import markdown_to_html_node
from textnode import TextNode
from textnode import TextType
from title_extractor import extract_title

dir_static = "./static"
dir_public = "./public"
source_folder = "./content"
template_file = "./template.html"


def generate_page_recursively(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {
          dest_path} using {template_path}")

    # Create destination directory if it doesn't exist
    os.makedirs(dest_path, exist_ok=True)

    # Read template file content once
    with open(template_path, "r") as f:
        html_template = f.read()

    items = os.listdir(from_path)

    for item in items:
        source_path = os.path.join(from_path, item)

        if os.path.isfile(source_path):
            # Only process markdown files
            if item.endswith('.md'):
                # Create destination path for HTML file
                dest_file = os.path.join(
                    dest_path, item.replace(".md", ".html"))

                # Read and process markdown file
                with open(source_path, "r") as f:
                    markdown = f.read()

                # Extract title and convert markdown to HTML
                title = extract_title(markdown)
                html_nodes = markdown_to_html_node(markdown)
                html_content = html_nodes.to_html()

                # Create new HTML content from template
                final_html = html_template.replace("{{ Title }}", title)
                final_html = final_html.replace("{{ Content }}", html_content)

                # Write the final HTML file
                with open(dest_file, "w") as f:
                    f.write(final_html)

        elif os.path.isdir(source_path):
            # Create corresponding destination directory path
            new_dest_path = os.path.join(dest_path, item)

            # Recursively process subdirectory
            generate_page_recursively(
                source_path, template_path, new_dest_path)


def main():
    print("Deleting public directory...")

    if os.path.exists(dir_public):
        shutil.rmtree(dir_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_static, dir_public)

    generate_page_recursively("./content", template_file, dir_public)


main()
