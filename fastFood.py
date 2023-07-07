valorHamburguer = float(input("Digite o valor unitário do hambúrguer: "))
quantidadeHamburguer = int(input("Digite a quantidade de hambúrgueres desejada: "))
valorBebida = float(input("Digite o valor unitário da bebida: "))
quantidadeBebida = int(input("Digite a quantidade de bebidas desejada: "))
valorPago = float(input("Digite o valor pago pelo usuário: "))

totalHamburguer = valorHamburguer * quantidadeHamburguer
totalBebida = valorBebida * quantidadeBebida
precoTotal = totalHamburguer + totalBebida
troco = valorPago - precoTotal

print(f"O preço final do pedido é R$ {precoTotal:.2f}. Seu troco é R$ {troco:.2f}.")
