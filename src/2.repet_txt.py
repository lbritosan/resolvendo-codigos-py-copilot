# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.
def repete_string(texto, vezes):
    return texto * vezes

# Exemplo de uso
if __name__ == "__main__":

    texto = input("Digite uma string: ")
    vezes = int(input("Digite um número inteiro: "))
    resultado = repete_string(texto, vezes)
    print("String repetida:", resultado)

