user_prompt = "Enter a todo: "
todo_file = 'todos.txt'


def read_todos():
    existing_file = open(todo_file, 'r')
    todo_list = existing_file.readlines()
    existing_file.close()
    return todo_list


def write_todos(todos_list):
    new_file = open(todo_file, 'w')
    new_file.writelines(todos_list)
    new_file.close()


def format_string(string):
    return string + '\n'


while True:
    user_action = input("Type add, show, edit. complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = format_string(input(user_prompt))

            todos = read_todos()

            todos.append(todo)

            write_todos(todos)
        case "show":
            todos = read_todos()

            for index, item in enumerate(todos):
                index = index + 1
                formattedStr = f"{index}-{item}"
                print(formattedStr)

        case "edit":
            editItem = int(input("which item do you want to edit?"))
            todos = read_todos()

            if editItem <= len(todos):
                editItem = editItem - 1
                todos[editItem] = format_string(input("update " + todos[editItem] + " to be: "))
                write_todos(todos)
            else:
                print("item doesnt exit")

        case "complete":
            todos = read_todos()
            completedItem = int(input("Which item number did you complete?"))

            if completedItem <= len(todos):
                todos.pop(completedItem - 1)
                write_todos(todos)
            else:
                print("item doesnt exist")

        case "exit":
            break

        case _:
            print("That's not a valid command")

print("Bye!")
