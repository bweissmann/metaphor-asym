from graphviz import Digraph
from typing import List, Tuple
import __main__
import os

from metaphor import metaphor


# results is a list of tuples of the form (from_url, to_url, score)
def visualize_results(results: List[Tuple[str, str, float]], include_lengths=False):
    dot = Digraph(comment="Asymmetry in Similirity Scores")

    # Prune graph so that only bidirectional edges exist
    pruned_results = []
    for result in results:
        if result[0] == result[1]:
            continue

        # Check if the symmetrical edge exists
        for check_result in results:
            if (result[1], result[0]) == (check_result[0], check_result[1]):
                pruned_results.append(result)
                break

    # Get contents for all urls
    url_to_contents = {}
    if include_lengths:
        for result in pruned_results:
            if result[0] not in url_to_contents:
                url_to_contents[result[0]] = get_contents_for_url(result[0])
            if result[1] not in url_to_contents:
                url_to_contents[result[1]] = get_contents_for_url(result[1])

    for result in pruned_results:
        from_name = get_display_name(result[0], url_to_contents, include_lengths)
        to_name = get_display_name(result[1], url_to_contents, include_lengths)
        dot.node(from_name)
        dot.node(to_name)
        dot.edge(from_name, to_name, label=str(result[2]))

    file_name = os.path.splitext(os.path.basename(__main__.__file__))[0]

    dot.render(f"output/{file_name}.gv", view=True)


def get_display_name(text, url_to_contents, include_lengths):
    if include_lengths:
        return text + f" (len={len(url_to_contents[text])})"
    else:
        return text



def get_contents_for_url(url: str):
    """
    This is an *incredibly* inefficient way to get the contents of each url
    If this were used in any setting with real traffic, we should save the ids from previous api calls instead of regeneraring them from urls.
    And probably add a caching layer, perhaps a simple sqlite cache of id => contents

    Also, we are not guarenteed that "/search" with a url returns that same url and its id, but i think its been fine so far
    """
    id = metaphor().search(url, type="keyword", num_results=1).results[0].id
    return metaphor().get_contents([id]).contents[0].extract
