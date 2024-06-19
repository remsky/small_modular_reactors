"""
Not functional, placeholder
"""

# import networkx as nx
# # from dash import Dash, dcc, html
# import plotly.graph_objs as go
# from ..context.context import Context

# class Visualizer:
#     def __init__(self, manager):
#         self.manager = manager
#         self.graph = nx.DiGraph()

#     def add_edge(self, from_agent, to_agent, message):
#         self.graph.add_edge(from_agent, to_agent, label=message)

#     def get_graph_data(self):
#         pos = nx.spring_layout(self.graph)
#         edge_trace = go.Scatter(
#             x=[], y=[], line=dict(width=1, color='#888'), hoverinfo='none', mode='lines')
#         node_trace = go.Scatter(
#             x=[], y=[], text=[], mode='markers+text', hoverinfo='text', marker=dict(
#                 showscale=True,
#                 colorscale='YlGnBu',
#                 size=10,
#                 colorbar=dict(thickness=15, title='Node Connections', xanchor='left', titleside='right')
#             )
#         )

#         for edge in self.graph.edges():
#             x0, y0 = pos[edge[0]]
#             x1, y1 = pos[edge[1]]
#             edge_trace['x'] += [x0, x1, None]
#             edge_trace['y'] += [y0, y1, None]

#         for node in self.graph.nodes():
#             x, y = pos[node]
#             node_trace['x'] += [x]
#             node_trace['y'] += [y]
#             node_trace['text'] += [node]

#         return edge_trace, node_trace

#     def handle_message(self, msg):
#         self.manager.context.add_message(msg)
#         previous_agent = 'User'
#         for agent in self.manager.agents:
#             agent_name = type(agent).__name__
#             if agent_name == 'Judge':
#                 if agent.handle(self.manager.context):
#                     self.manager.context.judge_approves = True
#                     self.add_edge(previous_agent, agent_name, msg['content'])
#                     previous_agent = agent_name
#                     continue
#             if agent_name == 'Searcher' and not self.manager.context.judge_approves:
#                 continue

#             response = agent.handle(self.manager.context)
#             self.add_edge(previous_agent, agent_name, response)
#             previous_agent = agent_name
#             self.manager.context.add_message({'role': 'system', 'content': response})
#         return self.manager.context.get_messages()[-1]['content']
