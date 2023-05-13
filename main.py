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


def get_user_action():
    action = input("Type add [todo], show, edit [todo num], complete [todo num] or exit: ")
    action = action.strip()
    return action


def add_todo(action):
    todo = format_string(action[4:])
    all_todos = read_todos()
    all_todos.append(todo)
    write_todos(all_todos)


def edit_todo(action):
    edit_item = int(action[5:])
    todos = read_todos()
    edit_item = edit_item - 1
    todos[edit_item] = format_string(input("update " + todos[edit_item] + " to be: "))
    write_todos(todos)


def complete_todo(action):
    todos = read_todos()
    completed_item = action[9:]
    if completed_item == 'all':
        todos = []
    else:
        completed_item = int(action[9:])
        todos.pop(completed_item - 1)
    write_todos(todos)


def show_todos():
    all_todos = read_todos()
    # example of inline for-loop or list comprehension
    # for each item in todos, return item.strip
    formatted_todos = [item.strip('\n') for item in all_todos]

    for index, item in enumerate(formatted_todos):
        index = index + 1
        formatted_str = f"{index}-{item}"
        print(formatted_str)


while True:
    user_action = get_user_action()

    if user_action.startswith("add"):
        add_todo(user_action)

    elif user_action.startswith("show"):
        show_todos()

    elif user_action.startswith("edit"):
        try:
            edit_todo(user_action)
        except IndexError:
            print("item doesnt exit")
            continue
        except ValueError:
            print("You must enter the number of the todo")
            continue

    elif user_action.startswith("complete"):
        try:
            complete_todo(user_action)
        except IndexError:
            print("Item doesnt exist")
            continue
        except ValueError:
            print("You must enter the number of the todo")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Not a valid command")

print("Bye!")
