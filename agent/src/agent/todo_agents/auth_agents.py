from agents import Agent
from ..todo_tools.auth_tools import signup, login, deleteUser, logout, whoami



session_agent = Agent(
    name="SessionAgent",
    instructions="You tell users who they are logged in as using the `whoami` tool.",
    tools=[whoami],
    handoff_description="Use when user asks 'Who am I?' or 'Am I logged in?'"
)
signup_agent = Agent(
    name="SignupAgent",
    instructions=(
        "You register new users for the todo system.\n\n"
        "Use the `signup` tool when the user provides: `name`, `email`, and `password`.\n"
        "Do not proceed without all required fields.\n"
        "Only use the tool with clear and valid inputs."
    ),
    tools=[signup],
    handoff_description=(
        "Use this agent when the user wants to sign up. "
        "It requires their name, email, and password."
    ),
)

# Login agent
login_agent = Agent(
    name="LoginAgent",
    instructions=(
        "You log users into the todo system.\n\n"
        "Use the `login` tool when the user gives both their `email` and `password`.\n"
        "Never guess missing input.\n"
        "Return only the JWT token from the tool’s response and nothing else."
    ),
    tools=[login],
    handoff_description=(
        "Use this agent when the user wants to log in. "
        "It authenticates credentials and returns a token."
    ),
)

# Logout agent
logout_agent = Agent(
    name="LogoutAgent",
    instructions=(
        "You log users out of the todo system.\n\n"
        "Use the `logout` tool when the user explicitly wants to log out.\n"
        "Clear all session-related context fields such as token, name, email, and password."
    ),
    tools=[logout],
    handoff_description=(
        "Use this agent when the user wants to log out of their account."
    ),
)

# Delete user agent
delete_user_agent = Agent(
    name="DeleteUserAgent",
    instructions=(
        "You delete the currently logged-in user account and their todos from the system.\n\n"
        "Use the `deleteUser` tool only when the user explicitly asks to delete their account.\n"
        "Ensure the user is authenticated before proceeding.\n"
        "After deletion, clear all session-related context fields."
    ),
    tools=[deleteUser],
    handoff_description=(
        "Use this agent when the user wants to permanently delete their account."
    ),
)
