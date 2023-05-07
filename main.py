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
            for index, item in enumerate(todos):
                index = index + 1
                formattedStr = f"{index}-{item}"
                print(formattedStr)
        case "edit":
            editItem = input("which item do you want to edit?")

            if int(editItem) <= len(todos):
                editItem = int(editItem) - 1
                todos[editItem] = input("update " + todos[editItem] + " to be: ")
            else:
                print("item doesnt exit")

        case "exit":
            break
        case _:
            print("That's not a valid command")

print("Bye!")
