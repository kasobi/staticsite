from f_extract_markdown import extract_markdown_links, extract_markdown_images
from textnode import TextNode, TextType
from enum import Enum

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue 
        image_list = extract_markdown_images(old_node.text)
        if not image_list:
            new_nodes.append(old_node)
            continue
        node_text = old_node.text
        for image in image_list:
            node_text = node_text.split(f"![{image[0]}]({image[1]})", 1)
            if node_text[0]:
                new_nodes.append(TextNode(node_text[0], TextType.TEXT))
            new_nodes.append(TextNode(f"{image[0]}", TextType.IMAGE, f"{image[1]}"))
            node_text = node_text[-1]
        if node_text:
            new_nodes.append(TextNode(node_text, TextType.TEXT))
            
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue 
        link_list = extract_markdown_links(old_node.text)
        if not link_list:
            new_nodes.append(old_node)
            continue
        node_text = old_node.text
        for link in link_list:
            node_text = node_text.split(f"[{link[0]}]({link[1]})", 1)
            if node_text[0]:
                new_nodes.append(TextNode(node_text[0], TextType.TEXT))
            new_nodes.append(TextNode(f"{link[0]}", TextType.LINK, f"{link[1]}"))
            node_text = node_text[-1]
        if node_text:
            new_nodes.append(TextNode(node_text, TextType.TEXT))
            
    return new_nodes
