"""Entry writer for real-life-patch-notes comedy changelog."""

from pathlib import Path

ENTRY = "v2.4.1: Fixed a bug where the brain replayed embarrassing moments from 2009 at 3 AM instead of sleeping."


def main():
    target_path = Path("/output/entry.txt")
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
