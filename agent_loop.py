def run_agent_loop(iterations=3):
    for iteration in range(1, iterations + 1):
        print(f"\n--- Iteration {iteration} ---")
        observation = input("Observe: Enter current situation: ")

        if "rain" in observation.lower():
            decision = "Carry an umbrella"
        elif "hot" in observation.lower():
            decision = "Drink water"
        else:
            decision = "Continue normally"

        print("Decide:", decision)
        print("Act:", decision)

    print(f"\nAgent loop completed after {iterations} iterations.")


if __name__ == "__main__":
    run_agent_loop()