import subprocess
import json
#permite o uso do journalctl em tempo real e converte ele em json para criar um dicionario
def start_colletor():
    process = subprocess.Popen(["journalctl","--follow","--output=json"],stdout=subprocess.PIPE,text=True)
    for linha in process.stdout:
        entrada = json.loads(linha)
        print(entrada.get("PRIORITY"),entrada.get("MESSAGE"))
if __name__ == "__main__":
    start_colletor()