import re
from collections import Counter
import subprocess
#filtra os logs para aqueles que tem o nivel abaixo ou igual a 3
def deve_processar(entrada):
    if int(entrada.get("PRIORITY")) <= 3:
        return True
    else:
        return False
#extrai o ip das mensagens
def extrair_ip(entrada):
    p = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    m = (entrada.get("MESSAGE"))
    ip = re.search(p, m)
    if ip:
        return ip.group()
    else:
        return None

keywords = [
    "Failed password",
    "Invalid user",
    "authentication failure",
    "Connection closed by invalid user",
    "SQL injection",
    "Command Injection",
    "XSS Attack",
    "segfault",
    "Out of memory",
    "kernel: possible SYN flooding"
]
def sus(entrada):
    logs = entrada.get("MESSAGE")
    for word in keywords:
        if word in logs:
            return True
    return None

def monitorar_ip(entrada,contagem):
    ip = extrair_ip(entrada)
    if ip is None:
        return
    contagem[ip] += 1
    if contagem[ip] >= 5:
        subprocess.run(["sudo","iptables","-A","INPUT","-s",ip,"-j","DROP"])