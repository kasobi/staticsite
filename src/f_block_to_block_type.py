from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(markdown_block):
    if markdown_block.startswith(("# ","## ","### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if markdown_block.startswith("```\n") and markdown_block.endswith("```"):
        return BlockType.CODE
    if markdown_block.startswith(">"):
        if "\n" in markdown_block:
            block_lines = markdown_block.split("\n")
            for line in block_lines:
                if line.startswith(">"):
                    continue
                return BlockType.PARAGRAPH
            return BlockType.QUOTE
        else:
            return BlockType.QUOTE
    if markdown_block.startswith("- "):
        if "\n" in markdown_block:
            block_lines = markdown_block.split("\n")
            for line in block_lines:
                if line.startswith("- "):
                    continue
                return BlockType.PARAGRAPH
            return BlockType.UNORDERED_LIST
        else:
            return BlockType.UNORDERED_LIST
    if markdown_block.startswith("1. "):
        if "\n" in markdown_block:
            block_lines = markdown_block.split("\n")
            count = 0
            for line in block_lines:
                count += 1
                if line.startswith(f"{count}. "):
                    continue
                return BlockType.PARAGRAPH
            return BlockType.ORDERED_LIST
        else:
            return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH