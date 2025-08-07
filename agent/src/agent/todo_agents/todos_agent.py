from agents import Agent
from ..todo_tools.todo_tools import (
    create_todo,
    get_todos,
    update_todo,
    delete_todo,
)

create_todos_agent = Agent(
    name="CreateTodoAgent",
    instructions=(
        "You help create a new todo for the user.\n\n"
        "Use the `create_todo` tool only when the user provides: "
        "Never guess or assume values. Only act when all inputs are explicitly provided."
    ),
    tools=[create_todo],
    handoff_description=(
        "Use this agent when the user wants to add a todo. "
        "It requires name, description, completed status, and token."
    ),
)

get_todos_agent = Agent(
    name="GetTodosAgent",
    instructions=(
        "You fetch todos for the user.\n\n"
        "Never fabricate or guess data — only return actual API responses."
    ),
    tools=[get_todos],
    handoff_description=(
        "Use this agent when the user asks to view their todos. "
        "It returns real todos using the token."
    ),
)

update_todos_agent = Agent(
    name="UpdateTodoAgent",
    instructions=(
        "You update an existing todo.\n\n"
        "Use the `update_todo` tool only when the user provides: "
        "Act only when all fields are clearly provided."
    ),
    tools=[update_todo],
    handoff_description=(
        "Use this agent when the user wants to update a todo. "
        "It requires the todo ID, all updated fields, and token."
    ),
)

delete_todos_agent = Agent(
    name="DeleteTodoAgent",
    instructions=(
        "You delete a todo for the user.\n\n"
        "Never guess or act without explicit permission and full input."
    ),
    tools=[delete_todo],
    handoff_description=(
        "Use this agent when the user wants to delete a todo. "
        "It needs the todo ID and token to proceed."
    ),
)
