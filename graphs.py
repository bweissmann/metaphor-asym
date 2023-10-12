
from itertools import permutations
from typing import List
from metaphor import metaphor
from visualize import visualize_results
from utils import add_response_to_accumulator, baseurl


def create_similarity_graph(start_url: str, num_results: int, include_lengths: bool = False) -> None:
    """
    Creates a similarity graph based on the given start URL.

    Makes an initial similarity search based on the start URL, which gives the working set of url domains.
    For each url in the working set, make a similarity search, not including its own domain (otherwise all results come from the same domain)

    From these (num_results + 1) queries, we construct a graphviz graph of the scores between each pair of urls IFF they have a bidirectional edge.
    """
    response = metaphor().find_similar(
        start_url,
        num_results,
        exclude_domains=[baseurl(start_url)],
    )
    accumulator = []
    add_response_to_accumulator(start_url, response, accumulator)

    next_urls = [result.url for result in response.results]

    base_urls = list(set([baseurl(url) for url in next_urls + [start_url]]))
    for next_url in next_urls:
        next_url_base = baseurl(next_url)
        response = metaphor().find_similar(
            next_url,
            num_results,
            include_domains=[base for base in base_urls if base != next_url_base],
        )

        add_response_to_accumulator(next_url, response, accumulator)

    for entry in accumulator:
        print(entry)

    visualize_results(accumulator, include_lengths=include_lengths)


def construct_pairwise_graph(urls: List[str], num_results, include_lengths=False):
    """
    This version forces full connectivity by restricting the include_domains to each url in turn.
    So, this makes about N^2 queries instead of ~N
    """
    accumulator = []
    for url1, url2 in permutations(urls, 2):
        response = metaphor().find_similar(
            url1,
            num_results,
            include_domains=[baseurl(url2)],
        )
        
        add_response_to_accumulator(url1, response, accumulator)

    for entry in accumulator:
        print(entry)
    
    visualize_results(accumulator, include_lengths=include_lengths)


def create_single_domain_similarity_graph(start_url: str, num_results: int, include_lengths: bool = False) -> None:
    """
    Another version which forces all results to be in the same domain instead of different ones.
    """
    response = metaphor().find_similar(
        start_url,
        num_results,
        include_domains=[baseurl(start_url)],
    )
    accumulator = []
    add_response_to_accumulator(start_url, response, accumulator)

    next_urls = [result.url for result in response.results]

    for next_url in next_urls:
        next_url_base = baseurl(next_url)
        response = metaphor().find_similar(
            next_url,
            num_results,
            include_domains=[baseurl(start_url)],
        )

        add_response_to_accumulator(next_url, response, accumulator)

    for entry in accumulator:
        print(entry)

    visualize_results(accumulator, include_lengths=include_lengths)
