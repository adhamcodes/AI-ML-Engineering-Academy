class Agent:
    def run(self, request: str, approved: bool = False) -> list[str]:
        trajectory = ["understand_request", "lookup_context"]
        if request == "delete_account":
            trajectory.append("delete_account")
            return trajectory
        trajectory.append("respond")
        return trajectory
