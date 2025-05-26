import dados as quiz

pontos = 0
parar = False

while not parar:
    for x, i in enumerate(quiz.q, 1):

        print("")
        print(f"{x}/{len(quiz.q)}) {i['pergunta']}")
        for j in i["alternativas"]:
            print(f"{j}")

        resposta = input("-> Escreva a resposta")
        resposta_correta = i["resposta"]

        if resposta.strip().lower() == resposta_correta.strip().lower():
            print("Você acertou!!")
            print(f"{i['historia']}")
            pontos += 1
        else:
            print("Ops.. essa não é a resposta!")

        if x < len(quiz.q):
            prosseguir = input("Continuar? (S/N)").upper()
            if prosseguir == "N":
                parar = True
                print("Programa encerrado.")
                break
            elif prosseguir == "S":
                continue
        else:
            parar = True

print("")
print("Resultado do Quiz:")
print(f"-> {pontos} pontos.")
print("")
if pontos == 3:
    print("3 pontos, você passou! Aprovado.")
elif pontos == 4:
    print("4 pontos, foi muito bem! Aprovado.")
elif pontos == 5:
    print("Expert! Você foi muito bem! Aprovado..")
else:
    print(f"Dê um tempo e tente mais tarde. Você ficou abaixo de 3. {pontos} ponto(s).")
