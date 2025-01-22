from typing import List
from textnode import TextType, TextNode
import re


def split_nodes_delimiter(old_nodes: List[TextNode], delimiter: str, text_type: TextType):
    result = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue

        splitted_nodes = []
        textnode_sections = old_node.text.split(delimiter)
        if len(textnode_sections) % 2 == 0:
            raise ValueError("Something wrong with the text formatting")

        for i in range(len(textnode_sections)):
            if textnode_sections[i] == "":
                continue
            if i % 2 == 0:
                splitted_nodes.append(
                    TextNode(textnode_sections[i], TextType.TEXT))
            else:
                splitted_nodes.append(
                    TextNode(textnode_sections[i], text_type))

        result.extend(splitted_nodes)

    return result


def extract_markdown_images(text: str):
    regex = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex, text)
    return matches


def extract_markdown_links(text: str):
    regex = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(regex, text)
    return matches


text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
extract_markdown_images(text)

text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
x = extract_markdown_links(text)
