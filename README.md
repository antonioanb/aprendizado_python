# 🐍 Minha Jornada Python: Do Zero ao Django

Repositório dedicado ao armazenamento das minhas notas, exercícios e projetos práticos realizados durante meus estudos de Python. O objetivo é servir como uma base de consulta técnica pessoal.

## 💻 Minha Estação de Estudos
Para manter o foco e a produtividade, utilizo uma configuração otimizada para Linux:

*   **Sistema Operacional:** Debian GNU/Linux.
*   **Editor de Código:** VS Code (Versão `.deb` nativa).
*   **Estética:** Tema *Plasma Refinado* com terminal em tom **Amber** (Fallout Style).
*   **Shell:** Bash com integração `direnv` e `nix-shell`.

## 📂 Estrutura de Pastas
*   **01-fundamentos/**: Variáveis, tipos de dados e conceitos de memória.
*   **02-estruturas-de-dados/**: Listas, Dicionários, Tuplas e Sets.
*   **03-poo/**: Classes, Herança e Polimorfismo.
*   **04-projetos/**: Pequenas aplicações práticas.

## 🛠️ Como rodar
Este repositório utiliza **Nix** para garantir que o ambiente de desenvolvimento (Python 3.13 + Pylint) seja idêntico e reprodutível.

### 1. Pré-requisitos (Configuração do Sistema)
Antes de escolher uma opção, certifique-se de ter o `direnv` instalado no sistema (Debian ou WSL2) para que a automação funcione:

```bash
sudo apt update && sudo apt install direnv
echo 'eval "$(direnv hook bash)"' >> ~/.bashrc
source ~/.bashrc
```

### 2. Formas de uso:

#### **Opção A: Recomendada (Linux/WSL2 com Nix)**
Esta opção utiliza o `shell.nix` do projeto para configurar tudo automaticamente.
1.  Instale o [Nix](https://nixos.org/download.html).
2.  Entre na pasta do projeto.
3.  Execute `direnv allow` (apenas na primeira vez).
4.  O ambiente será carregado sozinho toda vez que você entrar na pasta.

#### **Opção B: Tradicional (Sem Nix)**
Basta ter o **Python 3.10+** instalado no sistema:
1.  **Crie o ambiente virtual:** `python -m venv .venv`
2.  **Ative o ambiente:**
    *   Windows: `.venv\Scripts\activate`
    *   Linux/macOS: `source .venv/bin/activate`
3.  **(Opcional) Instale o linter:** `pip install pylint`

---
💡 **Nota:** A Minha preferência pela versão **.deb** do VS Code em vez de Flatpak é para garantir acesso total às ferramentas do sistema e ao ambiente Nix.