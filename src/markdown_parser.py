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
        if line.startswith("*") or line.startswith("-"):
            text = line.strip()[1:].strip()
            textnodes.extend(text_to_textnodes(text))

        li_children = ParentNode("li", [])

        for textnode in textnodes:
            htmlnode = text_node_to_html_node(textnode)
            li_children.children.append(htmlnode)

        li_nodes.append(li_children)

    return [ParentNode("ul", [li_nodes])]


def parse_ordered_list(block):
    textnodes = []
    for line in block.split("\n"):
        if line[0].isdigit():
            text = line.strip()[2:].strip()
            textnodes.extend(text_to_textnodes(text))

    li_children = ParentNode("li", [])

    for textnode in textnodes:
        htmlnode = text_node_to_html_node(textnode)
        li_children.children.append(htmlnode)

    return [ParentNode("ol", [li_children])]


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
    textnodes = text_to_textnodes(block)
    for i, textnode in enumerate(textnodes):
        if i == 0:
            htmlnode = ParentNode("code", [text_node_to_html_node(textnode)])
            continue
        htmlnode.children.append(text_node_to_html_node(textnode))
    print(htmlnode)

    return [htmlnode]


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

    print(HTMLNode("div", htmlnodes))
    return HTMLNode("div", htmlnodes)


markdown_to_html_node(
    """# Heading Parsing\n\n## Another Heading Passing\n\n1. one\n2. two\n3. three\n\n* ONE\n*TWO\n\n\n```print("Hello, World!");\nprint("Hello, World!");```""")
