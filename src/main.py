from textnode import TextType, TextNode



def main():
    my_node = TextNode("Hello world!", TextType.italic, "www.google.com")
    print(my_node)

if __name__ == "__main__":
    main()