import streamlit as st

st.title('TO DO-LIST')

st.write('A to-do list program is a simple and efficient application that helps you manage your tasks and stay organized.')

# Initialize session state 
if 'tasks' not in st.session_state:
    st.session_state.tasks = [] 
# Input for new task 
    new_task = st.text_input("Add a new task:") 
# Add button 
    if st.button("Add Task"):
        if new_task:
            st.session_state.tasks.append({'task': new_task, 'done': False}) 
            st.experimental_rerun() 
# Display tasks
            st.subheader("Tasks to Do")
            for i, task in enumerate(st.session_state.tasks):
                if not task['done']:
                    col1, col2 = st.columns([4, 1])
                    col1.write(task['task'])
                    if col2.button("Done", key=f"done_{i}"):
                        task['done'] = True st.experimental_rerun()
                        st.subheader("Completed Tasks") 
                        for task in st.session_state.tasks:
                            if task['done']:
                                st.write(task['task'])
