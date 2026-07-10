from astraquant import __application__, __version__


def main() -> None:
    print("=" * 60)
    print(f"{__application__} {__version__}")
    print("=" * 60)
    print("Project Skeleton Loaded Successfully")


if __name__ == "__main__":
    main()