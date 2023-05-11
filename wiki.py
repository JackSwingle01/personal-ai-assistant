import wikipedia


def get_wiki_page(title: str, search: bool = False) -> wikipedia.WikipediaPage:

    try:
        return wikipedia.page(title, auto_suggest=False)
    except:
        print("Wiki page not found, trying auto-suggest")

    try:
        return wikipedia.page(title, auto_suggest=True)
    except:
        print("Wiki page not found, trying search")

    if search:
        try:
            return wikipedia.page(wikipedia.search(title)[0])
        except:
            print("Wiki page not found")

    return None


def get_wiki_content(title: str, search: bool = False) -> str:
    page = get_wiki_page(title, search=search)
    if page:
        return page.content
    else:
        return "No wiki page found."


def get_wiki_summary(title: str, search: bool = False) -> str:
    page = get_wiki_page(title, search=search)
    if page:
        return page.summary
    else:
        return "No wiki page found."
