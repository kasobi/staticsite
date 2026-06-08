from f_markdown_to_blocks import markdown_to_blocks
from f_block_to_block_type import block_to_block_type, BlockType
from f_text_to_textnodes import text_to_textnodes
from f_text_to_html import text_node_to_html_node
from htmlnode import *
from textnode import *


#Takes full markdown doc and returns single HTML Parent node
def markdown_to_html_node(markdown):
    block_list = markdown_to_blocks(markdown)
    all_nodes = []
    for block in block_list:
        all_nodes.append(block_to_html(block))
    return ParentNode("div", all_nodes)
         

def text_to_children(text):
    nodes_list = text_to_textnodes(text)
    html_nodes_list = []
    for node in nodes_list:
        html_nodes_list.append(text_node_to_html_node(node))
    return html_nodes_list


def block_to_html(block):
    type = block_to_block_type(block)
    children = []
    if type == BlockType.PARAGRAPH:
        lines = block.split("\n")
        children.extend(text_to_children(" ".join([line.strip() for line in lines])))
        parent = ParentNode("p", children)
        return parent
    
    if type == BlockType.HEADING:
        heading_val, heading_text = block.split(" ", 1)
        children.extend(text_to_children(heading_text.replace("\n", " ")))
        parent = ParentNode(f"h{len(heading_val)}", children)
        return parent
    
    if type == BlockType.QUOTE:
        children.extend(text_to_children((block[1:].strip()).replace("\n>", " ")))
        parent = ParentNode("blockquote", children)
        return parent

    if type == BlockType.UNORDERED_LIST:
        list_items = (block[2:].strip()).split("\n- ")
        list_item_parent = []
        for item in list_items:
            list_items_children = []
            list_items_children.extend(text_to_children(item))
            list_item_parent.append(ParentNode("li", list_items_children))

        list_parent = ParentNode("ul", list_item_parent)
        return list_parent

    if type == BlockType.ORDERED_LIST:
        list_items = block.split("\n")
        list_item_parent = []
        for item in list_items:
            list_items_children = []
            list_items_children.extend(text_to_children(item.split(". ", 1)[1]))
            list_item_parent.append(ParentNode("li", list_items_children))

        list_parent = ParentNode("ol", list_item_parent)
        return list_parent
    
    if type == BlockType.CODE:
        return ParentNode("pre", [ParentNode("code",[text_node_to_html_node(TextNode(block[3:-3].lstrip(), TextType.TEXT))])])



