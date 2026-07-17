from pathlib import Path

from astraquant.instruments.downloader import (
    InstrumentDownloader,
)

root = Path(__file__).resolve().parents[1]

gz_file = (
    root
    / "astraquant"
    / "data"
    / "instruments"
    / "upstox.json.gz"
)

json_file = gz_file.with_suffix("")

downloader = InstrumentDownloader()

downloader.download(gz_file)

downloader.extract(
    gz_file,
    json_file,
)

print()

print("Saved to")

print(json_file)