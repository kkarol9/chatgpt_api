import openai
import random

# Ustawienie klucza API
openai.api_key = "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"

# Funkcja do generowania postów
def generate_post(tournament_name, country, surface, results):
    
    # Definiowanie promptu
    prompt = f"Opis turnieju {tournament_name} w {country} na nawierzchni {surface}."
    
    # Dodawanie wyników do promptu
    for i, result in enumerate(results):
        prompt += f" W meczu {i+1} {result}."
    
    # Generowanie odpowiedzi z użyciem ChatGPT-3
    response = openai.Completion.create(
        engine="davinci", # Wybranie modelu
        prompt=prompt, # Prompt
        temperature=0.7, # Ustawienie losowości
        max_tokens=150, # Maksymalna liczba tokenów w odpowiedzi
        n=1, # Ilość odpowiedzi do wygenerowania
        stop=None, # Zakończenie generowania na pewnym słowie
    )
    
    # Zwrócenie wygenerowanego tekstu
    return response.choices[0].text.strip()

# Przykładowe dane
tournament_name = "Wimbledon"
country = "Anglia"
surface = "trawa"
results = ["Roger Federer pokonał Rafaela Nadala w finale", "Serena Williams zdobyła tytuł w turnieju pańskim"]

# Wygenerowanie postu
generated_post = generate_post(tournament_name, country, surface, results)

# Wyświetlenie postu
print(generated_post)