import openai
import json
openai.api_key = "TU_WPROWADZ_SWOJ_KLUCZ_API"
model_engine = "text-davinci-002"
model_prompt = (f"Turniej: {tournament_name}\n"
                f"Lokalizacja: {location}\n"
                f"Miejsce: {city}\n"
                f"Nawierzchnia: {surface_type}\n"
                f"Liczba meczy: {matches_count}\n"
                "Moje wyniki:\n"
               )

for match in matches:
    opponent_name = match['opponent_name']
    result = match['result']
    score = match['score']

    # formatowanie wyniku
    if result == "W":
        result_str = "wygrałem z"
    else:
        result_str = "przegrałem z"

    # formatowanie wyniku punktowego
    score_str = ""
    for set_score in score:
        score_str += f"{set_score['player_1']}-{set_score['player_2']} "

    # generowanie postu
    generated_text = openai.Completion.create(
        engine=model_engine,
        prompt=model_prompt +
        f"- {result_str} {opponent_name}: {score_str}\n"
    ).choices[0].text.strip()

    # wyświetlenie postu w terminalu
    print(generated_text)