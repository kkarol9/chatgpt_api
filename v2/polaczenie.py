"""
W tym pliku lacze tworzenie posta poprzez api chatgpt wraz z pobiernaiem danych z pliku json
"""

import json
#import openai

#openai.api_key = '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'


data = []

with open('data.json') as f:
    data = json.load(f)



for i in range(len(data)-1):
    tournament = data[i]
    # odczytanie wartości poszczególnych kluczy w słowniku
    city = tournament['City']
    nation = tournament['Nation']
    tournament_type = tournament['Tournament type']
    surface = tournament['Surface']
    draw = tournament['Draw']
    type = tournament['Type']
    entry = tournament['Entry']
    
    for result in tournament["Results"]:
        amount = len(tournament["Results"])
        round = result["Round"]
        win_lose = result["Win/lose"]
        nationality = result["Nationality"]
        name_and_surname = result["Name anad surname"]
        score = result["Score"]
    
    print(f"Bylem w {city[11:]} w kraju {nation[8:]}, gdzie rozzegralem {amount} meczy")


    #chce stworzyc aby w princie wypisywal mi sie ladny prompt. Musze dodac opis wynikow po kolei

