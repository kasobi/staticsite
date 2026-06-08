from f_split_delimiter import split_nodes_delimiter
from f_split_nodes import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


def text_to_textnodes(text):
    nodes_list = [TextNode(text, TextType.TEXT)]
    nodes_list = split_nodes_delimiter(nodes_list, "**", TextType.BOLD)
    nodes_list = split_nodes_delimiter(nodes_list, "_", TextType.ITALIC)
    nodes_list = split_nodes_delimiter(nodes_list, "`", TextType.CODE)
    nodes_list = split_nodes_image(nodes_list)
    nodes_list = split_nodes_link(nodes_list)

    return nodes_list

