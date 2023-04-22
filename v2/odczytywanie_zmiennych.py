"""
w tym pliku odczytuję zmienne do pliku json
"""
import json

"""
#krok 1 - stworzenie recznie slownika i odczytanie danych
city = 'Jaworzno'
nation = 'POL'
tournament_type = 'ITF'
data = []
data2 = []
for i in range(0, 2):
    data2.append({"Kolejnsoc:" : i})
    #print(data2)
    data.append({'City': city, 'Nation' : nation, 'Tournament type': tournament_type, "kolejnosc: ": data2 })

with open('odczytywanie_zmiennych.json', 'w') as f:
    json.dump(data, f)
"""


"""
#krok 2 - odczytywaanie danych w petli

for tournament in data:
    # odczytanie wartości poszczególnych kluczy w słowniku
    print("City:", tournament['City'])
    print("Nation:", tournament['Nation'])
    print("Tournament type:", tournament['Tournament type'])
    for kolejnosc in tournament["kolejnosc: "]:
        print("Kolejnosc:", kolejnosc["Kolejnsoc:"])


"""
data = []

with open('data.json') as f:
    data = json.load(f)


for i in range(len(data)-1):
    tournament = data[i]
    # odczytanie wartości poszczególnych kluczy w słowniku
    print("City:", tournament['City'])
    print("Nation:", tournament['Nation'])
    print("Tournament type:", tournament['Tournament type'])
    print("Surface:", tournament['Surface'])
    print("Draw:", tournament['Draw'])
    print("Type:", tournament['Type'])
    print("Entry:", tournament['Entry'])
    for result in tournament["Results"]:
        print("    Round:", result["Round"])
        print("        Win/lose:", result["Win/lose"])
        print("        Nationality:", result["Nationality"])
        print("        Name and surname:", result["Name anad surname"])
        print("        Score:", result["Score"])



