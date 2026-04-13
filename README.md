# ALog

Ferramenta CLI em Python para leitura e classificação automática de logs de servidores Linux.

## O que faz

- Lê arquivos de log no formato padrão do systemd/journald
- Filtra automaticamente entradas de **ERROR** e **WARNING**
- Exibe data, aplicação e mensagem de forma organizada no terminal
- 
## Como usar

```bash
python funcoes.py
```

O arquivo de log analisado é definido diretamente em `funcoes.py`:

```python
analisar("meus_logs.txt")
```

Substitua `"meus_logs.txt"` pelo caminho do seu arquivo de log.


## Exemplo de saída
Data: abr 05 10:57:55
App: fluidsynth
Mensagem:  Failed to open the "default" audio device
Data: abr 05 11:10:44
App: dunst
Mensagem:  Couldn't initialize X11 output. Aborting...

# Tecnologias

- Python 3
- Módulo `re` (expressões regulares)

## Próximos passos

- Interface web para visualização dos logs
- Integração com IA para geração de relatórios automáticos
- Suporte a múltiplos arquivos simultaneamente
