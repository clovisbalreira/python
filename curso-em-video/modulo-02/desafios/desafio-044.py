# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# á vista dinheiro/chegue: 10% de desconto
# á vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
produto = float(input('Digite o valor do produto R$ '))
print('O valor do produto é R$ {:.2f}'.format(produto))
formaPagamento = int(input('Digite a forma de pagamento:\n1 - Á vista ou Cheque ( 10% de desconto )\n2 - Cartão\n'))
if formaPagamento == 1:
    valorAtualizado = produto - (produto * 10 / 100)
    print('Com essa forma de pagamento você de 10% de desconto o valor ficou R$ {:.2f}'.format(valorAtualizado))
elif formaPagamento == 2:
    prestacao = int(input('Quantos prestações quer fazer se pagar\nÁ vista tem 5% porcento de desconto\nAté 2 vezes preço normal\nMais de 3 vezes com 20% porcento de juros\n'))
    if prestacao == 1:
        valorAtualizado = produto - (produto * 5 / 100)
        print('Pagando á vista no cartão você tem 5% de desconto o valor ficou R$ {:.2f}'.format(valorAtualizado))
    elif prestacao == 2:
        valorAtualizado = produto / 2
        print('Pagando em {} vezes\nO valor ficou R$ {:.2f}\nCom as prestações no valor de R$ {:.2f}'.format(prestacao, produto, valorAtualizado))
    else:
        valorTotal = produto + (produto * 20 / 100)
        valorAtualizado = valorTotal / prestacao
        print('Pagando em {} vezes\nO valor ficou R$ {:.2f}\nCom as prestações no valor de R$ {:.2f}'.format(prestacao, valorTotal, valorAtualizado))
else:
    print('Você digitou a opção errada tente novamente')