# Verificando Palíndromos
# Descrição: Vamos testar se uma palavra é um palíndromo?! 
# Uma dica é: Utilize
# conceitos de manipulação de strings para inverter a palavra e comparar com a original.


def verificar_palindromo(palavra):
    palavra_invertida = palavra[::-1]
    return palavra == palavra_invertida

# Exemplo de uso
if __name__ == "__main__":

    palavra = input("Digite uma palavra: ")
    if verificar_palindromo(palavra):
        print(f"A palavra '{palavra}' é um palíndromo.")
    else:
        print(f"A palavra '{palavra}' não é um palíndromo.")