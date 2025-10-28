def select_dificulty():
    print("=== SELEÇÃO DE DIFICULDADE ===")
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")

    escolha = input("Escolha a dificuldade (1/2/3): ")

    if escolha == "1":
        print("Você escolheu: Fácil 🐣")
        return "fácil"
    elif escolha == "2":
        print("Você escolheu: Médio ⚔️")
        return "médio"
    elif escolha == "3":
        print("Você escolheu: Difícil 🔥")
        return "difícil"
    else:
        print("Opção inválida! Dificuldade padrão: Fácil 🐣")
        return "fácil"
