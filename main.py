from astraquant.constants import APP_NAME, APP_VERSION
from astraquant.startup import bootstrap

def banner():
    print("="*60)
    print(f"{APP_NAME} {APP_VERSION}")
    print("="*60)

if __name__=="__main__":
    banner()
    bootstrap()
