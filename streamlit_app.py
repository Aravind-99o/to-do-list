import streamlit as st

st.title('TO DO-LIST')

st.write('A to-do list program is a simple and efficient application that helps you manage your tasks and stay organized.')

def main():
    st.title("To-Do List")

    # Initialize the session state for tasks list if not already initialized
    if "tasks" not in st.session_state:
        st.session_state["tasks"] = []

    # Option to add a new task
    st.header("Add New Task")
    new_task = st.text_input("Enter a new task:")
    if st.button("Add Task"):
        if new_task:
            st.session_state["tasks"].append({"task": new_task, "done": False})
            st.success("Task added!")
        else:
            st.warning("Please enter a task before adding.")

    # Display all tasks
    st.header("Tasks List")
    if st.session_state["tasks"]:
        for index, task in enumerate(st.session_state["tasks"]):
            status = "Done" if task["done"] else "Not Done"
            st.write(f"{index + 1}. {task['task']} - {status}")

            # Add a button to mark the task as done
            if not task["done"]:
                if st.button(f"Mark as Done {index + 1}", key=index):
                    st.session_state["tasks"][index]["done"] = True
                    st.success(f"Task '{task['task']}' marked as done!")
                    st.experimental_rerun()  # Rerun to refresh the task status
    else:
        st.info("No tasks added yet.")

    # Option to exit (not required in Streamlit, but added for user convenience)
    st.header("Exit")
    if st.button("Exit"):
        st.info("Thank you for using the To-Do List app!")
        st.stop()


if __name__ == "__main__":
    main()
