class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplemented

    def props_to_html(self):
        output_string = ""

        if self.props == None:
            return output_string

        for key, value in self.props.items():
            output_string += f' {key}="{value}"'

        return output_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, children=None, props=None):
        if value == None:
            raise ValueError("All leaf nodes must have a value.")
        super().__init__(tag, value, children, props)

    def to_html(self):
        if self.tag == None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
