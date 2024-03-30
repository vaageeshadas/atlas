import wikipediaapi
# import openai
from openai import OpenAI




def prep_openai(api_key, org_id):
    OpenAI.api_key = api_key
    OpenAI.organization = org_id
    

# def promp_GPT(prompt):
#     completion = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return completion.choices[0].message["content"]


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
    print(completion.choices[0].message.content)



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
print(history_text[:8000])
print()
print("--------------------------")
print()

prompt = "can you summarize this:" + history_text
print(promp_GPT(prompt, API_KEY_HERE))
                