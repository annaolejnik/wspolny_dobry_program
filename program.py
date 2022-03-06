def przyjmij_tekst():
  path = input("wprowadz sciezke")
  with open (path, 'r') as file:
  content = file.read()
  return content
content = przyjmij_tekst()
content = usun(content)
content2 = liczba_slow(content)
