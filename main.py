user_prompt = "Enter a todo: "
todo_file = 'todos.txt'


def read_todos():
    # Using with-context-manager, removes need to manually close the file
    with open(todo_file, 'r') as file:
        todo_list = file.readlines()
        return todo_list


def write_todos(todos_list):
    # Using with-context-manager, removes need to manually close the file
    with open(todo_file, 'w') as file:
        file.writelines(todos_list)


def format_string(string):
    return string + '\n'


while True:
    user_action = input("Type add [todo], show, edit [todo num], complete [todo num] or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = format_string(user_action[4:])

        todos = read_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = read_todos()
        # example of inline for-loop or list comprehension
        # for each item in todos, return item.strip
        formatted_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(formatted_todos):
            index = index + 1
            formattedStr = f"{index}-{item}"
            print(formattedStr)

    elif user_action.startswith("edit"):
        editItem = int(user_action[5:])
        todos = read_todos()

        if editItem <= len(todos):
            editItem = editItem - 1
            todos[editItem] = format_string(input("update " + todos[editItem] + " to be: "))
            write_todos(todos)
        else:
            print("item doesnt exit")

    elif user_action.startswith("complete"):
        todos = read_todos()
        completedItem = int(user_action[9:])

        if completedItem <= len(todos):
            todos.pop(completedItem - 1)
            write_todos(todos)
        else:
            print("item doesnt exist")

    elif user_action.startswith("exit"):
        break

    else:
        print("Not a valid command")

print("Bye!")
