"""
W tym pliku lacze tworzenie posta poprzez api chatgpt wraz z pobiernaiem danych z pliku json

Dzialajaca wersja generatora postow.
-> dostaje plik data.json z danymi z turnieju
-> zwraca napisane posty z kazdego turnieju
"""

import json
import openai

openai.api_key = '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'


data = []

with open('data.json') as f:
    data = json.load(f)



for i in range(len(data)-1):
    tab_wyniki = []
    text = ""

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
        
        if round == "R1":
            score_text = "W pierwszej rundzie"
        elif round == "R2":
            score_text = "W drugiej rundzie"
        elif round == "QF":
            score_text = "W cwiercfinale"
        elif round == "SF":
            score_text = "W polfinale"
        elif round == "F":
            score_text = "W finale"

        if win_lose == "W":
            win_lose_text = " wygrałem z "
        elif win_lose == "L":
            win_lose_text = " przegralem z "

        text += score_text + win_lose_text + name_and_surname + "(" + nationality + ")" + score + ". "
        #tab_wyniki.append(text)
    
    
    prompt = f"Bylem w {city[11:]} w kraju {nation[8:]}, gdzie rozegralem {amount} mecz. {text}"
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", # this is "ChatGPT" $0.002 per 1k tokens
    messages=[{"role": "user", "content": "Hej, czy pomożesz mi stworzyć post na facebooka podsumowujący mój udział w turnieju tenisowym? W kolejnym zdaniu masz informacje które mozesz wykorzystac do stworzenia postu" + prompt}]
    )

    reply_content = completion.choices[0].message.content
    print(reply_content)    


    #chce stworzyc aby w princie wypisywal mi sie ladny prompt. Musze dodac opis wynikow po kolei

