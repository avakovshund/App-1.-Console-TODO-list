import time

import functions

now = time.strftime("%b %d, %Y - %H:%M:%S")
print(f"It is {now} now.")
while True:
    todo_input = input("Enter add, show, edit, complete or exit: ")
    todo_input = todo_input.strip()

    if todo_input.startswith("add"):
        todo = todo_input[4:] + '\n'

        with open('todos.txt', 'a') as txt_file:
            txt_file.writelines(todo)

    elif todo_input.startswith("show"):
        with open('todos.txt', 'r') as txt_file:
            for index, item in enumerate(txt_file, start=1):
                print(f"{index}. {item}".strip('\n'))
                
    elif todo_input.startswith("edit"):
        try:
            edit = int(todo_input[5:]) - 1
            edited_todo = input("Got it! Write new todo: ") + "\n"

            todo_list = functions.read_file()

            todo_list[edit] = edited_todo

            functions.write_file(todo_list)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif todo_input.startswith("complete"):
        try:
            complete = int(todo_input[9:]) - 1

            todo_list = functions.read_file()

            completed_todo = todo_list[complete]
            todo_list.pop(complete)

            functions.write_file(todo_list)

            message = f'Congratulations! Todo "{completed_todo.strip('\n')}" was removed from your list.'
            print(message)
        except ValueError:
            print("Your command is not valid.")
            continue
        except IndexError:
            print("Number is out of list range. Try again!")
            continue
    elif todo_input.startswith("exit"):
        break
    else:
        print("Try again.")
print("Good luck with all of this shitty tasks!")