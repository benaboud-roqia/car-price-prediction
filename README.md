# Interface de Prédiction de Prix de Voiture

Cette application permet de prédire le prix d'une voiture en fonction de ses caractéristiques.

## Fonctionnalités

- Interface web simple et intuitive
- Prédiction en temps réel du prix de la voiture
- Supporte plusieurs marques et types de carburant

## Installation

1. Installez les dépendances nécessaires :
```bash
pip install -r requirements.txt
```

2. Entraînez et sauvegardez le modèle (à exécuter une seule fois) :
```bash
python save_model.py
```

## Utilisation

1. Démarrez l'application :
```bash
python app.py
```

2. Ouvrez votre navigateur et allez à l'adresse :
```
http://127.0.0.1:5000
```

3. Remplissez le formulaire avec les informations de la voiture :
   - Année de fabrication
   - Kilométrage
   - Marque de la voiture
   - Type de carburant

4. Cliquez sur "Prédire le prix" pour obtenir une estimation

## Structure du projet

- `app.py` : Application Flask principale
- `save_model.py` : Script pour entraîner et sauvegarder le modèle
- `templates/index.html` : Interface utilisateur
- `requirements.txt` : Dépendances du projet
- `car_price_model.pkl` : Modèle entraîné (généré automatiquement)
- `company_mapping.pkl` : Mapping des marques (généré automatiquement)
- `fuel_mapping.pkl` : Mapping des carburants (généré automatiquement)

## Personnalisation

Pour utiliser votre propre jeu de données :

1. Modifiez le script `save_model.py` pour charger vos données réelles
2. Exécutez à nouveau `python save_model.py` pour mettre à jour le modèle

Auteur :
BENABOUD ROQIA etudiante master AI &SD
AMANI OUAHDANI  etudiante master architecture distribuee
