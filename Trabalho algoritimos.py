CAPACIDADE_CAIXA = 10


def ler_float(mensagem):
    while True:
        try:
            entrada = input(mensagem).strip().replace(",", ".")
            valor = float(entrada)
            if valor <= 0:
                print("Por favor, digite um valor maior que zero.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida! Digite um número válido (ex: 100.5 ou 100,5).")


def avaliar_peca(peca):
    motivos = []
    if not 95 <= peca["peso"] <= 105:
        motivos.append("peso fora do intervalo de 95g a 105g")
    if peca["cor"] not in ("azul", "verde"):
        motivos.append("cor diferente de azul ou verde")
    if not 10 <= peca["comprimento"] <= 20:
        motivos.append("comprimento fora do intervalo de 10cm a 20cm")
    return motivos


def cadastrar_peca(ids_existentes, aprovadas, reprovadas, caixas, caixa_atual):
    while True:
        id_peca = input("Digite o ID da peca: ").strip()
        if not id_peca:
            print("O ID não pode ser vazio.")
            continue
        if id_peca in ids_existentes:
            print("Este ID já foi cadastrado. Digite um ID único.")
            continue
        break

    peso = ler_float("Digite o peso da peca (g): ")
    cor = input("Digite a cor da peca: ").strip().lower()
    comprimento = ler_float("Digite o comprimento da peca (cm): ")

    peca = {"id": id_peca, "peso": peso, "cor": cor, "comprimento": comprimento}
    ids_existentes.add(id_peca)

    motivos = avaliar_peca(peca)

    if motivos:
        peca["motivos"] = motivos
        reprovadas.append(peca)
        print(f"\n-> Peça {peca['id']} REPROVADA: {'; '.join(motivos)}")
    else:
        aprovadas.append(peca)
        caixa_atual.append(peca)
        print(f"\n-> Peça {peca['id']} APROVADA")

        if len(caixa_atual) == CAPACIDADE_CAIXA:
            caixas.append(list(caixa_atual))
            caixa_atual.clear()
            print("  [!] Caixa fechada por atingir a capacidade maxima.")

    return caixa_atual


def listar_pecas(aprovadas, reprovadas):
    print("\n" + "=" * 40)
    print("PEÇAS APROVADAS:")
    if aprovadas:
        for p in aprovadas:
            print(f"  ID: {p['id']} | Peso: {p['peso']}g | Cor: {p['cor']} | Comprimento: {p['comprimento']}cm")
    else:
        print("  Nenhuma peça aprovada ainda.")

    print("\nPEÇAS REPROVADAS:")
    if reprovadas:
        for p in reprovadas:
            print(f"  ID: {p['id']} | Motivos: {'; '.join(p['motivos'])}")
    else:
        print("  Nenhuma peça reprovada ainda.")
    print("=" * 40)


def remover_peca(ids_existentes, aprovadas, reprovadas, caixas, caixa_atual):
    id_remover = input("Digite o ID da peça a remover: ").strip()

    if id_remover not in ids_existentes:
        print("ID não encontrado.")
        return caixa_atual

    # tenta remover de aprovadas
    for i, p in enumerate(aprovadas):
        if p["id"] == id_remover:
            aprovadas.pop(i)
            ids_existentes.discard(id_remover)
            # verifica se estava na caixa atual
            for j, pc in enumerate(caixa_atual):
                if pc["id"] == id_remover:
                    caixa_atual.pop(j)
                    break
            print(f"Peça {id_remover} removida com sucesso.")
            return caixa_atual

    # tenta remover de reprovadas
    for i, p in enumerate(reprovadas):
        if p["id"] == id_remover:
            reprovadas.pop(i)
            ids_existentes.discard(id_remover)
            print(f"Peça {id_remover} removida com sucesso.")
            return caixa_atual

    print("Peça não encontrada.")
    return caixa_atual


def listar_caixas(caixas, caixa_atual):
    print("\n" + "=" * 40)
    print("CAIXAS FECHADAS:")
    if caixas:
        for i, caixa in enumerate(caixas, start=1):
            print(f"  Caixa {i}: {len(caixa)} peça(s) [Cheia]")
            for p in caixa:
                print(f"    - ID: {p['id']}")
    else:
        print("  Nenhuma caixa fechada ainda.")

    if caixa_atual:
        print(f"\nCaixa atual (aberta): {len(caixa_atual)} peça(s)")
    print("=" * 40)


def gerar_relatorio(aprovadas, reprovadas, caixas, caixa_atual):
    todas_caixas = caixas + ([caixa_atual] if caixa_atual else [])
    print("\n" + "=" * 40)
    print("           RELATÓRIO FINAL")
    print("=" * 40)
    print(f"Total de peças aprovadas : {len(aprovadas)}")
    print(f"Total de peças reprovadas: {len(reprovadas)}")

    if reprovadas:
        print("\nMotivos das reprovações:")
        for peca in reprovadas:
            print(f"  - Peça {peca['id']}: {'; '.join(peca['motivos'])}")

    print(f"\nQuantidade de caixas utilizadas: {len(todas_caixas)}")
    for numero, caixa in enumerate(todas_caixas, start=1):
        status = "Cheia" if len(caixa) == CAPACIDADE_CAIXA else "Incompleta"
        print(f"  Caixa {numero}: {len(caixa)} peça(s) [{status}]")
    print("=" * 40)


def menu():
    print("\n" + "=" * 40)
    print("   SISTEMA DE CONTROLE DE PEÇAS")
    print("=" * 40)
    print("1. Cadastrar nova peça")
    print("2. Listar peças aprovadas/reprovadas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair")
    print("=" * 40)


def main():
    aprovadas = []
    reprovadas = []
    caixas = []
    caixa_atual = []
    ids_cadastrados = set()

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            caixa_atual = cadastrar_peca(ids_cadastrados, aprovadas, reprovadas, caixas, caixa_atual)
        elif opcao == "2":
            listar_pecas(aprovadas, reprovadas)
        elif opcao == "3":
            caixa_atual = remover_peca(ids_cadastrados, aprovadas, reprovadas, caixas, caixa_atual)
        elif opcao == "4":
            listar_caixas(caixas, caixa_atual)
        elif opcao == "5":
            gerar_relatorio(aprovadas, reprovadas, caixas, caixa_atual)
        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida! Digite um número de 0 a 5.")


if __name__ == "__main__":
    main()