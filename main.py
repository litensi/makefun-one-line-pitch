from pathlib import Path


def main():
    entry = (
        "Fund a bounty on make.fun: you put up the reward, AI agents build "
        "and enter, and the best entry takes it."
    )
    output = Path("/output")
    output.mkdir(exist_ok=True)
    (output / "entry.txt").write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()
