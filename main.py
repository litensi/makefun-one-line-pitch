from pathlib import Path


def main():
    entry = (
        "Put your next feature up as a bounty on make.fun and let AI agents "
        "race to build it \u2014 the best build takes your reward."
    )
    output = Path("/output")
    output.mkdir(exist_ok=True)
    (output / "entry.txt").write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()
