import re
def analisar(arquivo):
  with open('arquivo','r') as log:
      for x in log:
        resultado = re.search(r"(\w+\s\d+\s[\d:]+)\s(\w+)\s(.+?)\:(.+)", x)
        if 'ERROR' in x or 'WARNING' in x:
           if resultado:
             print(f"\nData:{resultado.group(1)}\nApp:{resultado.group(3)}\nMensagem:{resultado.group(4)}")
