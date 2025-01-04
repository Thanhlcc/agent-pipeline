from typing import List

class Pipeline:
    def __init__(self):
        self.name = "00 Echo"

    def pipe(self, user_message: str, model_id: str, messages: List[dict], body: dict):
        print(f"received message from user: {user_message}") # user message to logs
        return (f"received message from user: {user_message}") # user message to UI