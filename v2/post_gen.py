import openai
import random

# set up the OpenAI API key
openai.api_key = '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'

# define the base post text
base_post_text = "Uczestniczyłem w turnieju {tournament_name} w {city}, {country}. Grałem na nawierzchni {surface}. W tym turnieju rozegrałem {num_matches} mecze, w których {result_text}em. Wyniki moich meczów: {match_results_text}. Przegrałem z {opponent_names}."

def create_tennis_post(tournament_name, country, city, surface, num_matches, results, opponents):
    # determine whether the player won or lost
    if results[-1] == 'W':
        result_text = 'wygrałem'
        emoji = '🎉'
    else:
        result_text = 'przegrałem'
        emoji = '😔'

    # get the opponent names
    opponent_names = ' z '.join(opponents)

    # format the match results as a string
    match_results_text = ', '.join(results)

    # generate a unique variation of the base post text using GPT-3
    prompt = f'Wygeneruj unikalną wersję następującego postu:\n\n{base_post_text}\n\n'
    prompt += f'Turniej: {tournament_name}\nKraj: {country}\nMiasto: {city}\nNawierzchnia: {surface}\nLiczba meczów: {num_matches}\nWyniki: {match_results_text}\nPrzeciwnicy: {opponent_names}\n'
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, temperature=0.5, max_tokens=200)

    # get the generated post text from the API response
    generated_post_text = response.choices[0].text.strip()

    # add the emoji to the end of the generated post text
    generated_post_text += f' {emoji}'

    # print the generated post text
    print(generated_post_text)

# example usage
tournaments = [
    {
        'tournament_name': 'ITF World Tour',
        'country': 'Egipt',
        'city': 'Sharm El Sheikh',
        'surface': 'twarda',
        'num_matches': 3,
        'results': ['6-3 2-6 6-2', '6-7 7-6 7-6', '6-3 2-6 5-7'],
        'opponents': ['Petrem Nestorem', 'Petrem Benjaminem Privara', 'Mohamedem Safatem']
    },
    # add more tournaments here
]

for tournament in tournaments:
    create_tennis_post(**tournament)
