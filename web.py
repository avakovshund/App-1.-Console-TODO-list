import streamlit as st
import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass

todos_list = functions.read_file()

def add_todo():
    new_todo = st.session_state["input_todo"] + '\n'

    todos_list.append(new_todo)
    functions.write_file(todos_list)

st.title("TODO List")

for index, todo in enumerate(todos_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos_list.pop(index)
        functions.write_file(todos_list)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo:", placeholder="Add a new todo...", label_visibility="collapsed",
              on_change=add_todo, key="input_todo")

st.session_state