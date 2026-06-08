
def extract_title(markdown):
    if not markdown.strip().startswith('# '):
        raise Exception(f"missing h1 header for {markdown}")
    return ((markdown.strip())[2:]).split("\n", 1)[0] #first line of h1 header, \n removed, '# ' removed.
