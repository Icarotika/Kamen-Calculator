import time


pi = 3.1415

print("\n\033[34mBEM VINDO A CALCULADORA FODONA DE COMBATE 666\033[m")
time.sleep(1)
print("Aqui você pode calcular diretamente as fórmulas mais importantes da Matemática!")
time.sleep(1)


while(True):

    print("\nQual a formula matemática você gostaria de testar?")
    time.sleep(1)
    print("Opções: \033[36m")
    time.sleep(0.5)
    print("- Bhaskara")
    time.sleep(0.5)
    print("- Teorema de Pitágoras")
    time.sleep(0.5)
    print("- Área de figura plana")
    time.sleep(0.5)
    print("- Função Afim \033[0m")
    time.sleep(0.5)
    interesse = input("\n: ")

    # BHASKARA



    if interesse == "Bhaskara":

        print("\nAgora, vamos aprender bhaskara!")
        print("Defina os números A, B e C da função:\033[35m ax² + bx + c = 0 \033[0m")
        a = int(input("Defina o algoritmo \033[33mA: \033[0m"))
        b = int(input("Defina o algoritmo \033[33mB: \033[0m"))
        c = int(input("Defina o algoritmo \033[33mC: \033[0m"))
        time.sleep(1)
        d = ( b ** 2) - (4 * a * c)
        print("\nPrimeiro definimos o DELTA, que, utilizando os valores dados, será: \nDelta =", d)
        time.sleep(2)
        print("\nAgora, faremos o calculo pela formula de Bhaskara")
        time.sleep(2)

        x1bhaskara = (-b + d ** 0.5) / (2 * a)
        x2bhaskara = (-b - d ** 0.5) / (2 * a)

        print("os resultados são: \nx1 = ", x1bhaskara, "\nx2 = ", x2bhaskara)





    # PITAGORAS

    elif interesse == "Teorema de Pitágoras":

        print("\nAgora, vamos aprender o Teorema de Pitágoras! (ou Pitanga como eu gosto de chamar")
        time.sleep(1)
        print("O Teorema de Pitágoras é dado pela função:\033[35m a² = b² + c² \033[0m")
        time.sleep(2)
        interessepitagoras = input("Em sua questão, você precisa descobrir um cateto ou a hipotenusa?\n: ")
        if interessepitagoras == "cateto":
            print("\nEntão me dê os algoritmos a e b")
            time.sleep(1)
            a = int(input("Defina o algoritmo \033[33mA: \033[0m"))
            b = int(input("Defina o algoritmo \033[33mB: \033[0m"))
            c = (a ** 2) - (b ** 2)
            time.sleep(1)
            print("\nO Valor do Cateto Desconhecido dessa função é \n c = ", c)
        elif interessepitagoras == "hipotenusa":
            print("\nEntão me dê os algoritmos b e c")
            time.sleep(1)
            b = int(input("Defina o algoritmo \033[33mB: \033[0m"))
            c = int(input("Defina o algoritmo \033[33mC: \033[0m"))
            a = ((b ** 2) + (c ** 2)) ** 0.5
            time.sleep(1)
            print("\nO Valor da Hipotenusa Desconhecida dessa função é \n c = ", a)





    # AREA - FIGURA PLANA

    elif interesse == "Área de figura plana":
        print("\nÓtimo, geometria plana é uma área bastante importante de se aprender!")
        time.sleep(1)
        print("Você gostaria de fazer o cálculo da área de qual figura plana?")
        time.sleep(1)
        print("Opções: \033[36m")
        time.sleep(0.5)
        print("- Quadrado")
        time.sleep(0.5)
        print("- Triangulo")
        time.sleep(0.5)
        print("- Retângulo")
        time.sleep(0.5)
        print("- Circulo \033[0m")
        time.sleep(0.5)
        interessearea = input("\n: ")

        # QUADRADO
        if interessearea == "Quadrado":
            print("\nA área de um Quadrado é dada pela fórmula:\033[35m L² \033[0m")
            time.sleep(1)
            print("sendo que L = medida do lado do quadrado")
            time.sleep(1)
            ladoquadrado = int(input("\nDefina o valor de \033[33mL: \033[0m"))
            areaquadrado = ladoquadrado ** 2
            time.sleep(1)
            print("\nA Área deste quadrado é de: ", areaquadrado)

        # RETÂNGULO
        elif interessearea == "Retângulo":
            print("\n A área de um Retângulo é dada pela fórmula:\033[35m B . H \033[0m")
            time.sleep(1)
            print("Sendo que B = base do retângulo \ne A = altura do retângulo")
            time.sleep(1)
            basedoretangulo = int(input("\nDefina o valor de \033[33mB: \033[0m"))
            alturaretangulo = int(input("Defina o valor de \033[33mH: \033[0m"))
            arearetangulo = basedoretangulo * alturaretangulo
            time.sleep(1)
            print("\nA área deste retângulo é de: ", arearetangulo)

        # TRIÂNGULO
        elif interessearea == "Triângulo":
            print("\nA área de um Triângulo é dada pela fórmula:\033[35m (b . h) / 2 \033[0m")
            time.sleep(1)
            print("Sendo que b = base\ne h = altura")
            time.sleep(1)
            basetriangulo = int(input("\nDefina o valor de \033[33mb: \033[0m"))
            alturatriangulo = int(input("Defina o valor de \033[33mh: \033[0m"))
            areatriangulo = (basetriangulo * alturatriangulo) / 2
            time.sleep(1)
            print("\nA área deste triângulo é de : ", areatriangulo)

        # CIRCULO
        elif interessearea == "Circulo":
            print("\nA área de um Circulo é dada pela fórmula:\033[35m π . r²")
            time.sleep(1)
            print("Sendo que π = pi, ou seja, arredondamos pra 3,14")
            time.sleep(0.5)
            print("e r = raio do circulo")
            time.sleep(1)
            raiocirculo = int(input("\nDefina o valor de \033[33mr: \033[0m"))
            areacirculo = pi * ( raiocirculo ** 2)
            time.sleep(1)
            print("\nA área deste circulo é de: ", areacirculo)

    # PRIMEIRO GRAU

    elif interesse == "Função Afim":
        print("\nVamos agora aprender sobre Função Afim!")
        time.sleep(1.5)
        print("Função Afim, simplificando, é quando se tem uma Função Polinomial definida pela Fórmula:\033[35m \n f(x) = ax + b \033[0m")
        time.sleep(1.5)
        print("A qual buscamos descobrir o resultado de 'y', em determinada fórmula, ao transmutar o valor de 'x'")
        time.sleep(1.5)
        print("Sendo que 'a' não pode ser igual a 0")
        time.sleep(2)
        print("\nMe dê os algorismos 'a' e 'b', então te darei o resultado da Função Afim para\033[35m x = [-1, 0, 1]\033[0m")
        time.sleep(1)
        afima = int(input("\nDefina o valor de \033[33ma: \033[0m"))
        afimb = int(input("Defina o valor de \033[33mb: \033[0m"))
        funcaoafim0 = (afima * -1) + afimb
        funcaoafim1 = (afima * 0) + afimb
        funcaoafim2 = (afima * 1) + afimb
        print("\nOs resultados para x = [-1, 0, 1] desta Função Afim são:")
        time.sleep(0.5)
        print("Se x = -1; y = ", funcaoafim0)
        time.sleep(0.5)
        print("Se x = 0; y = ", funcaoafim1)
        time.sleep(0.5)
        print("Se x = 1; y = ", funcaoafim2)
        time.sleep(1)


    # ACABOU SAPORRA


    time.sleep(2)
    print("\nBoa, você ficou 0.01% mais esperto!!")
    time.sleep(4)
