dicionario = {
    1: 'um', 2: 'dois', 3: 'tres', 4: 'quatro', 5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez', 11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze',
    15: 'quinze', 16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove', 20: 'vinte', 30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 60: 'sessenta', 70: 'setenta',
    80: 'oitenta', 90: 'noventa', 100: 'cento', 200: 'duzentos', 300: 'trezentos', 400: 'quatrocentos', 500: 'quinhentos', 600: 'seiscentos', 700: 'setecentos', 800: 'oitocentos', 
    900: 'novecentos',
}

# Soma os caracteres de um até noventa e nove 
def umANoventaENove():
    soma = 0
    somaString = str()

    for i in range(1, 20):
        string = str(dicionario.get(i))
        soma = soma + len(string)
        somaString = somaString + string
    for i in range(20, 100):
        if (i % 10 == 0):
            string = str(dicionario.get(i))
            soma = soma + len(string)
            somaString = somaString + string
        else:
            j = i - i % 10
            string = str(dicionario.get(j)) +'e'+ str(dicionario.get(i % 10))
            soma =  soma + len(string)
            somaString = somaString + string
    return soma

def somaUmAte999():
    soma = 0
    # Como de 1 a mil temos a contagem de 1 até 99, se repetindo por 10 vezes, esse laço vai fazer a soma dos caracteres para essa situação
    for i in range(0, 10):
        soma = soma + umANoventaENove()
    # Soma os caracteres de centenas redondas como duzentos, trezentos e etc, até chegar em 900
    for i in range(1, 10): 
        soma = soma + len(str(dicionario.get(i*100)))
        # Como na lingua portuguesa nos temos o "e" para juntar numeros como duzenos "e" um para formarmos 201 e todos os otros numeros, esse laço de
        # repetição somará todas as vezes que isso ocorre. 99 vezes para cada centena
        for j in range(1, 100):
            soma = soma + len(str(dicionario.get(i*100))+'e')
    return soma           

# No resultado final devemos considerar que no dicionario está escrito a palavra cento ao invés de cem, pois a palavra cem apareceria apenas uma vez
# portanto decidi que seria mais viável, no resultado final subtrair 2 caracteres no resultado

# A função final "somaUmAte999", como o nome já diz, soma a quantidade de caracteres de de 1 até 999, então deve-se acrescer mais 3 caracteres no final, que é o tamanho
# da palavra "mil"

# Como tivemos que subtrair dois caracteres por causa do "cem" e somar tres por causa do "mil", somei 1 no resultado final

#Vale lembrar que no algoritmo também foi considerado os "Es", então se temos o numero "Cento e noventa e sete", considerei as duas vezes que o caractere "e" aparece

print('São '+str(somaUmAte999()+1)+' letras no total')