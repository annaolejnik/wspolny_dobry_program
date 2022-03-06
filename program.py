from liczba_slow import*
from licznik_slow import*
from usun import*

def przyjmij_tekst():
  path = input("C:\\Users\\]Ania\\Desktop\\plik_test.txt")
  with open (path, 'r') as file:
    content = file.read()
  return content
content = przyjmij_tekst()
content = usun(content)
content2 = liczba_slow(content)
content = licznik_slow(content)
