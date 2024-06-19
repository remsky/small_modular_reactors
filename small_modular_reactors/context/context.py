class Context:
    def __init__(self):
        self.messages = []
        self.judge_approves = False

    def add_message(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages

    def get_recent(self, n=3):
        return self.messages[-n:]

    def summarize(self):
        return " ".join([msg['content'] for msg in self.messages])
