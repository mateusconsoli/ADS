# Cálculo da nota V 2.0
while True:
    while True:
        try:
            quantidadededesafios = int(input("Quantos desafios tem a disciplina? "))
            if 1 <= quantidadededesafios <= 3:
                break
            print("Número inválido, digite um número entre 1 e 3.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    while True:
        try:
            desafio1 = desafio2 = desafio3 = 0.0
            if quantidadededesafios == 1:
                PESODESAFIO = 0.3
                desafio1 = float(input("Insira sua nota do Desafio 1: "))
                while desafio1 < 0 or desafio1 > 10:
                    print("ERRO: Insira uma nota entre 0 e 10")
                    desafio1 = float(input("Insira sua nota do Desafio 1: "))
            elif quantidadededesafios == 2:
                PESODESAFIO = 0.15
                desafio1 = float(input("Insira sua nota do Desafio 1: "))
                while desafio1 < 0 or desafio1 > 10:
                    print("ERRO: Insira uma nota entre 0 e 10")
                    desafio1 = float(input("Insira sua nota do Desafio 1: "))
                desafio2 = float(input("Insira sua nota do Desafio 2: "))
                while desafio2 < 0 or desafio2 > 10:
                    print("ERRO: Insira uma nota entre 0 e 10")
                    desafio2 = float(input("Insira sua nota do Desafio 2: "))
            else:
                PESODESAFIO = 0.1
                desafio1 = float(input("Insira sua nota do Desafio 1: "))
                while desafio1 < 0 or desafio1 > 10:
                    print("ERRO: Insira uma nota entre 0 e 10")
                    desafio1 = float(input("Insira sua nota do Desafio 1: "))
                desafio2 = float(input("Insira sua nota do Desafio 2: "))
                while desafio2 < 0 or desafio2 > 10:
                    print("ERRO: Insira uma nota entre 0 e 10")
                    desafio2 = float(input("Insira sua nota do Desafio 2: "))
                desafio3 = float(input("Insira sua nota do Desafio 3: "))
                while desafio3 < 0 or desafio3 > 10:
                    print("ERRO: Insira uma nota entre 0 e 10")
                    desafio3 = float(input("Insira sua nota do Desafio 3: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

    while True:
        try:
            PESOAVALIACAO1 = 0.6
            avaliacao1 = float(input("Insira sua nota da Avaliação 1: "))
            while avaliacao1 < 0 or avaliacao1 > 10:
                print("ERRO: Insira uma nota entre 0 e 10")
                avaliacao1 = float(input("Insira sua nota da Avaliação 1: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

    while True:
        try:
            PESOIDEA = 0.1
            idea = float(input("Insira sua nota da Idea: "))
            while idea < 0 or idea > 10:
                print("ERRO: Insira uma nota entre 0 e 10")
                idea = float(input("Insira sua nota da Idea: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

    def notafinal():
        return ((desafio1 + desafio2 + desafio3) * PESODESAFIO) + (avaliacao1 * PESOAVALIACAO1) + (idea * PESOIDEA)

    def aprovacao():
        nf = notafinal()
        if nf >= 6:
            print(f"Você foi aprovado e sua nota é {nf}")
        elif nf < 3:
            print(f"Você foi reprovado, sua nota final foi: {nf}")
        else:
            print(f"Você precisará realizar o exame final pois sua nota não atingiu a média, sua nota foi: {nf}")

    aprovacao()

    while True:
        repetir = input("Deseja executar novamente? (s/n): ").lower()

        if repetir == "s":
            break
        elif repetir == "n":
            print("Programa encerrado.")
            exit()
        else:
            print("Resposta inválida. Digite apenas s ou n.")

#Fim