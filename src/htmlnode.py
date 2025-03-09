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
        super().__init__(tag, value, None, props)
        self.children = []

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode value cannot be None")
        if self.tag is None:
            return self.value
        props_string = self.props_to_html()
        #if self.props:
        #    for key, value in self.props.items():
        #        props_string += f' {key}="{value}"'

        return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
    
    def add_child(self, child):
        raise Exception("LeafNode cannot have children!")
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        #props is the only optional field
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent Node must have a tag")
        if self.children is None:
            raise ValueError("Parent Node must have children")
        #Check for tag and children, raise error if either are empty

        props_string = ""
        if self.props is not None:
            for key, value in self.props.items():
                props_string += f' {key}="{value}"'
            #Copy of the props_string from before, stores the same thing

        full_string = f"<{self.tag}{props_string}>"
        #begin the string to return at the end

        for child in self.children:
            full_string = full_string + child.to_html()
            #iterate over each child, adding each to the full_string to return at the end

        full_string += f"</{self.tag}>"
        #adds the closing tag

        return full_string
