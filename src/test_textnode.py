import unittest
from f_text_to_html import text_node_to_html_node
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode('This is a text node', TextType.BOLD)
        node2 = TextNode('This is a text node', TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode('link set None vs default None', TextType.LINK, None)
        node2 = TextNode('link set None vs default None', TextType.LINK)
        self.assertEqual(node, node2)

    def test_type_diff(self):
        node = TextNode('testing different types', TextType.LINK)
        node2 = TextNode('testing different types', TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_diff_text(self):
        node = TextNode('Text 1', TextType.TEXT)
        node2 = TextNode('Text 2', TextType.TEXT)
        self.assertNotEqual(node, node2)
        
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")



if __name__ == "__main__":
    unittest.main()
    