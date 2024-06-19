# %%
import os
from dotenv import load_dotenv

from small_modular_reactors.agents.judge import Judge
from small_modular_reactors.agents.assistant import Assistant
# from small_modular_reactors.agents.summarizer import Summarizer
from small_modular_reactors.agents.searcher import Searcher
from small_modular_reactors.manager.manager import Manager
from small_modular_reactors.context.cycle import Cycle
from small_modular_reactors.context.context import Context

load_dotenv()
# Define a message to process
msg_content = "What are some good songs?"
msg = {
    'role': 'user',
    'content': msg_content
}

# Create agent instances
judge = Judge()
# summarizer = Summarizer()
assistant = Assistant()
searcher = Searcher(api_key=os.getenv("TAVILY_API_KEY"))

# Create a manager and assign the agents
context = Context()
manager = Manager(context)
manager.assign_agents([judge, searcher, assistant])

# Create a cycle with the manager
cycle = Cycle(manager)

# Handle the message and print the response
response = cycle.handle_message(msg)
print(response)
