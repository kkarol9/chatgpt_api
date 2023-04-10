import openai
import json

# Wczytaj klucz API OpenAI
openai.api_key = "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"

# Wczytaj dane zawodników z pliku JSON
with open('jeden_turniej.json') as f:
    data = json.load(f)

# Zdefiniuj funkcję do generowania treści posta na Facebooku
def generate_post(city):#, round, name_surname, score):
    # Użyj API OpenAI do wygenerowania treści posta na Facebooku
    prompt = f"{city}.  💪💪 Jestem mega zadowolony a jutro zawalczę o tytuł. Trzymajcie kciuki ✊️"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    post = response.choices[0].text.strip()
    return post

# Zdefiniuj funkcję do publikowania posta na Facebooku
def publish_post(post):
    # Skorzystaj z biblioteki Facebook SDK, aby opublikować post na Facebooku
    # Kod na potrzeby przykładu nie zawiera implementacji publikacji posta
    print(f"Opublikowano post: {post}")

# Przejdź przez wszystkie wpisy w pliku JSON i wygeneruj posty na ich podstawie
for player in data:
    city = player['City']
    #name = player['name']
    post = generate_post(city)
    publish_post(post)


    # Użyj API OpenAI do wygenerowania treści posta na Facebooku

