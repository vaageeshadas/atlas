import wikipediaapi

def fetch_history(country):
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent='Atlas - SteelHacks 2024 (vad50@pitt.edu)',
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )

    page_title = "History of " + country

    p_wiki = wiki_wiki.page(page_title)

    return p_wiki.text


country_name = "Japan"
history_text = fetch_history(country_name)
print(history_text)