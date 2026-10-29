# Vérifications réalisées

- Windows, Python 3.13.1 : exactement **9 tests réussis** (5 prix, 4 API).
- Rapports séparés `prix.xml` et `api.xml` générés ; `coverage.xml` généré avec la suite API, couverture de `app.py` : **96 %**.
- Sabotage réel, multiplication remplacée temporairement par une addition : **4 échecs, 5 réussites**, code de sortie pytest 1. Multiplication rétablie, puis **9 réussites** avant le commit.
- Docker Desktop Linux : `docker compose -p campus-cafe up -d --build` exécuté avec succès. Serveur Waitress accessible sur le port 5000 ; Python du conteneur : **3.12.16**.
- `smoke.py` exécuté avec succès contre le conteneur : `status=ok`, `build=local`, nom de machine du conteneur.

## À vérifier dans l’atelier

- Python 3.12 n’est pas installé sur cet hôte Windows : les tests locaux ont donc utilisé 3.13. Le conteneur a été construit et démarré sous Python 3.12.
- Aucun contrôleur Jenkins de l’atelier n’est connecté ici. L’exécution réelle du Jenkinsfile, l’affectation par `AGENT_LABEL`, les deux branches parallèles, la publication JUnit et le blocage de livraison dans Jenkins restent à vérifier sur le contrôleur commun.
- Vérifier la transmission du numéro de build depuis Jenkins et l’accès réseau depuis un autre PC selon le pare-feu local.
