class TreeNode:
    def __init__(self, data, yes_link=None, no_link=None):
        self.data = data
        self.yes_link = yes_link
        self.no_link = no_link

def build_binary_tree(data_file):
    root = None
    nodes = {}
    
    with open(data_file, "r") as file:
        title = file.readline().strip()
        help_info = file.readline().strip()
        
        for line in file:
            parts = line.strip().split()
            node_num = int(parts[0])
            question_or_answer = " ".join(parts[1:])
            
            node = TreeNode(question_or_answer)
            nodes[node_num] = node

            if node_num == 1:
                root = node
            else:
                parent_num = node_num // 2
                parent_node = nodes[parent_num]
                if node_num % 2 == 0:
                    parent_node.no_link = node
                else:
                    parent_node.yes_link = node
    
    return title, help_info, root

def play_game(root):
    current_node = root
    while True:
        print(current_node.data)
        if current_node.yes_link is None and current_node.no_link is None:
            print("The answer is found.")
            break
        answer = input("Your choice (Y/N): ").strip().lower()
        while answer not in ["y", "yes", "n", "no"]:
            answer = input("Please enter a valid choice (Y/N): ").strip().lower()
        if answer in ["y", "yes"]:
            current_node = current_node.yes_link
        else:
            current_node = current_node.no_link

def display_tree(root):
    while True:
        print("What order do you want to display?")
        print("1. Inorder")
        print("2. Preorder")
        print("3. Postorder")
        print("4. Return to main menu")
        choice = input("Your choice: ").strip()
        
        if choice == "1":
            print("Inorder Traversal:")
            inorder_traversal(root)
        elif choice == "2":
            print("Preorder Traversal:")
            preorder_traversal(root)
        elif choice == "3":
            print("Postorder Traversal:")
            postorder_traversal(root)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def inorder_traversal(node):
    if node is not None:
        inorder_traversal(node.yes_link)
        print(node.data)
        inorder_traversal(node.no_link)

def preorder_traversal(node):
    if node is not None:
        print(node.data)
        preorder_traversal(node.yes_link)
        preorder_traversal(node.no_link)

def postorder_traversal(node):
    if node is not None:
        postorder_traversal(node.yes_link)
        postorder_traversal(node.no_link)
        print(node.data)

if __name__ == "__main__":
    game_file = "game1.txt"
    title, help_info, root = build_binary_tree(game_file)

    while True:
        print(title)
        print("P: Play the game")
        print("L: Load another game file")
        print("D: Display the binary tree")
        print("H: Help information")
        print("X: Exit the program")

        choice = input("Your choice: ").strip().lower()

        if choice == "p":
            play_game(root)
        elif choice == "l":
            new_game_file = input("Enter the name of the new game file: ")
            title, help_info, root = build_binary_tree(new_game_file)
        elif choice == "d":
            display_tree(root)
        elif choice == "h":
            print(help_info)
        elif choice == "x":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
