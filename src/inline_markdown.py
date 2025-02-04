from typing import List
from textnode import TextType, TextNode
import re


"""
    Split nodes based on delimiter and convert delimited text to specified type.
    >>> node = TextNode("This is text with a **bolded** word", TextType.TEXT)
    >>> split_nodes_delimiter([node], "**", TextType.BOLD)
    [TextNode("This is text with a ", TextType.TEXT), TextNode("bolded", TextType.BOLD), TextNode(" word", TextType.TEXT)] 
"""


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


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    if text == "":
        raise ValueError("Text cannot be empty")

    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    return nodes
