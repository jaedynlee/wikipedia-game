import requests
from bs4 import BeautifulSoup


def get_soup(url):
    """
    Makes a BeautifulSoup object from the given webpage url (basically a textual representation of the page's HTML)

    :param url: The url to make a soup out of
    :return: BeautifulSoup object generated from url
    """
    # Make a GET request to this url and obtain the response
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'referer': 'http://stats.nba.com/scores/'}
    res = requests.get(url, headers=header, timeout=10)
    try:
        res.raise_for_status()
    except:
        return None
    # Create a BeautifulSoup object from the website's response text. Use html5 as the parser.
    soup = BeautifulSoup(res.text, 'html5lib')
    return soup


def get_wiki_links(query):
    """Returns a list of subpage titles from the given Wikipedia page"""
    url = 'https://en.wikipedia.org/wiki/{}'.format(query.replace(' ', '_'))
    soup = get_soup(url)
    if soup:
        body_content = soup.find('div', {'id':'bodyContent'})
        all_links_tags = body_content.find_all('a', href=True)
        all_links = list(map(lambda a: a['href'], all_links_tags))
        wiki_links = list(filter(lambda a: a.startswith('/wiki/') and ':' not in a, all_links))
        queries = list(map(lambda a: a.split('/')[-1].replace('_', ' '), wiki_links))
        return queries
    return []


def wiki_game(start, end, path=[], pages_searched=[]):
    """
    Find a path from one Wikipedia article to another with depth-first search
    :param start: the starting Wikipedia article
    :param end: the goal Wikipedia article
    :param path: the path taken to get to 'start'
    :param pages_searched: an ultimate list of all articles searched so far
    :return: a list of pages representing the path from start to end
    """
    # Check if start and end article are the same
    if start == end:
        print('Start and end are the same!')
        return start
    # Add article to current path and get all subpages
    path.append(start)
    subpages = get_wiki_links(start)
    # Check if there are any links on this page
    if not subpages:
        # print('No subpages found on {}'.format(start))
        return []
    # Check if the end article is linked from this page
    if end in subpages:
        path.append(end)
        return path
    # Go through each of the subpages and perform the same steps
    for page in subpages:
        # Avoid searching pages more than once
        if page in pages_searched:
            # print('Avoiding loop')
            return []
        pages_searched.append(page)
        result = wiki_game(page, end, path=path, pages_searched=pages_searched)
        # If we have discovered a valid path to the end article, return the path
        if result:
            return result

    return []


# Call wiki game
path = wiki_game('Alan Turing', 'The Most Honourable')
print(' -> '.join(path))
