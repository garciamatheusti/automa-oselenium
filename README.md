# Automação Chrome (Projeto Modular em Python)

Este projeto demonstra o uso profissional do **Selenium** para automação de navegador Chrome, com perfis temporários isolados, logs centralizados e ciclos  automatizados, voltados para teste em IA do google no ambiente do youtube, testando quanto tempo ela informaria farm de view fraudulenta. 
O teste durou 2 dias com 3 vídeos diferentes, o primeiro caiu com 48 horas, segundo em 16 horas e o terceiro com 2 horas, creio que o canal tenha recebido flag.

## 🧩 Estrutura
- `main.py`: ponto de entrada principal.
- `config.py`: configurações globais.
- `utils/`: contém módulos auxiliares.
  - `drivers.py`: inicialização do Chrome.
  - `profiles.py`: manipulação de perfis.
  - `loggers.py`: sistema de logs.

## 🚀 Como usar
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
