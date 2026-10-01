def track_state(max_iters=10, success_at=3):
    state = {
        "done": False,
        "stage": 0,
        "status": None
    }

    for _ in range(max_iters):
        state["stage"] += 1
        print(f"Iteration {state['stage']}")
        print("Observe")
        print("Decide")
        print("Act")

        if state["stage"] == success_at:
            state["done"] = True
            state["status"] = "success"
            return state

    state["done"] = True
    state["status"] = "failure"
    return state