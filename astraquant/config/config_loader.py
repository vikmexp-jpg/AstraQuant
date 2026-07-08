from pathlib import Path
import yaml


class ConfigLoader:

    @staticmethod
    def load():
        # Project root
        project_root = Path(__file__).resolve().parents[2]

        config_path = project_root / "config" / "config.yaml"

        if not config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {config_path}"
            )

        with config_path.open("r", encoding="utf-8") as file:
            return yaml.safe_load(file)