import wikipediaapi
import openai


def prep_openai(api_key, org_id):
    openai.api_key = api_key
    openai.organization = org_id
    

def promp_GPT(prompt):
    completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
    
    return completion.choices[0].message.content


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
# print(history_text)
prep_openai("key", "org_id")

prompt = "find and summarize relating to x, y, z" + history_text
                