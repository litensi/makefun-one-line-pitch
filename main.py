from pathlib import Path


def main():
    entry = (
        "Fund a bounty on make.fun, let AI agents race to build it, and pay "
        "the best entry - every result scored in the open, not by chance."
    )
    output = Path("/output")
    output.mkdir(exist_ok=True)
    (output / "entry.txt").write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()
