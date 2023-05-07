user_prompt = "Enter a todo: "

todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input(user_prompt)
            todos.append(todo)
        case "show":
            for item in todos:
                print(item)
        case "edit":
            editItem = input("which item do you want to edit?")
            editItem = editItem.strip()
            if editItem in todos:
                editIndex = todos.index(editItem)
                todos[editIndex] = input("update " + editItem + " to be: ")
        case "exit":
            break
        case _:
            print("That's not a valid command")

print("Bye!")
