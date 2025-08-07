from agents import Runner
from .setup import AppContext, config, triage_agent

def main() -> None:
    print("🤖 Triage Agent is ready. Type your request (or 'exit' to quit):\n")

    context = AppContext()

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        result = Runner.run_sync(
            triage_agent,
            user_input,
            run_config=config,
            context=context
        )

        print("Agent:", result.final_output)

if __name__ == "__main__":
    main()
