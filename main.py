
# Introdução

myname = input("me fale seu nome: ")
myold = int(input("me fale sua idade: "))
mymom = input("me fale o nome da sua mãe: ")
mydad = input("me fale o nome do seu pai: ")

if myname == mydad:
    print("\nNossa, você tem o mesmo nome do seu pai!")


print("\nOla, meu nome é", myname, "\nTenho", myold, "anos, \nMinha mãe se chama", mymom, "e eu amo muito ela \nMeu pai se chama", mydad, "e ele é muito legal")

# Bhaskara
interesse = input("Qual a formula matemática você gostaria de testar? \nOpções: Bhaskara, XXXXX, XXXXXX\n: ")

if interesse == "Bhaskara":

    print("\nAgora, vamos aprender bhaskara!")
    print("Defina os números A, B e C da função: ax² + bx + c = 0")
    a = int(input("Defina o algoritmo: "))
    b = int(input("Defina o algoritmo: "))
    c = int(input("Defina o algoritmo: "))
    d = ( b ** 2) - (4 * a * c)
    print("\nPrimeiro definimos o DELTA, que, utilizando os valores dados, será: \nDelta =", d)
    print("\nAgora, faremos o calculo pela formula de Bhaskara")

    x1bhaskara = (- b + d ** 0.5) / 2 * a
    x2bhaskara = (- b - d ** 0.5) / 2 * a

    print("os resultados são: \nx1 = ", x1bhaskara, "\nx2 = ", x2bhaskara)

else:
    print("tchau então")