class AgentUpdate:
    def __init__(
            self,
            code_name: str = None,
            real_name: str = None,
            location: str = None,
            status: str = None,
            missions_completed: int = None
    ) -> None:
        self.code_name = code_name
        self.real_name = real_name
        self.location = location
        self.status = status
        self.missions_completed = missions_completed

    def __str__(self) -> str:
        parts = []
        if self.code_name: parts.append(f"Code Name: {self.code_name}")
        if self.real_name: parts.append(f"Real Name: {self.real_name}")
        if self.location: parts.append(f"Location: {self.location}")
        if self.status: parts.append(f"Status: {self.status}")
        if self.missions_completed is not None: parts.append(f"Missions Completed: {self.missions_completed}")

        return f"({', '.join(parts)})"

    def to_dict(self):
        return {
            "code_name": self.code_name,
            "real_name": self.real_name,
            "location": self.location,
            "status": self.status,
            "missions_completed": self.missions_completed
        }