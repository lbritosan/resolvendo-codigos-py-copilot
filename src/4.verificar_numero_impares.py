# Verificando Números Pares e Ímpares 
# Descrição: Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 
# Uma dica é: Utilize condicionais para realizar a verificação e, se possível, faça uso do Github Copilot(ou outra IA) para otimizar a estrutura do código.

def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"
    
# Exemplo de uso
if __name__ == "__main__":

    numero = int(input("Digite um número inteiro: "))
    resultado = verificar_par_ou_impar(numero)
    print(f"O número {numero} é {resultado}.")