import unittest
from f_block_to_block_type import block_to_block_type, BlockType


class TestHTMLNode(unittest.TestCase):
    def test_block_to_blocktype_heading(self):
        md = "### This is a heading"
        type = block_to_block_type(md)
        self.assertEqual(type, BlockType.HEADING)

    def test_block_to_blocktype_code(self):
        md = "```\nThis is a codeblock\nline 2 of codeblock\nline 3 of codeblock```"
        type = block_to_block_type(md)
        self.assertEqual(type, BlockType.CODE)

    def test_block_to_blocktype_quote(self):
        md = ">this is a quote\n> to be or not to be."
        type = block_to_block_type(md)
        self.assertEqual(type, BlockType.QUOTE)

    def test_block_to_blocktype_unordered_list(self):
        md = "- list part 1\n- list part 2"
        type = block_to_block_type(md)
        self.assertEqual(type, BlockType.UNORDERED_LIST)

    def test_block_to_blocktype_ordered_list(self):
        md = "1. testing ordered list\n2. this is ordered\n3. last ordered list"
        type = block_to_block_type(md)
        self.assertEqual(type, BlockType.ORDERED_LIST)

    def test_block_to_blocktype_paragraph(self):
        md = ">basic paragraph\nthat contains everything\n``` to really try to\n1. trip it \n- up"
        type = block_to_block_type(md)
        self.assertEqual(type, BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()