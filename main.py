




# Introdução

introduzir = input("Você gostaria de falar um pouco sobre você?\nOpções: sim\n: ")
if introduzir == "sim":
    print("\nPrimeiro, me fale um pouco sobre você...\n")
    myname = input("me fale seu nome: ")
    myold = int(input("me fale sua idade: "))
    mymom = input("me fale o nome da sua mãe: ")
    mydad = input("me fale o nome do seu pai: ")

    if myname == mydad:
        print("\nNossa, você tem o mesmo nome do seu pai!")
    if myname == mymom:
        print("\nNossa, você tem o mesmo nome da sua mãe!")


    print("\nOla, meu nome é", myname, "\nTenho", myold, "anos, \nMinha mãe se chama", mymom, "e eu amo muito ela \nMeu pai se chama", mydad, "e ele é muito legal")
else




# BHASKARA

interesse = input("\nQual a formula matemática você gostaria de testar? \nOpções: Bhaskara, Teorema de Pitágoras, Área de figura plana\n: ")

if interesse == "Bhaskara":

    print("\nAgora, vamos aprender bhaskara!")
    print("Defina os números A, B e C da função: ax² + bx + c = 0")
    a = int(input("Defina o algoritmo A: "))
    b = int(input("Defina o algoritmo B: "))
    c = int(input("Defina o algoritmo C: "))
    d = ( b ** 2) - (4 * a * c)
    print("\nPrimeiro definimos o DELTA, que, utilizando os valores dados, será: \nDelta =", d)
    print("\nAgora, faremos o calculo pela formula de Bhaskara")

    x1bhaskara = (- b + d ** 0.5) / 2 * a
    x2bhaskara = (- b - d ** 0.5) / 2 * a

    print("os resultados são: \nx1 = ", x1bhaskara, "\nx2 = ", x2bhaskara)





# PITAGORAS

if interesse == "Teorema de Pitágoras":

    print("\nAgora, vamos aprender o Teorema de Pitágoras! (ou Pitanga como eu gosto de chamar")
    print("O Teorema de Pitágoras é dado pela função: a² = b² + c²")
    interessepitagoras = input("Em sua questão, você precisa descobrir um cateto ou a hipotenusa?\n: ")
    if interessepitagoras == "cateto":
        print("\nEntão me dê os algoritmos a e b")
        a = int(input("Defina o algoritmo A: "))
        b = int(input("Defina o algoritmo B: "))
        c = (a ** 2) - (b ** 2)
        print("\nO Valor do Cateto Desconhecido dessa função é \n c = ", c)
    elif interessepitagoras == "hipotenusa":
        print("\nEntão me dê os algoritmos b e c")
        b = int(input("Defina o algoritmo B: "))
        c = int(input("Defina o algoritmo C: "))
        a = ((b ** 2) + (c ** 2)) ** 0.5
        print("\nO Valor da Hipotenusa Desconhecida dessa função é \n c = ", a)





# AREA - FIGURA PLANA

if interesse == "Área de figura plana":
    print("\nÓtimo, geometria plana é uma área bastante importante de se aprender!")
    interessearea = input("Você gostaria de fazer o cálculo da área de qual figura plana?\nOpções: Quadrado, Retangulo, Triângulo, Circulo... \n: ")
    if interessearea == "Quadrado":
        print("\nA área de um Quadrado é dada pela fórmula: L²\nsendo que L = medida do lado do quadrado")
# ACABOU SAPORRA

else:
    print("\nfique burro e não aprenda matematica, então tchau")