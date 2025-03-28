'''
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tomas Benes
email: tomasbenes21@gmail.com
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

seznam = {'bob':'123', 'ann': 'pass123', 'mike':'password123', 'lizz': 'pas123'}
login = input('username: ')

cara = '-' * 50

#login
if login not in seznam.keys():
    print('unregistered user, terminating the program')
    quit()
else:
    password = input('password: ')
    if password != seznam.get(login):
        print('incorrect password')
        quit()
    else:
        print(cara)
        print('Welcome to the app, ', login)
        texts_qty = len(TEXTS)
        print('We have',texts_qty,'texts to be analyzed')

print(cara)

#analyza_textu
for part in TEXTS:
    print('\n','Number: ', TEXTS.index(part) + 1, '\n', part)

text_number = input('Zadejte cislo textu k analyze: ')

if not text_number.isnumeric():
    print('Neni cislo')
    quit()
elif int(text_number) > 0 and int(text_number) < 4:
    actual_text = TEXTS[int(text_number) - 1]
    print(actual_text)
else:
    print('Tato moznost neni k dispozici')
    quit()

words = []
titlecase_list = []
uppercase_list = []
lowercase_list = []
numeric_list = []
suma = []

# number of words
for sign in actual_text.split():
    words.append(sign.strip(',.?!-'))
# titlecase
    if sign.strip(',.?!-').istitle():
        titlecase_list.append(sign.strip(',.?!-'))
# uppercase & lower_case
    elif sign.strip(',.?!-').islower() and sign.strip(',.?!-').isalpha():
        uppercase_list.append(sign.strip(',.?!-'))
        lowercase_list.append(sign.strip(',.?!-'))
# numeric & sum of numbers
    elif sign.strip(',.?!-').isnumeric():
        numeric_list.append(int(sign.strip(',.?!-')))
        suma.append(sign.strip(',.?!-'))

print(f'There are {(len(words))} words in the selected text.')
print(f'There are {len(titlecase_list)} titlecase words.')
print(f'There are {len(uppercase_list)} uppercase words.')
print(f'There are {len(lowercase_list)} lowercase words.')
print(f'There are {len(numeric_list)} numeric strings.')
print(f'The sum of all the numbers {sum(numeric_list)}.')

print(cara)
print(f'{'LEN'}| {'OCCURENCES'.center(20):<20} |NR.')
print(cara)

#length of words
clean_words = []

for words in TEXTS[0].split():
    clean_words.append(((len(words.strip(',.?!-')))))

rozsah = range(1, max(clean_words)+ 1)

word_count = []

for numbers in rozsah:
    word_count.append(clean_words.count(numbers))

for sequence in list(zip(rozsah, word_count)):
    print(f'{sequence[0]: <2} | {'*' * sequence[1]:<20} | {sequence[1]}')