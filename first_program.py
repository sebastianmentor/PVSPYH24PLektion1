namn = input('Hej, skriv ditt namn: ')
age = input('Vänligen skriv din ålder: ')
animals = input('Vänligen skriv in antal djur du äger: ')
address = input('Vänligen skriv in din address: ')
brutto = input('Vänligen skriv in din bruttolön: ')

print('Hej på dig', namn)
# print('Hej på dig ' + namn)
print('Du är ålder', age, 'och om 10 år kommer du vara', int(age) + 10)
print('Att du har djur är', bool(int(animals)))
print('Du bor på', address)
print('Och efter skatt tjänar du', float(brutto )*0.69)