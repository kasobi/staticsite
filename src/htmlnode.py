

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag #str for the html tag name ( p, a, h1, etc.)
        self.value = value #content, link, etc.
        self.children = children #list of HTMLNodes that are children of this node
        self.props = props #dictionary k-v pairs of the attributes of HTML tag {"href": "https://www.google.com"}

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ''
        props_string = ''
        for i in self.props:
            props_string += f' {i}="{self.props[i]}"'
        return str(props_string)
    
    def __repr__(self):
        return f'HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})'
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError('leaf node requires value')
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f'LeafNode(tag: {self.tag}, value: {self.value}, props: {self.props})'


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError('parent node requires tag')
        if self.children is None:
            raise ValueError('parent node requires children')
        html_string = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            html_string += child.to_html()
        html_string += f'</{self.tag}>'
        return html_string
    
