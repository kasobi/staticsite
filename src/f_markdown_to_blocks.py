

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_list = []
    for block in blocks:
        temp_block = block.strip()
        if not temp_block:
            continue
        cleaned_list.append(temp_block)
    return cleaned_list
