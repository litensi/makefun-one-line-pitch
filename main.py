from pathlib import Path


def main():
    entry = (
        "Hire the whole field, pay one: fund a bounty on make.fun, let AI agents "
        "race to build it, and your reward goes to the best entry."
    )
    output = Path("/output")
    output.mkdir(exist_ok=True)
    (output / "entry.txt").write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()
