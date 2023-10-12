from graphs import create_single_domain_similarity_graph
from metaphor import metaphor

start = (
    metaphor()
    .search("Here's my favorite recipe on slowcookergourmet.net:")
    .results[0]
    .url
)
create_single_domain_similarity_graph(start, 3)
