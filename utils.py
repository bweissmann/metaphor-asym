from urllib.parse import urlparse

def add_response_to_accumulator(from_url, response, accumulator):
    for result in response.results:
        stripped_from_url = from_url.split('?')[0].replace('http://', '').replace('https://', '')
        stripped_result_url = result.url.split('?')[0].replace('http://', '').replace('https://', '')
        accumulator.append((stripped_from_url, stripped_result_url, round(result.score, 3)))


def baseurl(url):
    return urlparse(url).netloc