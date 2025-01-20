from typing import List
from textnode import TextType, TextNode


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
