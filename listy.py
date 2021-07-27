imiona = ["marcin", "Iwona", "Mikolaj", "Aniela"]
print(imiona[0])
print(imiona[1])
print(imiona[2])
print(imiona[3])

# ćw 2
mes1 = f"Witaj,{imiona[0].title()},co u ciebie?"
mes2 = f"Witaj,{imiona[1].title()}, co u ciebie?"
mes3 = f"Witaj,{imiona[2].title()}, co u ciebie?"
mes4 = f"Witaj, {imiona[3].title()}, co u ciebie?"

print(mes1)
print(mes2)
print(mes3)
print(mes4)

pojazdy = ["rower" , "pociąg" , "samochód"]
tekst1 = f"Moim ulubionym pojazdem jest {pojazdy[0]}.Lubie nim jezdzic zwlaszcza w lato"
print(tekst1)
# zamiana elementow na liscie

motocykle = ['honda', 'yamaha', 'suzuki']
print(motocykle)
motocykle[0] = "ducati"
print(motocykle)

#dodawanie elementow do listy za pomoca metody append

motocykle = ["honda", "yamaha", 'suzuki']
motocykle.append("ducati")
print(motocykle)
# dodawanie do pustej listy

motocykle = []
motocykle.append("junak")
motocykle.append("suzuki")
print(motocykle)

# wstawianie elementu do listy za pomoca metody insert(indeks,wartosc)

dzien = ['poniedzialek', 'wtorek', 'czwartek']
print(dzien)
dzien.insert(2, 'sroda')
print(dzien)

# usuwanie elementu za pom. funkcji 'del' oraz 'pop'(jesli zna sie indeks wyrazenia)
motocykle = ["honda", "yamaha", 'suzuki']
print(motocykle)
del motocykle[0]
print(motocykle)

# usuwanie elem. za pomoca funkcji 'pop' ( pozwala wyk. operacje na usunietym elemencie,domyslnie ostatnim z listy)
motocykle = ["honda", "yamaha", 'suzuki']
print(motocykle)

usuniete_motocykle = motocykle.pop()
print(usuniete_motocykle)
#  pop w praktyce
print(f"Ostatino zakupilem motocykl {usuniete_motocykle.title()}")

motocykle = ["honda", "yamaha", 'suzuki']
pierwszy_motor = motocykle.pop(0)
print(f"Moj pierwszy motocykl to {pierwszy_motor.title()}")

# usuniecie elementu za pom. 'remove'( po zawartosci)

motocykle = ["honda", "yamaha", 'suzuki']
print(motocykle)
motocykle.remove('suzuki')
print(motocykle)

# ćw

lista_gości = ['Adam', 'Julka', 'Mama' ]
print(f'Witaj , {lista_gości[0].title()}, zapraszam Cie na obiad!')
print(f'Witaj , {lista_gości[1].title()}, zapraszam Cie na obiad!')
print(f'Witaj , {lista_gości[2].title()}, zapraszam Cie na obiad!')
print("Julka nie moze przyjsc na obiad")

lista_gości[1] = "Babcia"
print(f'Witaj , {lista_gości[0].title()}, zapraszam Cie na obiad!')
print(f'Witaj , {lista_gości[1].title()}, zapraszam Cie na obiad!')
print(f'Witaj , {lista_gości[2].title()}, zapraszam Cie na obiad!')

print('Znalazlem wiekszy stół, bedzie nas wiecej!')

lista_gości.insert(0,'Wojtek')
lista_gości.insert(2,'Wiktoria')
lista_gości.append('Daniel')
print(f"Witaj, {lista_gości[0].title()}, zapraszam na obiad!")
print(f"witaj, {lista_gości[1].title()}, zapraszam na obiad")
print(f"witaj, {lista_gości[2].title()}, zapraszam na obiad!")
print(f"witaj, {lista_gości[3].title()}, zapraszam na obiad")
print(f"witaj, {lista_gości[4].title()}, zapraszam na obiad")
print(f"witaj, {lista_gości[5].title()}, zapraszam na obiad!")
print("niestety mam tylko trzy miejsca!")
gosc1 = lista_gości.pop(1)
print(f'niestety {gosc1.title()}, nie mam dla Ciebie miejsca')
gosc2 = lista_gości.pop(4)
print(f"niestety {gosc2.title()}, nie mam dla ciebie miejsca")
gosc3 = lista_gości.pop(0)
print(f"niestety {gosc3.title()}, nie mam dla ciebie miejsca")

del lista_gości[2]
del lista_gości[1]
del lista_gości[0]
print(lista_gości)
print("lista pusta")
