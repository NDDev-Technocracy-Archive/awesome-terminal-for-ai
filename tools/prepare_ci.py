"""Provide zsh on the GitHub-hosted Ubuntu runner."""

import os
import shutil
import subprocess


def main() -> None:
    if shutil.which("zsh"):
        return
    if os.environ.get("RUNNER_ENVIRONMENT") != "github-hosted":
        raise SystemExit("Install zsh through your system package manager before running the checks.")
    subprocess.run(["sudo", "apt-get", "update", "-q"], check=True)
    subprocess.run(
        ["sudo", "apt-get", "install", "-y", "-q", "--no-install-recommends", "zsh"],
        check=True,
    )


if __name__ == "__main__":
    main()
