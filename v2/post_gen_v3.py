import openai
import os

# Ustawienie klucza API OpenAI
openai.api_key = "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"

# Funkcja, która wykorzystuje API ChatGPT do wygenerowania propozycji posta
def generate_post_summary(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    post_summary = response.choices[0].text.strip()
    return post_summary

# Przykładowy prompt
prompt = "Hej, czy pomożesz mi stworzyć post na facebooka podsumowujący mój udział w turnieju tenisowym? Turniej był rozgrywany w {miejscowość} w {kraj}. Był to turniej {typ} na nawierzchni {nawierzchnia}. W {runda1} {win/los1}{wynik1} z {imie i nazwisko1}, w {runda2} {win/los2}{wynik2} z {imie i nazwisko2}, w {runda3} {win/los3} z {imie_nazwisko3} {wynik3}. Był to udany występ dzięki któremu zdobyłem trzy punkty do rankingu."

# Dane, które będą wstawiane w nawiasy klamrowe w prompt
data = {
    "miejscowość": "Sharm El Sheikh",
    "kraj": "Egipt",
    "typ": "ITF World Tour",
    "nawierzchnia": "twarda",
    "runda1": "pierwszej rundzie wygrałem",
    "runda2": "drugiej rundzie wygrałem",
    "runda3": "QF przegrałem",
    "win/los1": " wygrałem ",
    "win/los2": " wygrałem ",
    "win/los3": " przegrałem ",
    "wynik1": "6-3 2-6 6-2",
    "wynik2": "6-7 7-6 7-6",
    "wynik3": "6-3 2-6 5-7",
    "imie i nazwisko1": "Petrem Nestorem",
    "imie i nazwisko2": "Petrem Benjaminem Privara",
    "imie_nazwisko3": "Mohamedem Safatem"
}

# Zamiana danych w nawiasach klamrowych w prompt na konkretne wartości
prompt = prompt.format(**data)

# Wywołanie funkcji generate_post_summary i wyświetlenie wygenerowanego posta
post_summary = generate_post_summary(prompt)
print(post_summary)
