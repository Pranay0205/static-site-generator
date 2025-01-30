import os
import shutil
from copy_static import copy_files_recursive
from textnode import TextNode
from textnode import TextType

dir_static = "./static"
dir_public = "./public"


def main():
    print("Deleting public directory...")

    if os.path.exists(dir_public):
        shutil.rmtree(dir_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_static, dir_public)


main()
