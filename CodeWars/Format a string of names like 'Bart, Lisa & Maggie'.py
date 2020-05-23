def namelist(names):
    answer = ''
    for i in range(len(names)):
        if i == 0:
            answer += names[i]['name']
        elif i != 0 and i == len(names) - 1:
            answer += ' & ' + names[i]['name']
        else:
            answer += ', ' + names[i]['name']
    return answer

print(namelist([{'name': 'Bart'},{'name': 'Lisa'},\
    {'name': 'Maggie'},{'name': 'Homer'},\
    {'name': 'Marge'}]))