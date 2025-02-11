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
            if textnode.text == "":
                continue
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

    return htmlnodes


def parse_paragraph(block):
    htmlnode = None
    textnodes = text_to_textnodes(block)
    for i, textnode in enumerate(textnodes):
        if i == 0:
            htmlnode = ParentNode("p", [text_node_to_html_node(textnode)])
            continue
        htmlnode.children.append(text_node_to_html_node(textnode))
    return [htmlnode]


def parse_unordered_list(block):
    li_nodes = []
    for line in block.split("\n"):
        textnodes = []
        if line.startswith("* ") or line.startswith("-"):
            text = line.strip()[1:].strip()
            textnodes.extend(text_to_textnodes(text))

        li_children = ParentNode("li", [])

        for textnode in textnodes:
            htmlnode = text_node_to_html_node(textnode)
            li_children.children.append(htmlnode)

        li_nodes.append(li_children)

    return [ParentNode("ul", li_nodes)]


def parse_ordered_list(block):
    li_nodes = []

    for line in block.split("\n"):
        line = line.strip()
        if not line or not line[0].isdigit():
            continue  # Skip empty lines or non-numbered lines

        # Extract text after number
        text = line.split(" ", 1)[1] if " " in line else ""
        textnodes = text_to_textnodes(text)  # Convert text to text nodes

        li_nodes.append(ParentNode(
            "li", [text_node_to_html_node(tn) for tn in textnodes]))

    return [ParentNode("ol", li_nodes)]  # Wrap all <li> elements inside <ol>


def parse_blockquote(block):
    textnodes = text_to_textnodes(block)
    for i, textnode in enumerate(textnodes):
        if i == 0:
            textnode.text = textnode.text[2:].strip()
            htmlnode = ParentNode(
                "blockquote", [text_node_to_html_node(textnode)])
            continue
        htmlnode.children.append(text_node_to_html_node(textnode))

    return [htmlnode]


def parse_codeblock(block):
    text = block[4:-4]
    textnodes = text_to_textnodes(text)
    htmlnode = ParentNode("code", [])
    for textnode in textnodes:
        htmlnode.children.append(text_node_to_html_node(textnode))

    return [ParentNode("pre", [htmlnode])]


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
            htmlnodes.extend(parse_unordered_list(block))
        if block_type == BlockType.ordered_list:
            htmlnodes.extend(parse_ordered_list(block))
        if block_type == BlockType.blockquote:
            htmlnodes.extend(parse_blockquote(block))
        if block_type == BlockType.code:
            htmlnodes.extend(parse_codeblock(block))
        else:
            ValueError("Unrecognizable markdown")

    return ParentNode("div", htmlnodes)
