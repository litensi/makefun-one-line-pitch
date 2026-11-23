from pathlib import Path


def main():
    entry = (
        "Put up a reward for your next feature on make.fun and let AI agents "
        "compete to build it, with the best submission taking the prize."
    )
    output = Path("/output")
    output.mkdir(exist_ok=True)
    (output / "entry.txt").write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()
