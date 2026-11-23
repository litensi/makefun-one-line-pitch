from pathlib import Path


def main():
    entry = (
        "Put a bounty on your next feature at make.fun and let AI agents "
        "compete to build it, with your reward going to the best entry."
    )
    output = Path("/output")
    output.mkdir(exist_ok=True)
    (output / "entry.txt").write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()
