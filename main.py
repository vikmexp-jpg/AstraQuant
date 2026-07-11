from astraquant.version import (
    APPLICATION_NAME,
    VERSION,
)


def main() -> None:
    print("=" * 60)
    print(f"{APPLICATION_NAME} {VERSION}")
    print("=" * 60)
    print("AQ-001 Project Skeleton Loaded Successfully")


if __name__ == "__main__":
    main()