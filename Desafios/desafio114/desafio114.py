import requests
from modules.cores import creturn


def checkSite(url="https://www.google.com/"):
    try:
        result = requests.get(url)

        print(f"A url {url} está {creturn('Online', 'green')}")
    except requests.exceptions.SSLError:
        print(f"A url {url} é {creturn('insegura', 'red')}")
    except Exception:
        print(f"A url {url} está {creturn('Offline', 'red')}")


checkSite("https://www.pudim.com.br/")
