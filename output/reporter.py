def exibir(entrada):
    mensagem = entrada.get("MESSAGE")
    prioridade = entrada.get("PRIORITY")
    service = entrada.get("_SYSTEMD_UNIT")
    print(f"Mensagem: {mensagem}\nPrioridade: {prioridade}\nApp: {service}")
    print("─" * 40)