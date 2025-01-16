from textnode import TextNode
from textnode import TextType


def main():
    t1 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")

    print(t1)


main()
