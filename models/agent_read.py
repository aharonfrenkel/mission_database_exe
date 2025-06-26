class AgentRead:
    def __init__(
            self,
            _id: int,
            code_name: str,
            real_name: str,
            location: str,
            status: str,
            missions_completed: int
    ) -> None:
        self.id = _id
        self.code_name = code_name
        self.real_name = real_name
        self.location = location
        self.status = status
        self.missions_completed = missions_completed

    def __str__(self) -> str:
        return (
            "("
            f"ID: {self.id}, "
            f"Code Name: {self.code_name}, "
            f"Real Name: {self.real_name}, "
            f"Location: {self.location}, "
            f"Status: {self.status}, "
            f"Missions Completed: {self.missions_completed}"
            ")"
        )