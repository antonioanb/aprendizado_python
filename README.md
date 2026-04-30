# 🐍 Jornada Python: Do Zero ao Django

Repositório dedicado ao armazenamento de notas, exercícios e projetos práticos realizados durante meus estudos de Python. 
O objetivo é servir como uma base de consulta técnica pessoal.

## 📂 Estrutura de Pastas

* **01-fundamentos/**: Variáveis, tipos de dados, conceitos de memória basico de funções.
* **02-estruturas-de-dados/**: Listas, Dicionários, Tuplas e Sets.
* **03-poo/**: Classes, Herança e Polimorfismo.
* **04-projetos/**: Pequenas aplicações práticas.



## 🛠️ Como rodar

Este repositório utiliza **Nix** para garantir que o ambiente de desenvolvimento (Python 3.13 + Pylint) seja idêntico e reprodutível.

### 1. Pré-requisitos (Configuração do Sistema)

Antes de escolher uma opção, certifique-se de ter o `direnv` instalado no seu sistema operacional (Debian ou WSL2) para que a automação funcione:

Bash

```
sudo apt update && sudo apt install direnv
echo 'eval "$(direnv hook bash)"' >> ~/.bashrc
source ~/.bashrc
```

---

### 2. Escolha sua forma de uso:

#### **Opção A: Recomendada (Linux/WSL2 com Nix)**

Esta opção utiliza o `shell.nix` do projeto para configurar tudo automaticamente.

1. Instale o [Nix](https://nixos.org/download.html).

2. Entre na pasta do projeto.

3. Execute `direnv allow` (apenas na primeira vez).

4. **O ambiente será carregado sozinho toda vez que você entrar na pasta.**

#### **Opção B: Tradicional (Sem Nix)**

Se preferir não usar o Nix, basta ter o **Python 3.10+** instalado no seu sistema:

1. **Crie o ambiente virtual:**
   
   Bash
   
   ```
   python -m venv .venv
   ```

2. **Ative o ambiente:**
   
   - **Windows:** `.venv\Scripts\activate`
   
   - **Linux/macOS:** `source .venv/bin/activate`

3. **(Opcional) Instale o linter:** `pip install pylint`

---

### 💡 Por que usar o VS Code Nativo (.deb)?

Para que o **Pylint** e o **Python** do Nix funcionem perfeitamente com a extensão `direnv` no VS Code, é recomendado a instalação da versão **.deb** oficial. Versões em Sandbox (como Flatpak) podem ter dificuldades para acessar as ferramentas instaladas via Nix.
