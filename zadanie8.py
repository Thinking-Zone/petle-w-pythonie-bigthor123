pada = False
licznik_nie = 0
while not pada:
  print("Nie pada")
  odpowiedz - input("czy pada? (tak/nie)")
  if odpowiedz == 'tak':
    print('powiedziales nie: ', licznik_nie , 'razy')
    pada = True
  elif odpowiedz == 'nie':
    licznik_nie += 1
  else:
    print("to wyjdz na dwor i sie dowiedz")
