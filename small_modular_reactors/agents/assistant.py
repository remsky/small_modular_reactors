from ..base import BaseComponent

class Assistant(BaseComponent):
    def __init__(self, prompt=None, response_role='assistant'):
        if prompt is None:
            prompt = {
                'role': 'system',
                'content': """
                You are a knowledgeable rogue AI assistant. 
                Answer the user's queries based on the full conversation context.
                Always produce an opinionated response.
                Do not assume the user is able to view your system messages.
                """
            }
        super().__init__(prompt, response_role=response_role)

    def handle(self, context):
        msgs = context.get_messages()
        response = self.chat(msgs)
        # context.add_message({'role': 'assistant', 'content': response})
        return response
