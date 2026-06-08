import unittest
from f_text_to_html import text_node_to_html_node
from textnode import TextNode, TextType
from f_markdown_to_html_node import markdown_to_html_node
from f_extract_title import extract_title


class TestTextNode(unittest.TestCase):
#text node -> html node tests [text_node_to_html_node()]
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'i')
        self.assertEqual(html_node.to_html(), "<i>This is an italic node</i>")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'code')
        self.assertEqual(html_node.to_html(), "<code>This is a code node</code>")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, 'url.link.com')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.to_html(), '<a href="url.link.com">This is a link node</a>')

    def test_image(self):
        node = TextNode("This is an image node", TextType.IMAGE, 'url.link.com')
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.to_html(), '<img src="url.link.com" alt="This is an image node"></img>')

    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_extract_title(self):
        md = "\n# this is a h1 title"
        title = extract_title(md)
        self.assertEqual(title, "this is a h1 title")

    def test_extract_title_error(self):
        md = "\n## this isn't a h1 title"
        with self.assertRaises(Exception):
            extract_title(md)


if __name__ == "__main__":
    unittest.main()