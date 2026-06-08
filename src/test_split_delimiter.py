import unittest
from enum import Enum
from textnode import TextNode, TextType
from f_split_delimiter import split_nodes_delimiter

class TestTextNode(unittest.TestCase):
    def test_split_basic(self):
        old_node = TextNode("Testing the **bolding** return", TextType.TEXT)
        new_nodes = split_nodes_delimiter([old_node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)

    def test_missing_split(self):
        old_node = TextNode("Testing the **bolding return", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([old_node], "**", TextType.BOLD)

    def test_split_notText(self):
        old_node = TextNode("boldText", TextType.BOLD)
        new_nodes = split_nodes_delimiter([old_node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text_type, TextType.BOLD)

if __name__ == "__main__":
    unittest.main()