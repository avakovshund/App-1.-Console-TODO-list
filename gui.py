import functions
import FreeSimpleGUI as sg
import time

sg.theme("Black")
clock = sg.Text('', key='clock', font=('Crimson Pro', 12))
label = sg.Text("Write a new TODO", font=('Crimson Pro', 12))
input_box = sg.InputText(tooltip="Enter to-do", key="input")
add_button = sg.Button("Add", font=('Crimson Pro Bold', 12))
list_box = sg.Listbox(values=functions.read_file(), key="todos", enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit", font=('Crimson Pro Bold', 12))
complete_button = sg.Button("Complete", font=('Crimson Pro Bold', 12))
exit_button = sg.Button("Exit", font=('Crimson Pro Bold', 12))

window = sg.Window("What TODO",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]])
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y - %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.read_file()
            new_todo = values["input"] + '\n'
            todos.append(new_todo)
            functions.write_file(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["input"] + '\n'

                todos = functions.read_file()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_file(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select a todo first.",
                         button_color="black",
                         background_color="red",
                         font=('Crimson Pro Bold', 12))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]

                todos = functions.read_file()
                todos.remove(todo_to_complete)
                functions.write_file(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select a todo first.",
                         button_color="black",
                         background_color="red",
                         font=('Crimson Pro Bold', 12))
        case "todos":
            window["input"].update(value=values["todos"][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

print("Got to go. See you!")
window.close()