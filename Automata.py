#DFA
#x=abbaaa, y=baba, z=abaaabaaab
#a = 0 y b =1 

dfa = {
    0:{'a': 1 , 'b': 4},
    1:{'b': 2},
    2:{'a': 2, 'b': 3},
    3:{'a': 3},
    4:{'a': 4, 'b': 5},
    5:{'a': 5}
}

def checkLanguage(transiciones, estadoInicial, estadosFinales, lenguaje):
    state = estadoInicial
    try:
        for character in lenguaje: 
            state = transiciones[state][character]
        if state in estadosFinales:
            print('The language is approved')
        else:
            print('The language is not approved')
    except:
        print('The language is not approved')    

checkLanguage(dfa, 0, {3, 5}, 'ab')
checkLanguage(dfa, 0, {3, 5}, 'abbaaa')
checkLanguage(dfa, 0, {3, 5}, 'baba')
checkLanguage(dfa, 0, {3, 5}, 'abaaabaaab')