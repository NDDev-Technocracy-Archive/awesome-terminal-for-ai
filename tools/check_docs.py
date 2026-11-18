"""Check this repository's tracked documentation without walking tool caches."""

import argparse
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--online-links", action="store_true")
    args = parser.parse_args()
    raw = subprocess.check_output(["git", "ls-files", "-z", "--", "*.md"], cwd=ROOT)
    documents = ["./" + path for path in raw.decode("utf-8").split("\0") if path]
    if not documents:
        raise SystemExit("no tracked documentation to check")
    if args.online_links:
        command = ["lychee", "--no-progress", "--max-concurrency", "8", *documents]
        subprocess.run(command, cwd=ROOT, check=True)
        return
    cli = ROOT / ".github/quality/node_modules/.bin/markdownlint-cli2"
    subprocess.run([str(cli), *documents], cwd=ROOT, check=True)
    subprocess.run(["lychee", "--offline", "--no-progress", *documents], cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
