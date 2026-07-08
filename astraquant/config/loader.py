from pathlib import Path
import yaml

def load_config(path=None):
    path = path or Path(__file__).parent/'config.yaml'
    with open(path,'r',encoding='utf-8') as f:
        return yaml.safe_load(f)
