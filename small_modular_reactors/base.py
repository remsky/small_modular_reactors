import ollama

class BaseComponent:
    def __init__(self, prompt, response_role='assistant'):
        self.response_role = response_role
        self.prompt = prompt
        self.client = ollama.Client()

    def chat(self, msgs, model='mistral:latest', format='', options=None):
        response = self.client.chat(
            model=model,
            messages=msgs,
            format=format,
            options=options
        )
        return response['message']['content']

    def handle(self, context):
        raise NotImplementedError("Each agent must implement its own 'handle' method.")
