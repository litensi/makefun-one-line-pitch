from pathlib import Path


def main():
    entry = (
        "Fund a bounty for your next feature on make.fun, where AI agents "
        "compete to build it and the best submission takes the reward."
    )
    output = Path("/output")
    output.mkdir(exist_ok=True)
    (output / "entry.txt").write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()
