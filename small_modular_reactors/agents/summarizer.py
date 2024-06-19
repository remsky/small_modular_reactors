from ..base import BaseComponent

class Summarizer(BaseComponent):
    def __init__(self, prompt=None, response_role='assistant'):
        if prompt is None:
            prompt = {
                'role': 'system',
                'content': "You are an AI assistant. Summarize the following conversation into a single paragraph."
            }
        super().__init__(prompt, response_role=response_role)
        self.temperature = 0.5

    def handle(self, context):
        conversation = context.summarize()
        conversation_preface = "Please summarize the following conversation/information into a succinct set of key points, people, events, etc:"
        msgs = [self.prompt, {'role': 'user', 'content': conversation_preface + conversation}]
        summary = self.chat(msgs, options={'temperature': self.temperature})
        context.add_message({'role': 'system', 'content': summary})
        return summary
