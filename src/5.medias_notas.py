# Calculando Média de Notas
# Descrição: Agora vamos calcular a média de três notas fornecidas na entrada do usuário. 
# Uma dica é: Utilize operadores aritméticos para realizar o cálculo da média.

def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

# Exemplo de uso
if __name__ == "__main__":

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    media = calcular_media(nota1, nota2, nota3)
    print("Média das notas:", media)