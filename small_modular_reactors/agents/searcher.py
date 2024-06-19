import json
from datetime import datetime
from ..base import BaseComponent
from tavily import TavilyClient

class Searcher(BaseComponent):
    def __init__(self, api_key, return_raw=False, response_role='system'):
        self.today = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.tavily = TavilyClient(api_key=api_key)
        self.return_raw = return_raw
        prompt = {
            'role': 'system',
            'content': f"""
            You are an AI assistant who can request tools by responding in a specific way, conforming to the expected values. 
            The current date is {self.today}.
            [AVAILABLE TOOLS] {{ 'name': 'search', 'description': 'Search for anything on the internet. Has live access to the web, fully functional', 'parameters': {{ 'type': 'object', 'properties': {{ 'query': {{ 'type': 'string', 'description': 'The term to search for' }} }} }}}}
            """
        }
        super().__init__(prompt, response_role=response_role)

    def search(self, query):
        response = self.tavily.search(query=query, search_depth="advanced")
        tavily_response = response['results']
        if self.return_raw:
            return tavily_response
        formatted_response = "-".join([f"{r['title']}: {r['content']}" for r in tavily_response])
        return formatted_response

    def handle(self, context):
        last_message = context.get_messages()[-1]
        msgs = [self.prompt, last_message]

        response = self.chat(msgs, format='json')
        try:
            json_resp = json.loads(response)
            query = json_resp['arguments']['query']
            result = self.search(query)
            result = """
            Interpret the following information for your response, quote if relevant, formulating your response as a standalone:
            """ + result
            return result
        except json.JSONDecodeError:
            error_prefix = "Error, this may not be what we were looking for: "
            return error_prefix + response
