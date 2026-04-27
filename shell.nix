{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  # Aqui é lista do que é "invocado" do mundo Nix
  buildInputs = [
    pkgs.python3
    pkgs.python3Packages.pip
    pkgs.python3Packages.virtualenv
    # Se quiser testar o Aseprite aqui dentro no futuro, bastaria adicionar pkgs.aseprite
  ];

  # Isso aqui roda toda vez que você entrar no lab
  shellHook = ''
    echo "--- Laboratório de Python Ativado ---"
    python --version
  '';
}

