from agents import Agent

from .todo_agents.todos_agent import (
    get_todos_agent,
    create_todos_agent,
    update_todos_agent,
    delete_todos_agent,
)

from .todo_agents.auth_agents import (
    signup_agent,
    login_agent,
    delete_user_agent,
    logout_agent,
    session_agent
)

triage_agent = Agent(
    name="TriageAgent",
    instructions=(
        "You handle both todo and authentication related requests and route them to the correct agent.\n\n"
        "For todos: If the user wants to view, create, update, or delete a todo, choose the respective todo agent.\n"
        "For auth: If the user wants to sign up, log in, or log out, choose the respective auth agent.\n\n"
        "Do not handle the task yourself — your job is to delegate based on the user's intent."
    ),
    handoffs=[
        get_todos_agent,
        create_todos_agent,
        update_todos_agent,
        delete_todos_agent,
        signup_agent,
        login_agent,
        delete_user_agent,
        logout_agent,
        session_agent
    ],
)
