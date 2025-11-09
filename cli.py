#from functions import get_todos,write_todos

import functions
import time

now = time.strftime("%b %d ,%Y %H:%M:%S")
print("it is",now)

while True :
    # Get user user input and strip chars frm it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if  user_action.startswith("add"):
            todo = user_action[4:]

            todos = functions.get_todos()

            todos.append(todo+"\n")

            functions.write_todos(todos)

    elif user_action.startswith("show"):

              todos = functions.get_todos()

              #new_todos = []
              #for item in todos:
              #    new_item = item.strip('\n')
              #    new_todos.append(new_item)

              #new_todos = [item.strip('\n') for item in todos]

              for index,item in enumerate(todos):
                  #item = item.title()
                  item = item.strip('\n')
                  row = f"{index+1}-{item}"
                  print(row)
              #print(f"Length is,{index+1}")
              #print(len(todos))
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input('Enter a new todo:')
            todos[number] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
             print("Your command is not valid")
             continue

    elif user_action.startswith("complete"):
        try:
                  number = int(user_action[9:])

                  todos = functions.get_todos()

                  index = number-1
                  to_do_remove = todos[index].strip('\n')
                  todos.pop(index)

                  functions.write_todos(todos)

                  message = f"Todo {to_do_remove} was removed from the list."
                  print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
            break
    else:
          print("Command is not valid")



