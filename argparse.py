import argparse
from analisador import analisar
parser = argparse.ArgumentParser()
parser.add_argument("arquivo")
args = parser.parse_args()
analisar(args.arquivo)
