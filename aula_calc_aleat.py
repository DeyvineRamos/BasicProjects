"""
O projeto cria perguntas de operações básicas (+ - * /) entre valores aleatórios de 1 a 99. 
 
Pode-se de maneira prévia definir o número de perguntas a serem realizadas,
já na pergunta inicial
 
Cada questão terá cinco alternativas 
 
Em cada rodada será mostrado o "placa" de acertos e erros
"""
 
import random           # Gerar números aleatórios
import os               # Limpar a tela do terminal
 
def calcul_dicionario(operacao,valor1,valor2):
    if operacao == 1:
        questao['pergunta'] = f'Quanto é: {valor1} + {valor2}'
        valor = valor1+valor2
    elif operacao == 2:
        questao['pergunta'] = f'Quanto é: {valor1} - {valor2}'
        valor = valor1-valor2
    elif operacao == 3:
        questao['pergunta'] = f'Quanto é: {valor1}/{valor2}'
        valor = valor1/valor2
    elif operacao == 4:
        questao['pergunta'] = f'Quanto é: {valor1}*{valor2}'
        valor = valor1*valor2
    else:
        print("Erro")
    return valor
 
def calculadora(operacao,valor1,valor2):
    if operacao == 1:           # Adição
        valor = valor1+valor2
    elif operacao == 2:         # Subtração
        valor = valor1-valor2
    elif operacao == 3:         # Divisão
        valor = valor1/valor2
    elif operacao == 4:         # Multiplicação
        valor = valor1*valor2
    else:
        print("Erro")
    return valor
 
acertos = 0
erros = 0
 
print("\n")
# Determinar o número de perguntas a ser realizadas
perguntas = int(input("Quantas perguntas deverão ser feitas? ")) 
print("\n") 
os.system('cls')  
 
for i in range(perguntas): 
    questao = {
        'pergunta': '',
        'opcoes': ['a','b','c','d','e'],
        'resposta': [],
    }
 
    # Desenvolver um questão principal
 
    # Gerar valores inteiros aleatórios entre 1 e 99: random.randint(1,99)
    valor1 = random.randint(1,99)  
    valor2 = random.randint(1,99)
    # As operações básicas são definidas aleatóriamente, onde:
    # 1 = + (soma)
    # 2 = - (subtração)
    # 3 = / (divisão)
    # 4 = * (multiplicação)
    operacao = random.randint(1,4) 
    # Estabelecer a operação e adiciona-la ao dicionário "questão"
    valor = calcul_dicionario(operacao,valor1,valor2)
 
    # Resposta da equação
    questao['resposta'].append(valor) 
 
 
    ######################### PREENCHER OPÇÕES #########################
 
    # Preencher opções erradas resultantes da operação de outros valores
    # aleatório, utilizando porém a mesma operação base da questão principal
    # 
    # O código abaixo substitui os valores preenchidos anteriormente  
    # na chave opçoes pelos valores resultantes das operações dos outros 
    # valores aleatórios, deixando apenas um indice, também aleatório, para ser
    # posto a resposta certa.
    string = 5
 
    while True:
        op = random.randint(0,4)
        aux1 = random.randint(1,99)
        aux2 = random.randint(1,99)
        valor_aux = calculadora(operacao,aux1,aux2)
 
        questao['opcoes'][op] = valor_aux
 
        for n in questao['opcoes']:
            if type(n) != str:
                string-=1
 
        if string == 1:
            break
 
        string = 5
 
    # Preencher opção certa
    for n in range(5):
        if type(questao['opcoes'][n]) == str:
            questao['opcoes'][n] = valor
            indice = n
 
    # Criar o visual das perguntas e alternativas
    alternativa = ['a','b','c','d','e']
 
    print("\n")
    print(f"[Pergunta {i+1}] {questao['pergunta']}")
    for item,opcao in enumerate(questao['opcoes']):
        if operacao == 3:
            print(f"{alternativa[item]}) {opcao:.3f}")
        else:
            print(f"{alternativa[item]}) {opcao}")
 
    # Escolher uma opção
    escolha = input("Qual o item está correto? ") 
 
    # Verificar se o elemento digitado é válido na lógica do algoritmo e 
    # possibilita-lo sua reinscrição caso necessário
    while True:
        if escolha in alternativa:
            break
        else:
            print("Digite uma alternativa válida!")
            print("\n")
            escolha = input("Qual o item está correto? ") 
 
    # Verificar a resposta e informar se a opção escolhida está correta ou 
    # errada
    print("\n")
    if escolha == alternativa[indice]:
        print("   👍 Acertou 👍  ")
        acertos+=1
    else:
        print("   ❌ Errado ❌   ")
        erros+=1
 
    # Número de acertos e erros a cada rodada
    print("\n")
    print(f"Acertos: {acertos} | Erros: {erros}")
    
    # Pausa na execução das operações
    print("\n")
    input("Pressione enter para proxima pergunta!")
    os.system('cls')
    
print("\n")
print(f"Placar final: {acertos} acertos | {erros} erros")
print("\n")