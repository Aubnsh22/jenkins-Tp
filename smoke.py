"""Vérifie le service en 10 tentatives maximum, sans dépendance externe."""
import json
import time
from urllib.error import URLError
from urllib.request import urlopen


def main():
    for tentative in range(1, 11):
        try:
            with urlopen("http://127.0.0.1:5000/health", timeout=2) as response:
                data = json.load(response)
                if response.status == 200 and data.get("status") == "ok":
                    print(f"Smoke OK : {data}")
                    return 0
                raise ValueError("Réponse health invalide")
        except (URLError, OSError, ValueError) as erreur:
            print(f"Tentative {tentative}/10 : {erreur}")
            if tentative < 10:
                time.sleep(2)
    print("ÉCHEC : service indisponible après 10 tentatives.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
