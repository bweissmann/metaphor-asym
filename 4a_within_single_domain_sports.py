

from graphs import create_single_domain_similarity_graph
from metaphor import metaphor

start = metaphor().search("Here's the lions vs giants game link from ESPN:").results[0].url
create_single_domain_similarity_graph(start, 3)