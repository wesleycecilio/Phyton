v=float(input('Qual o valor da mercadoria que o cliente está comprando?'))
print('Ele está comprando no valor de {} reias? \ [1] - SIM \[2] - NÃO:'.format(v))
op=int(input('Confirme por favor!!'))
if op==1:
    print('Escolha a forma de pagamento:\n A vista / Cheque [1]\n A vista no cartão [2]\n No credito 2x [3]\n No credito 3x ou mais [4]')
    p=int(input('Informe a forma de pagamento:'))
    if p == 1:
        print('O valor terá um desconto de 10% e o cliente pagará {} reias'.format(v*0.9))
    elif p== 2:
        print('O valor téra um desconto de 5% e o cliente paragá {} reias'.format(v*0.95))
    elif p==3:
        print('O valor não terá desconto,será divido de 2 x e cada parcela será {} reias sem juros totalizando o montante de {} reias'.format(v/2,v))
    elif p==4:
        print('O valor terá um acrecimo de 30%')
        par=int(input('Informe quantas parcelas o cliente vai querer:'))
        if par==3 or par>3:
            print('O valor total da compra ficará em {} reias e cada parcela sairá a {} reias'.format(v*1.30,v*1.30/par))
        else:
            print('FIM')
    else:
        print('FIM DA COMPRA')
else:
    print('Informe o valor correto')
