{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  # Aqui é lista do que é "invocado" do mundo Nix
  buildInputs = [
    pkgs.python3
    pkgs.python3Packages.pip
    pkgs.python3Packages.virtualenv
    pkgs.python3Packages.pylint
  ];

  # Isso aqui roda toda vez que entrar no lab
  shellHook = ''
    echo "--- Laboratório de Python Ativado ---"
    python --version
  '';
}

