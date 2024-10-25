import random
pada = random.choice([True, False])
zgaduj = True
while zgaduj:
    odpowiedz = input("Czy pada? (t/n) ").strip().lower()
    
    if odpowiedz not in ['t', 'n']:
        print("Proszę wpisać 't' (tak) lub 'n' (nie).")
        continue
    
    if (pada and odpowiedz == 't') or (not pada and odpowiedz == 'n'):
        print("Brawo! Zgadłeś(aś) poprawnie!")
        zgaduj = False
    else:
        print("Niestety, spróbuj ponownie.")
