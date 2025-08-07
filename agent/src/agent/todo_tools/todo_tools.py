import os 
from dotenv import load_dotenv
import requests
from agents import function_tool, RunContextWrapper
load_dotenv()
BASE_URL = os.environ['BASE_URL']


@function_tool
def get_todos(wrapper: RunContextWrapper):
    """
    Fetch and display all todos for the authenticated user.
    """
    token = wrapper.context.token
    if not token:
        return f"Please login or create an account"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/todos/get", headers=headers)
    todos = response.json()
    if not todos:
        return "📭 No todos found."

    result = "📋 Your Todos:\n"
    for todo in todos:
        result += (
            f"\n🆔 ID: {todo.get('_id')}\n"
            f"📌 Title: {todo.get('name')}\n"
            f"📝 Desc: {todo.get('desc')}\n"
            f"✅ Done: {todo.get('completed')}\n"
            f"{'-'*40}\n"
        )
        
    return result


@function_tool
def create_todo(wrapper: RunContextWrapper, name: str, desc: str, completed: bool):
    """
    Create and display a new todo.
    """
    token = wrapper.context.token
    if not token:
        return f"Please login or create an account"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {"name": name, "desc": desc, "completed": completed}
    response = requests.post(f"{BASE_URL}/todos/create", json=payload, headers=headers)
    todo = response.json()

    return (
        f"✅ Todo Created!\n\n"
        f"🆔 ID: {todo.get('_id')}\n"
        f"📌 Title: {todo.get('name')}\n"
        f"📝 Desc: {todo.get('desc')}\n"
        f"✅ Done: {todo.get('completed')}\n"
    )


@function_tool
def update_todo(wrapper: RunContextWrapper, id: str, name: str, desc: str, completed: bool):
    """
    Update and display a todo.
    """
    token = wrapper.context.token
    if not token:
        return f"Please login or create an account"
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {"name": name, "desc": desc, "completed": completed}
    response = requests.put(f"{BASE_URL}/todos/update/{id}", json=payload, headers=headers)
    todo = response.json()

    return (
        f"🔄 Todo Updated!\n\n"
        f"🆔 ID: {todo.get('_id') or id}\n"
        f"📌 Title: {todo.get('name')}\n"
        f"📝 Desc: {todo.get('desc')}\n"
        f"✅ Done: {todo.get('completed')}\n"
    )


@function_tool
def delete_todo(wrapper: RunContextWrapper, id: str):
    """
    Delete a todo and show confirmation.
    """
    token = wrapper.context.token
    if not token:
        return f"Please login or create an account"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(f"{BASE_URL}/todos/delete/{id}", headers=headers)
    result = response.json()

    return f"🗑️ Deleted Todo ID: {id}\n📢 {result.get('message', 'Todo deleted.')}"
