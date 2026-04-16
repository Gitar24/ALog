import subprocess
import json
def start_colletor():
    process = subprocess.Popen(["journalctl","--follow","--output=json","-p 3"],stdout=subprocess.PIPE,text=True)
    for linha in process.stdout:
        entrada = json.loads(linha)
        print(entrada.get("PRIORITY"),entrada.get("MESSAGE"))
start_colletor()