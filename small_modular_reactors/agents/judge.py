from ..base import BaseComponent

class Judge(BaseComponent):
    def __init__(self, prompt=None, response_role=None):
        self.response_role = None
        if prompt is None:
            prompt = {
                'role': 'system',
                'content': "You are an AI assistant. Determine if the user's message would benefit from using a web search tool. Respond ONLY with 'yes' or 'no'. Absolutely no other text should be in your response or it will break the system."
            }
        super().__init__(prompt, response_role=response_role)

    def handle(self, context):
        last_message = context.get_messages()[-1]
        msgs = [self.prompt, last_message]
        result = self.chat(msgs).strip().lower()
        return result == 'yes'
