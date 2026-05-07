repetições = int(input("digite um numero de vezes: "))

soma = 0
menor = 999999999
maior = -1
numeros = []
for n in range(1, repetições + 1): 
    num = int(input("digite um numero: "))
    numeros.append(num)
    if maior < num:
        maior = num
    if menor > num:
        menor = num
    soma += num
    


media = soma / repetições

print(f'A soma dos números é: {soma}.') 
print(f'A média é igual à: {media}.')
print(f'O maior numero é igual à: {maior}.')
print(f'O menor número é igual: {menor}.')

x = 0

for numero in numeros:
    if numero > media:
        x += 1

print(f'E os números acima da média são/ é: {x}')
