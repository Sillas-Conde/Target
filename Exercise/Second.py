

#Number = int(input("DIGITE UM NÚMERO PARA TESTAR: "))
Number = 8

Fibonacci = [0,1]
soma = 1
anterior = 1
anterior_menos_1 = 0
fibonacci_number = 1

while fibonacci_number < Number:

    soma = anterior + anterior_menos_1
    fibonacci_number = soma
    anterior_menos_1 = anterior
    anterior = fibonacci_number


if fibonacci_number == Number:

    
    print('ESTE NÚMERO ESTÁ NA SEQUÊNCIA DE FIBONACCI:',Number)

else:
    print('ESTE NÚMERO NÃO ESTÁ NA SEQUÊNCIA DE FIBONACCI: ',Number)