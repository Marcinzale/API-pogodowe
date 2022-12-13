from requests import get
from json import loads
from terminaltables import AsciiTable

def main():
    city = input("Podaj miasto: ")
    city = city.capitalize()
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)
    rows = [
        ['Miasto', 'Godzina pomiaru', 'Temperatura', 'Ciśnienie']
    ]

    for row in loads(response.text):
        if row['stacja'] == city:
            rows.append([
                row['stacja'],
                row['godzina_pomiaru'],
                row['temperatura'],
                row['cisnienie']
            ])

    table = AsciiTable(rows)
    print(table.table)
    answer = str.lower(input("Zakończyć program? Tak (t) lub nie (n): "))
    if answer == 'n':
        main()
    else:
        print("Do zobaczenia!")
        quit()

if __name__ == '__main__':
    main()



