from block_markdown import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node


def parse_heading(block):
    htmlnodes = []
    parent = None

    for line in block.split("\n"):
        textnodes = text_to_textnodes(line)
        for textnode in textnodes:
            if textnode.text.startswith("#"):
                level = textnode.text.count("#")
                textnode.text = textnode.text.strip("# ")
                parent = ParentNode(
                    f"h{level}", [text_node_to_html_node(textnode)])
                htmlnodes.append(parent)
            else:
                htmlnode = text_node_to_html_node(textnode)
                if parent:
                    parent.children.append(htmlnode)
                else:
                    htmlnodes.append(htmlnode)

    return [htmlnodes]


def parse_paragraph(block):
    textnodes = text_to_textnodes(block)
    for i, textnode in enumerate(textnodes):
        if i == 0:
            htmlnode = ParentNode("p", [text_node_to_html_node(textnode)])
        htmlnode.children.append(text_node_to_html_node(textnode))
    return [htmlnode]


def parse_unordered_list(block):
    li_nodes = []
    for line in block.split("\n"):
        textnodes = []
        if line.startswith("*") or line.startswith("-"):
            text = line.strip()[1:].strip()
            textnodes.extend(text_to_textnodes(text))

        li_children = ParentNode("li", [])

        for textnode in textnodes:
            htmlnode = text_node_to_html_node(textnode)
            li_children.children.append(htmlnode)

        li_nodes.append(li_children)

    return ParentNode("ul", [li_nodes])


def parse_ordered_list(block):
    pass


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    htmlnodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.heading:
            htmlnodes.extend(parse_heading(block))
        if block_type == BlockType.paragraph:
            htmlnodes.extend(parse_paragraph(block))
        if block_type == BlockType.unordered_list:
            print(parse_unordered_list(block))


markdown_to_html_node("""## This is a **heading**\n\n### This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* First is the first list **item** in a list block
* Second is a list item
* Third is another list item""")
