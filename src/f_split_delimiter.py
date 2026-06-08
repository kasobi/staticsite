from enum import Enum
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = old_node.text.split(delimiter)
        #if len() even, missing delimiter '**bold text' -> ('','bold text' )
        if len(split_nodes) % 2 == 0:
            raise Exception(f'missing delimiter! missing a "{delimiter}" in {old_node}')
        for i, text in enumerate(split_nodes):
            if not text:
                continue
            if i % 2 == 0:
                node = TextNode(text, TextType.TEXT)
            else:
                node = TextNode(text, text_type)
            new_nodes.append(node)
    
    return new_nodes


        
            
        
            




                


