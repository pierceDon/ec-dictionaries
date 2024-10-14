infile = open('book of John text.txt','r')
file_content = infile.readlines()
book_of_john = []
frequency = {}

for l in file_content:
    book_of_john.extend(l.split())

# print(book_of_john)

for w in book_of_john:
    if w == 'Father':
        if w in frequency:
            frequency[w] += 1
        else:
            frequency[w] = 1
    elif w == 'God':
        if w in frequency:
            frequency[w] += 1
        else:
            frequency[w] = 1
    elif w == 'Christ':
            if w in frequency:
                frequency[w] += 1
            else:
                frequency[w] = 1
    elif w == 'Spirit':
            if w in frequency:
                frequency[w] += 1
            else:
                frequency[w] = 1
    elif w == 'spirit':
            if w in frequency:
                frequency[w] += 1
            else:
                frequency[w] = 1
    elif w == 'life':
            if w in frequency:
                frequency[w] += 1
            else:
                frequency[w] = 1
    elif w == 'man':
            if w in frequency:
                frequency[w] += 1
            else:
                frequency[w] = 1

print(f"""
Father: {frequency['Father']}
God: {frequency['God']}
Christ: {frequency['Christ']}
Spirit: {frequency['Spirit']}
spirit: {frequency['spirit']}
life: {frequency['life']}
man: {frequency['man']}
""")
