# 🧠 Projeto: Renomeador de Arquivos em Lote (Python)

Um pequeno projeto desenvolvido com o objetivo de **automatizar o processo de renomear arquivos** em uma pasta, usando **Python**.  
O script percorre os arquivos, aplica um **prefixo personalizado**, adiciona **numeração sequencial com zero padding** e **evita sobrescrever nomes existentes**.

---

## ⚙️ Funcionalidades
- Renomeia arquivos com prefixo personalizado (`foto_`, `documento_`, etc.)
- Ordenação dos arquivos (alfabética ou por data de modificação)
- Garante nomes únicos (evita sobrescritas acidentais)
- Modo “Dry Run” para simular a execução antes de aplicar mudanças
- Zero-padding automático (ex: `foto_001`, `foto_002`, …)
- Tratamento de erros e mensagens informativas no console

---

## 💡 Motivação e Aprendizado

Encontrei um código cru com a ideia básica de renomear arquivos e decidi transformá-lo em algo mais completo e profissional.  
Durante o processo:
- **Estudei linha por linha** do código original.  
- **Identifiquei limitações e erros** (como ausência de tratamento de exceções, risco de sobrescrita, e falta de ordenação).  
- Pedi **auxílio de uma IA (ChatGPT)** para revisar, sugerir boas práticas, explicar cada parte de forma técnica e formatação do README para melhora profissional.  
- A partir disso, **reescrevi e documentei o projeto** de forma estruturada.

Este projeto mostra não apenas o uso da linguagem Python, mas também **a capacidade de aprender, aprimorar código existente e aplicar raciocínio lógico com apoio de IA.**

---

## 🚀 Como usar

### 📦 Requisitos
- Python 3.8+
- Nenhuma dependência externa