# ALog — Analisador de Logs

ALog é uma ferramenta de monitoramento de logs em tempo real para sistemas Linux. Ele coleta logs do `journalctl`, filtra por prioridade, e usa IA para analisar anomalias — podendo corrigi-las automaticamente quando o risco for baixo.

---

## Como funciona

```
journalctl (fonte)
     │
     ▼
Filtro --priority (reduz volume)
     │
     ▼
IA (analisa e classifica o risco)
     │
   ┌─┴─────────────┐
   │               │
Baixo risco     Alto risco
   │               │
Corrige         Exibe sugestão
automático      aguarda você
```

---

## Estrutura do projeto

```
alog/
├── config.yaml          # Configurações do usuário
├── alog.py              # Ponto de entrada — orquestra tudo
├── core/
│   ├── collector.py     # Interface com o journalctl
│   ├── filter.py        # Filtragem por prioridade e regex
│   └── ai.py            # Integração com IA
└── output/
    └── reporter.py      # Formatação e exibição dos resultados
```

### O que cada arquivo faz

**`alog.py`**
Arquivo principal. Você executa ele com `python alog.py`. Não contém lógica — só conecta os módulos.

**`config.yaml`**
Configuração editável pelo usuário. Define prioridade mínima, serviços a monitorar, e comportamento da IA.

**`core/collector.py`**
Abre o processo do `journalctl` com `--follow --output=json` e entrega cada log como um dicionário Python para o resto do programa.

**`core/filter.py`**
Recebe os logs do collector e descarta o que não é relevante com base na prioridade definida no config.

**`core/ai.py`**
Pega os logs filtrados, monta um prompt, envia para a IA e retorna a análise com classificação de risco.

**`output/reporter.py`**
Formata e exibe os resultados no terminal. Decide como mostrar — cores, estrutura, alertas.

---

## Níveis de prioridade (journalctl)

| Nível | Nome | Descrição |
|-------|------|-----------|
| 0 | Emergency | Sistema inutilizável |
| 1 | Alert | Ação imediata necessária |
| 2 | Critical | Condição crítica |
| 3 | Error | Erros comuns |
| 4 | Warning | Avisos |
| 5 | Notice | Normal mas significativo |
| 6 | Info | Informacional |
| 7 | Debug | Mensagens de debug |

> Por padrão o ALog monitora níveis 0–3 (erros e acima).

---

## Correção automática

A IA classifica cada anomalia em três níveis de risco:

- **Baixo** — ALog corrige automaticamente (ex: reiniciar serviço caído)
- **Médio / Alto** — ALog exibe a análise e sugestão, você decide

Esse comportamento é configurável no `config.yaml`.

---

## Dependências

| Necessidade | Biblioteca |
|---|---|
| Leitura de YAML | `pyyaml` |
| Comunicação com journalctl | `subprocess` (built-in) |
| Parsing de JSON | `json` (built-in) |
| Regex | `re` (built-in) |
| IA | `anthropic` |

---

## Status do desenvolvimento

- [x] `collector.py` — coleta e parsing de logs
- [ ] `config.yaml` — configuração
- [ ] `filter.py` — filtragem por prioridade
- [ ] `ai.py` — integração com IA
- [ ] `reporter.py` — exibição
- [ ] `alog.py` — orquestração final
