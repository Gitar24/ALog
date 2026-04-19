import re
from collections import Counter
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

count = Counter(keywords)
print(keywords)