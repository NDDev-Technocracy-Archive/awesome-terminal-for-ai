set shell := ["bash", "-euo", "pipefail", "-c"]

# Lists the commands.
default:
    @just --list

# Prepares only the frozen project lint dependency without package lifecycle scripts.
setup:
    bun install --cwd .github/quality --frozen-lockfile --ignore-scripts

# Checks shell syntax, tracked documents, spelling and command formatting offline.
check:
    just --fmt --check
    zsh -f -n configs/zsh/.zshenv
    zsh -f -n configs/zsh/.zprofile
    zsh -f -n configs/zsh/.zshrc
    python3 -B tools/check_docs.py
    typos

# Checks the existing live documentation links on the CI executor.
test:
    python3 -B tools/check_docs.py --online-links

# Runs complete source and documentation verification.
verify: check test
