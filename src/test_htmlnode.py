import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_init_none(self):
        node = HTMLNode()
        result = True if node.tag == None and node.value == None and node.children == None and node.props == None else False
        self.assertTrue(result)

    def test_args(self):
        node = HTMLNode('tag', 'value', 'children', {'propKey': 'propValue'})
        result = True if node.tag == 'tag' and node.value == 'value' and node.children == 'children' and node.props == {'propKey': 'propValue'} else False
        self.assertTrue(result)

    def test_props_to_html(self):
        node = HTMLNode(props={'key1': 'value1', 'key2': 'value2'})
        result = True if node.props_to_html() == ' key1="value1" key2="value2"' else False

#leaf node tests
    def test_leafNode_to_html_p(self):
        node = LeafNode('p', 'Hello, world!')
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leafNode_to_html_a(self):
        node = LeafNode('a', 'Click test link!', {'link': 'test.url.com'})
        self.assertEqual(node.to_html(), '<a link="test.url.com">Click test link!</a>')

    def test_leafNode_to_html_noVal(self):
        node = LeafNode('a', None)
        with self.assertRaises(ValueError):
            node.to_html()

#parent node tests
    def test_parentNode_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parentNode_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parentNode_to_html_tag_valueError(self):
        with self.assertRaises(ValueError):
            ParentNode(None, None).to_html()

    def test_parentNode_to_html_children_valueError(self):
        with self.assertRaises(ValueError):
            ParentNode('div', None).to_html()

    def test_parentNode_to_html_multiple_children(self):
        child1 = LeafNode('b','bold text')
        child2 = LeafNode('__', 'italics text')
        parent = ParentNode('p', [child1, child2])
        self.assertEqual(
            parent.to_html(),
            '<p><b>bold text</b><__>italics text</__></p>'
        )

    def test_parentNode_to_html_with_props(self):
        child = LeafNode('b','bold text')
        parent = ParentNode('p', [child], {'key': 'value'})
        self.assertEqual(
            parent.to_html(),
            '<p key="value"><b>bold text</b></p>'
        )

if __name__ == "__main__":
    unittest.main()