#!/usr/bin/env python3
"""List comic pages in filename-defined natural reading order."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff"}


def natural_key(path: Path) -> list[tuple[int, object]]:
    parts = re.split(r"(\d+)", path.name.casefold())
    return [(0, int(part)) if part.isdigit() else (1, part) for part in parts]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Print storyboard image files in natural filename order."
    )
    parser.add_argument("directory", type=Path, help="Directory containing page images")
    args = parser.parse_args()

    directory = args.directory.expanduser().resolve()
    if not directory.is_dir():
        print(f"error: not a directory: {directory}", file=sys.stderr)
        return 2

    pages = sorted(
        (
            path
            for path in directory.iterdir()
            if path.is_file()
            and not path.name.startswith(".")
            and path.suffix.casefold() in IMAGE_EXTENSIONS
        ),
        key=natural_key,
    )
    if not pages:
        print(f"error: no supported page images in {directory}", file=sys.stderr)
        return 2

    numeric_pages: list[int] = []
    all_numeric = True
    seen: dict[int, Path] = {}
    duplicate = False

    print("sequence\tpage_label\tfilename\tpath")
    for sequence, path in enumerate(pages, start=1):
        stem = path.stem
        if stem.isdigit():
            number = int(stem)
            numeric_pages.append(number)
            if number in seen:
                duplicate = True
                print(
                    f"error: duplicate numeric page {number}: {seen[number].name}, {path.name}",
                    file=sys.stderr,
                )
            seen[number] = path
            label = str(number)
        else:
            all_numeric = False
            label = stem
        print(f"{sequence}\t{label}\t{path.name}\t{path}")

    if all_numeric and numeric_pages:
        first, last = min(numeric_pages), max(numeric_pages)
        missing = sorted(set(range(first, last + 1)) - set(numeric_pages))
        if first != 1:
            print(f"warning: numeric page sequence starts at {first}, not 1", file=sys.stderr)
        if missing:
            print(
                "warning: missing numeric page labels: " + ", ".join(map(str, missing)),
                file=sys.stderr,
            )

    return 2 if duplicate else 0


if __name__ == "__main__":
    raise SystemExit(main())
