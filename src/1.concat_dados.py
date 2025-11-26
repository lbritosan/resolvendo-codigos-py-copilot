# Vamos receber dois dados diferentes e concatená-los em uma única string.
def concatena_dados(dado1, dado2):
    return str(dado1) + " " + str(dado2)

# Exemplo de uso
if __name__ == "__main__":

    info1 = input("Digite o primeiro dado: ")
    info2 = input("Digite o segundo dado: ")
    resultado = concatena_dados(info1, info2)
    print("Dados concatenados:", resultado)