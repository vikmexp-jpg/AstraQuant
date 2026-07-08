from pathlib import Path

import yaml


class ConfigLoader:

    @staticmethod
    def load():

        config_path = Path(__file__).resolve().parents[2] / "config.yaml"

        with open(config_path, "r") as file:

            return yaml.safe_load(file)