import argparse

from astraquant.constants import APP_NAME, APP_VERSION

def banner():
    print("=" * 60)
    print(f"{APP_NAME} {APP_VERSION}")
    print("=" * 60)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", default="app",
                        choices=["app","backtest"])
    args = parser.parse_args()

    banner()

    if args.mode == "backtest":
        print("Historical Backtesting module is ready.")
        print("Next milestone will connect the CSV loader")
        print("to the DIDRS strategy and produce trade reports.")
    else:
        print("Application mode started.")

if __name__ == "__main__":
    main()
