import os
with open('names_13_10_2022__19_25_47.txt', 'r', encoding='utf-8') as text:
    data = text.read()
    with open('out2.txt', 'w', encoding='utf-8') as out:
        out.write('\n\n'.join([l for l in data.splitlines()]))
