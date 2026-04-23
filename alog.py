from collections import Counter
from core.coletor import start_colletor
from core.filtro import deve_processar, sus, monitorar_ip
from output.reporter import exibir
def main():
    contagem = Counter()
    for entrada in start_colletor():
        if deve_processar(entrada):
            exibir(entrada)
        if suspeito(entrada):
            monitorar_ip(entrada, contagem)
if __name__ == "__main__":
    main()