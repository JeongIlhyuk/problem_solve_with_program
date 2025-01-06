linked_list = {
    "First":{"next":"Tom"},
    "Tom":{"next":"Kim"},
    "Kim":{"next":"Rose"},
    "Rose":{"next":None}
}

def search_node(node):
    return node in linked_list
            
def add_node(target_node, new_node):
    if target_node not in linked_list:
        print("There is no this node")
        return
    old_next = linked_list[target_node]["next"]
    linked_list[target_node]["next"] = new_node

    linked_list[new_node] = {"next":old_next}

def delete_node(node):
    if node not in linked_list:
        print("There is no this node")
        return

    old_next = linked_list[node]["next"]
    linked_list.pop(node)
    key = "First"
    while True:
        if linked_list[key]["next"] == node:
            linked_list[key]["next"] = old_next
            print("Delete completed")
            return
        else:
            key = linked_list[key]["next"]

#add_node("Kim","Park")
#delete_node("Kim")
#print(linked_list)

def home():
    while True:
        print("1. Search Node")
        print("2. Add Node")
        print("3. Delete Node")
        print("4. Exit")
        menu = int(input("Select a menu number:"))
        if menu == 1:
            search_node()
        elif menu == 

while True:
    node = input("Type a node to search(0 to exit):")
    if node == "0":
        print("Exiting")
        break
    if search_node(node):
        print("Found the node")
    else:
        print("Can't find the node")
