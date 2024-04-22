# Bibliotecas necessárias ao código
import time
import random

# Função definida para organizar o estilo
def imprimir_cabecalho(titulo):
    print()
    print('-' * 60)
    print(titulo)
    print()
    time.sleep(1)
    
# Usando dicionário para armazenar os itens do cardápio e seus preços
cardapio = {
    "Misto quente": 5.00,
    "X-Burguer": 6.00,
    "X-Salada": 7.00,
    "X-Batata": 9.00,
    "X-Egg": 9.00,
    "X-Dog": 10.00,
    "X-Frango": 10.00,
    "X-Italiano": 10.00,
    "X-Calabresa": 10.00,
    "X-Bacon": 10.00,
    "Batata Recheada": 11.00,
    "X-Tudo": 11.00,
    "Pão de Queijo": 6.00,
    "Empada (Doce, Salgada)": 6.00,
    "Coxinha de Frango": 7.00,
    "Pastel de Forno": 7.00,
    "Fritas": 15.00,
    "Refrigerante 2L": 10.00,
    "Refrigerante 1L": 5.00,
    "Coxinha + Pastel F. + refrigerante 1L": 19.00,
    "X-Tudo + Empada + Refrigerante 1L": 22.00,
    "Fritas + Batat R. + Refrigerante 2L": 36.00
}
# Início dos comandos que vão aparecer na tela
imprimir_cabecalho('LUAN LANCHES')

# Seção SAUDAÇÕES
imprimir_cabecalho('SAUDAÇÕES')
print('Olá, querido cliente! Seja bem vindo!')
print()
time.sleep(1)
print('Atenção às instruções: ')
print('1. Aprecie nosso menu')
print('2. Escolha seu lanche ')
print('3. Escreva o nome do lanche no campo: "Digite o nome do seu lanche: " ')
print('4. Digite Sair, para sair do menu ')

# Seção MENU
imprimir_cabecalho('MENU')
# Exibir o cardápio
for item, preco in cardapio.items():
    print(f"[{item}] {'.' * (45 - len(item))} R${preco:.2f}")

# Seção SUA ESCOLHA
imprimir_cabecalho('SUA ESCOLHA ')
# Loop para permitir que o usuário escolha itens do cardápio
soma = 0
opcao = ''
resumo = ''
while opcao != 'Sair':
    opcao = input('Digite o nome do seu lanche: ')
    if opcao in cardapio:
        soma += cardapio[opcao]
        resumo += f'{opcao}, ' 

# seção CARRINHO
imprimir_cabecalho('CARRINHO')
print(f'Seu total ficou R$ {soma:.2f} ')
print()
time.sleep(2)
# intervalo = list(cardapio.keys()): Isso significa que uma lista contendo todas as chaves do dicionário cardapio \
# é criada e atribuída à variável intervalo.
intervalo = list(cardapio.keys())
desconto = soma * 0.1
valor_final = soma - desconto
if soma >= 10:
    print('Parabéns!')
    print()
    time.sleep(1)
    print('Nas compras acima de R$10,00, você pode escolher entre descontos e brindes! Vamos lá? ')
    print()
    time.sleep(1)
    print()

    escolha = input('Qual você prefere? ')

    if escolha == 'Desconto':
        time.sleep(1)
        print(f'Você recebeu um desconto de R${desconto:.2f}')
        time.sleep(1)
        print(f'O valor final da sua compra é de R${valor_final:.2f}')
    else:
        escolha_brinde = random.choice(intervalo)
        print('HMM....Um momento! Estamos sorteando um brinde para você! ')
        time.sleep(3)
        print('Oba!')
        time.sleep(1)
        print(f'Você ganhou: {escolha_brinde}!')

# Seçao PAGAMENTO
time.sleep(1)
imprimir_cabecalho('PAGAMENTO')
print('Muito bem, agora, vamos ao pagamento!')
time.sleep(2)
print(f'Você pediu: {resumo} ')
time.sleep(2)
print('Como prefere pagar? ')
print()
print('''    [1]  PIX
    [2]  Débito
    [3]  Crédito ''')

opçao = int(input('Escolha uma opção: '))
if opçao == 1:
    print('Se prepare para fazer o PIX na entrega ')
else:
    print('Perfeito! Enviaremos a maquineta ')
    time.sleep(1)
    print('Fique atento! Seu pedido chegará em até 30 minutos! ')


