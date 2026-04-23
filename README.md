# ALog — Analisador de Logs

ALog monitora logs do sistema em tempo real via `journalctl`, filtra pelo que realmente importa e bloqueia IPs suspeitos automaticamente.

---

## Como funciona
journalctl (fonte)
│
▼
Filtro de prioridade (níveis 0–3)
│
▼
Detector de padrões suspeitos
│
┌─┴─────────────┐
│               │
Normal          Suspeito
│               │
Exibe           Conta por IP →
no terminal     bloqueia após 5 ocorrências

---

## Estrutura
alog/
├── config.yaml
├── alog.py
├── core/
│   ├── coletor.py
│   └── filtro.py
└── output/
└── reporter.py

**`alog.py`** — orquestra tudo. É o que você executa.

**`core/coletor.py`** — abre o `journalctl` com `--follow --output=json` e entrega cada log como dicionário Python.

**`core/filtro.py`** — filtra por prioridade (≤ 3), extrai IPs e detecta padrões suspeitos como `Failed password`, `SQL injection`, `segfault`, entre outros.

**`output/reporter.py`** — exibe mensagem, prioridade e serviço no terminal.

---

## Níveis de prioridade

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

> Por padrão o ALog monitora níveis 0–3.

---

## Bloqueio automático de IPs

Se um IP suspeito aparece 5 ou mais vezes nos logs, o ALog roda automaticamente:

```bash
sudo iptables -A INPUT -s <ip> -j DROP
```

---

## Dependências
pyyaml

O resto é tudo da stdlib (`subprocess`, `json`, `re`, `collections`).

---

## Status

- [x] `coletor.py`
- [x] `filtro.py`
- [x] `reporter.py`
- [x] `alog.py`
- [ ] `config.yaml`
- [ ] `ai.py`
