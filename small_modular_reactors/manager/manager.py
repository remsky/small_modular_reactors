from ..context.context import Context

class Manager:
    def __init__(self, context):
        self.agents = []
        self.context = context

    def assign_agents(self, agents):
        self.agents = agents

    def handle_message(self, msg):
        self.context.add_message(msg)
        for agent in self.agents:
            if type(agent).__name__ == 'Judge':
                if agent.handle(self.context):
                    self.context.judge_approves = True
                    continue
            if type(agent).__name__ == 'Searcher' and not self.context.judge_approves:
                continue

            response = agent.handle(self.context)
            # print(response)
            if agent.response_role:
                self.context.add_message({'role': agent.response_role, 'content': response})
                
        return self.context.get_messages()[-1]['content']

    def get_context(self):
        return self.context
