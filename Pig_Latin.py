def pig_it(text):
    split = text.split()
    final = []
    for i in split:
        if i[:1] not in ('!?.'):
            word = i[1:] + i[:1] + 'ay'
            final.append(word)
        else:
            final.append(i)
    text = ' '.join(final)
    return text
    
