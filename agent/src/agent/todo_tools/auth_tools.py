import os 
from dotenv import load_dotenv
import requests
from agents import function_tool, RunContextWrapper

load_dotenv()
BASE_URL = os.environ["BASE_URL"]



@function_tool
def whoami(wrapper: RunContextWrapper):
    """
    Show the currently authenticated user’s session info: name, email, and whether a token is present.
    """
    token = wrapper.context.token
    name = wrapper.context.name
    email = wrapper.context.email

    if not token:
        return "🔒 You are not logged in."

    response = "🧑‍💼 You are currently logged in.\n"
    if name:
        response += f"• Name: {name}\n"
    if email:
        response += f"• Email: {email}\n"
    response += "• ✅ Authenticated session is active."

    return response

@function_tool
def signup(wrapper: RunContextWrapper ,name: str, email: str, password: str):
    if wrapper.context.token:
        return "Please logout first to create another account."

    payload = {"name": name, "email": email, "password": password}
    response = requests.post(f"{BASE_URL}/auth/signup", json=payload)
    return response.json()

@function_tool
def login(wrapper: RunContextWrapper, email: str, password: str):
    if wrapper.context.token:
        return "Please logout first before logging into another account."

    payload = {"email": email, "password": password}
    response = requests.post(f"{BASE_URL}/auth/login", json=payload)

    if response.status_code == 200:
        data = response.json()
        token = data.get("token")
        user = data.get("user")  

        if token and user:
            wrapper.context.token = token
            wrapper.context.name = user.get("name")
            wrapper.context.email = user.get("email")
            print(data, wrapper.context.name, wrapper.context.email)

            return {"message": "Login successful", "token": token}

    return response.json()


@function_tool
def deleteUser(wrapper: RunContextWrapper):
    if not wrapper.context.token:
        return "You are not currently logged in. Please login first."

    headers = {"Authorization": f"Bearer {wrapper.context.token}"}
    response = requests.delete(f"{BASE_URL}/auth/deleteUser", headers=headers)

    if response.status_code == 200:
        wrapper.context.token = None
        wrapper.context.name = None
        wrapper.context.email = None
        return {"message": "User and all related todos deleted successfully."}

    elif response.status_code == 401:
        return {"error": "Unauthorized. Please log in again."}
    elif response.status_code == 404:
        return {"error": "User not found."}
    else:
        return {
            "error": "Failed to delete user",
            "status_code": response.status_code,
            "details": response.json()
        }


@function_tool
def logout(wrapper: RunContextWrapper):
    if not wrapper.context.token:
        return "You are not logged in."

    wrapper.context.token = None
    wrapper.context.name = None
    wrapper.context.email = None

    return "User logged out successfully."
