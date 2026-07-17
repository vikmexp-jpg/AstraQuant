from pathlib import Path
import gzip
import shutil
import requests


class InstrumentDownloader:

    UPSTOX_URL = (
        "https://assets.upstox.com/market-quote/instruments/exchange/complete.json.gz"
    )

    def download(self, destination: Path):

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        print("Downloading Instrument Master...")

        response = requests.get(
            self.UPSTOX_URL,
            stream=True,
            timeout=60,
        )

        response.raise_for_status()

        with open(destination, "wb") as fp:
            for chunk in response.iter_content(8192):
                fp.write(chunk)

        print("Download completed.")

    def extract(
        self,
        gz_file: Path,
        json_file: Path,
    ):

        print("Extracting...")

        with gzip.open(gz_file, "rb") as fin:
            with open(json_file, "wb") as fout:
                shutil.copyfileobj(fin, fout)

        print("Extraction completed.")