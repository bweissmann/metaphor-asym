from graphs import create_similarity_graph
from metaphor import metaphor


start = metaphor().search("Here's my favorite butter chicken recipe:").results[0].url
create_similarity_graph(start, 4, include_lengths=True)