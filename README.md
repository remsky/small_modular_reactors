
![Small Modular ReActors (2)](https://github.com/remsky/small_modular_reactors/assets/25017870/b1f1490c-4411-4f30-a7ec-a5cdc1ca9ba2)

Small Modular Reactors (SMR) is a lightweight and modular framework for building AI agents that can handle complex workflows.
Designed specifically for use with a local Ollama install, it offers a more transparent agent construction process without unnecessary bloat.
SMR allows developers to see what they're building and understand the flow of interactions between agents.

## Features

- **Modular Design**: Easily add and manage different types of agents, models, literally anything
- **Context Management**: Maintain a context of the conversation that a Manager agent can access and modify independently.
- **Visualization**: Visualize the flow of interactions between agents using `networkx` and `pyvis`. [**WIP**]
- **Simplicity**: Small, simple agents that are easy to modify and extend. No nightmare tangle of chains 

## Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/small-modular-reactors.git
cd small-modular-reactors
pip install .
```
## Dependencies

- `tavily-python==0.3.3`
- `ollama==0.2.1`
- `python-dotenv==1.0.0`
## Dependencies

- `tavily-python==0.3.3`
- `ollama==0.2.1`
- `python-dotenv==1.0.0`

## Usage

Here's the basic example of how to use the `small-modular-reactors` library.:

```python
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
