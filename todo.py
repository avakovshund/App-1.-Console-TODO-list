while True:
    todo_input = input("Enter add, show, edit, complete or exit: ")
    todo_input = todo_input.strip()

    match todo_input:
        case "add":
            todo = input("Enter a todo: ") + '\n'

            with open('todos.txt', 'a') as txt_file:
                txt_file.writelines(todo)
        case "show":
            with open('todos.txt', 'r') as txt_file:
                for index, item in enumerate(txt_file, start=1):
                    print(f"{index}. {item}".strip('\n'))
        case "edit":
            edit = int(input("Ok! Write the todo`s number you want to edit: ")) - 1
            edited_todo = input("Got it! Write new todo: ") + "\n"

            with open('todos.txt', 'r') as txt_file:
                todo_list = txt_file.readlines()

            todo_list[edit] = edited_todo

            with open('todos.txt', 'w') as txt_file:
                txt_file.writelines(todo_list)
        case "complete":
            complete = int(input("Write the todo`s number that you completed: ")) - 1

            with open('todos.txt', 'r') as txt_file:
                todo_list = txt_file.readlines()

            completed_todo = todo_list[complete]
            todo_list.pop(complete)

            with open('todos.txt', 'w') as txt_file:
                txt_file.writelines(todo_list)

            message = f'Congratulations! Todo "{completed_todo.strip('\n')}" was removed from your list.'
            print(message)
        case "exit":
            break
        case _:
            print("Try again.")

print("Good luck with all of this shitty tasks!")