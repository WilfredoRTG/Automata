import re

NUMEROS = []

def printSavedValues():
    global NUMEROS
    if len(NUMEROS) == 0:
        return
    numbers = ''.join(NUMEROS)
    print(f'TOKEN TEXT: {numbers}')
    print(f'TOKEN LEXICAL CATEGORY: OPERAND')
    NUMEROS = []


def checkOperator(lexical_string):
    # Confirma si es un operador
    m = re.match(r'[-|+|/|*|%]', lexical_string)

    if m:
        switcher = {
            '+': 'ADD',
            '-': 'SUBSTRACT',
            '/': 'DIVIDE',
            '*': 'MULTIPLY',
            '%': 'MODULE'
        }
        printSavedValues()
        print(f'TOKEN TEXT: {m.group(0)}') #El simbolo
        print(f'TOKEN LEXICAL CATEGORY: {switcher[m.group(0)]}') # El tipo

def checkNumbers(lexical_string):
    # Confirma si es un numero
    m = re.match(r'[0-9]', lexical_string)
    
    if m:
        NUMEROS.append(m.group(0))

def checkLetters(lexical_string):
    # Confirma si es letra
    m = re.match(r'[a-zA-Z]', lexical_string)
    
    if m:
        print(f'TOKEN TEXT: {m.group(0)}')
        print(f'TOKEN LEXICAL CATEGORY: OPERAND')

lexical_string = input(str("Input your string:"))
for letter in lexical_string:
    checkOperator(letter)
    checkNumbers(letter)
    checkLetters(letter)
printSavedValues()
