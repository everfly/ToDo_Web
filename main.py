# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:24:56 2023

@author: Cielo
"""

import streamlit as st
import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as f:
        pass

todo_list = functions.get_todo()

def add_todo():
    todo = st.session_state["todo_input"]
    todo = todo.title() + '\n'
    # print(todo)
    todo_list.append(todo)
    functions.write_todo(todo_list)
    st.session_state["todo_input"] = ""


st.title("My ToDo App")
# st.subheader("This is my ToDo App.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todo_list.pop(index)
        functions.write_todo(todo_list)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo: ", placeholder="Add new todo...",
              on_change=add_todo, key="todo_input")


# st.session_state
