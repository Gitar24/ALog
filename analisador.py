import re
def analisar(arquivo):
   padrao = r"(\w+\s+\d+\s+[\d:]+)\s(\w+)\s+(\w+\[\d+\])\:(.+?)\:(.+)"
   with open(arquivo,'r') as log:
      for linha in log:
         linha = linha.strip()
         if 'ERROR' in linha or 'WARNING' in linha:
            resultado = re.search(padrao, linha)
            if resultado:
               print(f"\nData: {resultado.group(1).strip()}")
               print(f"Host: {resultado.group(2).strip()}")
               print(f"App: {resultado.group(3).strip()}")
               print(f"Nivel: {resultado.group(4).strip()}")
               print(f"Mensagem: {resultado.group(5).strip()}")
            else:
               print(f"\n linha imcompativel com o padrao: {linha.strip()}")
