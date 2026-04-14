# ALog

Ferramenta CLI em Python para leitura e classificação automática de logs de servidores Linux.

## O que faz

- Lê arquivos de log no formato padrão do systemd/journald
- Filtra automaticamente entradas de **ERROR** e **WARNING**
- Exibe data, host, aplicação, nível e mensagem de forma organizada no terminal
- Suporte a passagem de arquivo via argumento na linha de comando

## Como usar

```bash
python argparse.py caminho/do/arquivo
```

Exemplo:

```bash
python argparse.py meus_logs.txt
```

## Exemplo de saída
Data: abr 05 11:10:44
Host: konton
App: dunst[12341]
Nivel: ERROR
Mensagem: Couldn't initialize X11 output. Aborting...

## Tecnologias

- Python 3
- Módulos `re` e `argparse`

## Próximos passos

- Integração com IA para geração de relatórios automáticos
- Suporte a múltiplos arquivos simultaneamente
