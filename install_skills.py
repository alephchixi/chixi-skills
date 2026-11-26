#!/usr/bin/env python3
"""Copy complete Ch’ixi skill folders to a host's chosen discovery directory."""

import argparse
from pathlib import Path
from shutil import copytree

SKILLS = Path(__file__).resolve().parent / "skills"


def install(target, names):
    if target.resolve() == SKILLS:
        raise ValueError("Use a host discovery directory outside the source skills.")
    pending = []
    for name in names:
        source, destination = SKILLS / name, target / name
        if destination.is_symlink():
            raise FileExistsError(f"Conflict at {destination}")
        if destination.exists():
            source_files = {p.relative_to(source): p for p in source.rglob("*") if p.is_file()}
            for entry in destination.rglob("*"):
                relative = entry.relative_to(destination)
                original = source / relative
                if entry.is_symlink() or (
                    entry.is_dir() and not original.is_dir()
                ) or (
                    not entry.is_dir()
                    and (relative not in source_files or entry.read_bytes() != original.read_bytes())
                ):
                    raise FileExistsError(f"Conflict at {entry}")
            if not destination.is_dir():
                raise FileExistsError(f"Conflict at {destination}")
        pending.append((source, destination))
    target.mkdir(parents=True, exist_ok=True)
    for source, destination in pending:
        copytree(source, destination, dirs_exist_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path)
    available = sorted(p.name for p in SKILLS.iterdir() if (p / "SKILL.md").is_file())
    parser.add_argument("names", nargs="*", metavar="SKILL", help=", ".join(available))
    args = parser.parse_args()
    names = args.names or available
    if unknown := sorted(set(names) - set(available)):
        parser.error(f"Unknown skills: {', '.join(unknown)}")
    try:
        install(args.target, names)
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")
    print(f"Installed {len(set(names))} skills in {args.target}")


if __name__ == "__main__":
    main()
