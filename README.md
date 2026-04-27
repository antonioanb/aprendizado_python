# 🐍 Jornada Python: Do Zero ao Django

Repositório dedicado ao armazenamento de notas, exercícios e projetos práticos realizados durante meus estudos de Python. 
O objetivo é servir como uma base de consulta técnica pessoal.

## 📂 Estrutura de Pastas

* **01-fundamentos/**: Variáveis, tipos de dados, conceitos de memória basico de funções.
* **02-estruturas-de-dados/**: Listas, Dicionários, Tuplas e Sets.
* **03-poo/**: Classes, Herança e Polimorfismo.
* **04-projetos/**: Pequenas aplicações práticas.

## 🛠️ Tecnologias e Ambiente

- **Linguagem:** Python 3.13.12 (Gerenciado via Nix)

- **Sistema Operacional:** Debian GNU/Linux

- **Ambiente de Desenvolvimento:** `nix-shell` (Ambiente isolado e reprodutível)

- **Editor:** VS Code / Vim (Tema Gruvbox / Amber Fallout style)

## 🧪 Como usar o Laboratório Python

Para garantir que o ambiente de estudos seja idêntico ao meu, utilize o arquivo `shell.nix` incluso:

1. Instale o [Nix Package Manager](https://nixos.org/download.html).

2. Na raiz do projeto, execute:
   
   Bash
   
   ```
   nix-shell
   ```

3. O ambiente carregará automaticamente o Python e as ferramentas necessárias sem poluir o sistema operacional.
