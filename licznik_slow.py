def licznik(content):
slownik = {}
split_content = content.split(" ")
for i in split_content:
    if i in slownik:
        slownik[i] += 1
    else:
        slownik[i] = 1
return slownik



