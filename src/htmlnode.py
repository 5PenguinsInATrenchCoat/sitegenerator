class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        output = ""
        if self.props == None:
            return ""
        for key, entry in self.props.items():
            output = output + f' {key}="{entry}"'
        return output
    
    def __repr__(self):
        return f"Tag: {self.tag} Value: {self.value} Children: {self.children} Props: {self.props}"
    
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props)
        self.children = []

    def to_html(self):
        if self.value is None:
            raise ValueError("Please enter a value")
        if self.tag is None:
            return self.value
        props_string = ""
        if self.props is not None:
            for key, value in self.props.items():
                props_string += f' {key}="{value}"'

        return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
    
    def add_child(self, child):
        raise Exception("LeafNode cannot have children!")
