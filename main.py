from functions import get_user_action, \
    add_todo, \
    show_todos, \
    edit_todo, \
    complete_todo

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
