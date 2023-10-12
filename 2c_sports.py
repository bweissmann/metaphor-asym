from graphs import create_similarity_graph
from metaphor import metaphor


start = metaphor().search("Here's the ESPN homepage:").results[0].url
create_similarity_graph(start, 5, include_lengths=True)