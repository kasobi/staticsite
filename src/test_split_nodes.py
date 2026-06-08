import unittest
from textnode import TextNode, TextType
from enum import Enum
from f_split_nodes import split_nodes_image, split_nodes_link


class TestHTMLNode(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
            node = TextNode(
                "This is text with an [link](https://linking.com/linkylinklynk) and another [second link](https://link.li.ink/gobblygook)",
                TextType.TEXT,
            )
            new_nodes = split_nodes_link([node])
            self.assertListEqual(
                [
                    TextNode("This is text with an ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://linking.com/linkylinklynk"),
                    TextNode(" and another ", TextType.TEXT),
                    TextNode(
                        "second link", TextType.LINK, "https://link.li.ink/gobblygook"
                    ),
                ],
                new_nodes,
            )

    def test_split_links_with_images(self):
            node = TextNode(
                "This is text with an [link](https://linking.com/linkylinklynk) and another ![second image](https://i.imgur.com/3elNhQu.png)",
                TextType.TEXT,
            )
            new_nodes = split_nodes_link([node])
            self.assertListEqual(
                [
                    TextNode("This is text with an ", TextType.TEXT),
                    TextNode("link", TextType.LINK, "https://linking.com/linkylinklynk"),
                    TextNode(" and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT)
                ],
                new_nodes,
            )

    def test_split_image_with_links(self):
            node = TextNode(
                "This is text with an ![second image](https://i.imgur.com/3elNhQu.png) and another [link](https://linking.com/linkylinklynk)",
                TextType.TEXT,
            )
            new_nodes = split_nodes_image([node])
            self.assertListEqual(
                [
                    TextNode("This is text with an ", TextType.TEXT),
                    TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
                    TextNode(" and another [link](https://linking.com/linkylinklynk)", TextType.TEXT)
                ],
                new_nodes,
            )


if __name__ == "__main__":
    unittest.main()