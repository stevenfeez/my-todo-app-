import streamlit as st
import function


todos = function.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function.write_todos(todos)

st.title("My Todo Web App")
st.subheader("This is my todo web app")
st.write("This app is to increase <b>productivity.</b>", unsafe_allow_html=True)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.rerun()


st.text_input(label=" ", placeholder="Add new list...", on_change=add_todo, key='new_todo')


