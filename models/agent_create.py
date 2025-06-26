class AgentCreate:
    def __init__(
            self,
            code_name: str,
            real_name: str,
            location: str,
            status: str
    ) -> None:
        self.code_name = code_name
        self.real_name = real_name
        self.location = location
        self.status = status
        self.missions_completed = 0

    def __str__(self) -> str:
        return (
            "("
            f"Code Name: {self.code_name}, "
            f"Real Name: {self.real_name}, "
            f"Location: {self.location}, "
            f"Status: {self.status}, "
            f"Missions Completed: {self.missions_completed}"
            ")"
        )