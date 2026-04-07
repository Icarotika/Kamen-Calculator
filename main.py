import time


print("\nBem vindo a Calculadora Fodona De Combate 2000")
time.sleep(1)
print("Aqui você pode calcular diretamente as fórmulas mais importantes da Matemática!")
time.sleep(1)


while(True):

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
        time.sleep(2)
        print("\nAgora, faremos o calculo pela formula de Bhaskara")
        time.sleep(2)

        x1bhaskara = (- b + d ** 0.5) / 2 * a
        x2bhaskara = (- b - d ** 0.5) / 2 * a

        print("os resultados são: \nx1 = ", x1bhaskara, "\nx2 = ", x2bhaskara)





    # PITAGORAS

    if interesse == "Teorema de Pitágoras":

        print("\nAgora, vamos aprender o Teorema de Pitágoras! (ou Pitanga como eu gosto de chamar")
        time.sleep(1)
        print("O Teorema de Pitágoras é dado pela função: a² = b² + c²")
        time.sleep(2)
        interessepitagoras = input("Em sua questão, você precisa descobrir um cateto ou a hipotenusa?\n: ")
        if interessepitagoras == "cateto":
            print("\nEntão me dê os algoritmos a e b")
            time.sleep(1)
            a = int(input("Defina o algoritmo A: "))
            b = int(input("Defina o algoritmo B: "))
            c = (a ** 2) - (b ** 2)
            time.sleep(1)
            print("\nO Valor do Cateto Desconhecido dessa função é \n c = ", c)
        elif interessepitagoras == "hipotenusa":
            print("\nEntão me dê os algoritmos b e c")
            time.sleep(1)
            b = int(input("Defina o algoritmo B: "))
            c = int(input("Defina o algoritmo C: "))
            a = ((b ** 2) + (c ** 2)) ** 0.5
            time.sleep(1)
            print("\nO Valor da Hipotenusa Desconhecida dessa função é \n c = ", a)





    # AREA - FIGURA PLANA

    if interesse == "Área de figura plana":
        print("\nÓtimo, geometria plana é uma área bastante importante de se aprender!")
        time.sleep(1)
        interessearea = input("Você gostaria de fazer o cálculo da área de qual figura plana?\nOpções: Quadrado, Retangulo, Triângulo, Circulo... \n: ")

        # QUADRADO
        if interessearea == "Quadrado":
            print("\nA área de um Quadrado é dada pela fórmula: L²")
            time.sleep(1)
            print("sendo que L = medida do lado do quadrado")
            time.sleep(1)
            ladoquadrado = int(input("\nDefina o valor de L: "))
            areaquadrado = ladoquadrado ** 2
            time.sleep(1)
            print("\nA Área deste quadrado é de: ", areaquadrado)

        # RETÂNGULO
        if interessearea == "Retangulo":
            print("\n A área de um Retângulo é dada pela fórmula: B . H")
            time.sleep(1)
            print("Sendo que B = base do retângulo \ne A = altura do retângulo")
            time.sleep(1)
            basedoretangulo = int(input("\nDefina o valor de B: "))
            alturaretangulo = int(input("\nDefina o valor de H: "))
            arearetangulo = basedoretangulo * alturaretangulo
            time.sleep(1)
            print("\nA área deste retângulo é de: ", arearetangulo)

        # TRIÂNGULO
        if interessearea == "Triângulo":
            print("\nA área de um Triângulo é dada pela fórmula: (b . h) / 2")
            time.sleep(1)
            print("Sendo que b = base\ne h = altura")
            time.sleep(1)
            basetriangulo = int(input("\nDefina o valor de b: "))
            alturatriangulo = int(input("\nDefina o valor de h: "))
            areatriangulo = (basetriangulo * alturatriangulo) / 2
            time.sleep(1)
            print("\nA área deste triângulo é de : ", areatriangulo)

        # CIRCULO
        if interessearea == "Circulo":
            print("\nA área de um Circulo é dada pela fórmula: π . r²")
            time.sleep(1)
            print("Sendo que π = pi, ou seja, arredondamos pra 3,14")
            time.sleep(0.5)
            print("e r = raio do circulo")
            time.sleep(1)
            picirculo = 3.14
            raiocirculo = int(input("\nDefina o valor de r: "))
            areacirculo = picirculo * ( raiocirculo ** 2)
            time.sleep(1)
            print("\nA área deste circulo é de: ", areacirculo)
    # ACABOU SAPORRA


    time.sleep(2)
    print("\nBoa, você ficou 0.01% mais esperto!!")
    time.sleep(4)
