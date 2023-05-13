import functions
import time

print(time.strftime("%b %d, %Y %H:%M"))

while True:

    user_action = functions.get_user_action()

    if user_action.startswith("add"):
        functions.add_todo(user_action)

    elif user_action.startswith("show"):
        functions.show_todos()

    elif user_action.startswith("edit"):
        try:
            functions.edit_todo(user_action)
        except IndexError:
            print("item doesnt exit")
            continue
        except ValueError:
            print("You must enter the number of the todo")
            continue

    elif user_action.startswith("complete"):
        try:
            functions.complete_todo(user_action)
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
