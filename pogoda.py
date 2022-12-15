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
            break

    if row['stacja'] != city:                
        print(f"Nie ma takiego miasta {city}\n")
    
    table = AsciiTable(rows)
    print(table.table)
    print()

    answer = str.lower(input("Zakończyć program? Tak (t) lub nie (n): "))
    if answer == 'n':
        main()
    else:
        print("Do zobaczenia!\n")
        input('Naciśnij dowolny klawisz aby zamknąć okno...')
        # quit()

if __name__ == '__main__':
    main()



