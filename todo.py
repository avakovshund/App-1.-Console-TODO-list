todo_list = []
while True:
    todo_input = input("Enter add, show, edit or exit: ")
    todo_input = todo_input.strip()

    match todo_input:
        case "add":
            todo = input("Enter a todo: ")
            todo_list.append(todo.capitalize())
        case "show":
            a = 0
            for item in todo_list:
                a += 1
                print(f"{a}.", item)
        case "edit":
            edit = int(input("Ok! Write the todo`s number you want to edit: ")) - 1
            edited_todo = input("Got it! Write new todo: ")
            todo_list[edit] = edited_todo
        case "exit":
            break
        case _:
            print("Wrong number.")

print("Good luck with all of this shitty tasks!")