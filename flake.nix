{
  description = "";

  # Flake inputs
  inputs = {
    nixpkgs.url = "https://flakehub.com/f/NixOS/nixpkgs/0.2405.*.tar.gz";
    nixpkgs-python.url = "github:cachix/nixpkgs-python";
  };

  # Flake outputs
  outputs = { self, nixpkgs, nixpkgs-python }:
    let
      # Systems supported
      allSystems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];

      # Helper to provide system-specific attributes
      forAllSystems = f: nixpkgs.lib.genAttrs allSystems (system: f {
        pkgs = import nixpkgs { inherit system; };
      });
    in
    {
      # Development environment output
      devShells = forAllSystems ({ pkgs }: {
        default =
          let
            python = nixpkgs-python.packages.${pkgs.system}."3.10.11";

            # https://github.com/jetify-com/devbox/issues/1276#issuecomment-1894983364
            poetryLibs = [
              pkgs.stdenv.cc.cc.lib
              pkgs.zlib
            ];
            poetry = pkgs.symlinkJoin {
              name = "poetry";
              paths = [ pkgs.poetry ];
              buildInputs = [ pkgs.makeWrapper ];
              postBuild = ''
                wrapProgram $out/bin/poetry --set LD_LIBRARY_PATH ${nixpkgs.lib.makeLibraryPath poetryLibs}
              '';
            };

          in
          pkgs.mkShell {
            packages = [
              pkgs.bashInteractive
              poetry
              (python.withPackages (ps: with ps; [
                virtualenv
                pip
              ]))
            ];
          };
      });
    };
}
