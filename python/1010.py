product1 = input().split()
product2 = input().split()

price = (int(product1[1]) * float(product1[2])) + (int(product2[1]) * float(product2[2]))

print('VALOR A PAGAR: R$ {:.2f}'.format(price))