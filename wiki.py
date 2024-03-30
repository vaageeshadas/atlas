import wikipediaapi
from openai import OpenAI


def prep_openai(api_key, org_id):
    OpenAI.api_key = api_key
    OpenAI.organization = org_id
    


def promp_GPT(prompt, api_key):
    client = OpenAI(api_key=api_key)
    
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": prompt,
        },
    ],
)
    return completion.choices[0].message.content


def extract_years(content, start_year, end_year):
    relevant_content = []
    for line in content.split('\n'):
        if any(str(year) in line for year in range(start_year, end_year + 1)):
            relevant_content.append(line)
    return '\n'.join(relevant_content)


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
# print(history_text[:8000])
# print()
# print("--------------------------")
# print()

new_text = extract_years(history_text, 1800, 1900)


# prompt = "please provide a DETAILED summary of what is happening during the ____:" + new_text
# print(promp_GPT(prompt, "API_KEY_HERE"))

question = ""
while(question.lower() != "quit"):
    # promp_GPT()  =>  have to figure out whether it's the same thread or do i need to keep giving it 
    # the historical text   also how do i avoid repetition
    pass
