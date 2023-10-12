from graphs import construct_pairwise_graph

construct_pairwise_graph([
    "https://www.embra.ai/", 
    "https://www.globalissues.org/",
    "https://myheartbeets.com/",
    "https://www.espn.com/"
], 3, [])

# Note that duplicate edges may occur becuase we remove query params from the URL
# Shockingly, query params actaully seem to affect the similarity score nontrivially