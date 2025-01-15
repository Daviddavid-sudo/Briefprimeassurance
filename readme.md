# Prédiction de Primes d'Assurance pour Assur’Aimant

## Description
Ce projet vise à développer une solution basée sur le machine learning pour prédire les primes d'assurance des clients d'Assur'Aimant, une compagnie d'assurance souhaitant s'implanter aux États-Unis. En exploitant des données démographiques et comportementales, cette solution remplace les estimations manuelles actuelles par une approche plus rapide, précise et rentable.

## Objectifs
1. Réaliser une analyse exploratoire des données pour mieux comprendre les caractéristiques des clients.
2. Créer un modèle de machine learning performant pour estimer les primes d'assurance.
3. Développer une application interactive pour générer des prédictions en temps réel.

## Structure du Projet

### 1. Analyse des Données
- Gestion des valeurs manquantes et des doublons.
- Détection des valeurs aberrantes.
- Analyse univariée et bivariée avec visualisations.
- Corrélations entre les variables explicatives et la variable cible.
- Validation d'hypothèses avec des tests statistiques.

### 2. Modélisation
- Comparaison de modèles de régression :
  - Régression linéaire.
  - Lasso, Ridge et ElasticNet.
- Pipelines de prétraitement pour la standardisation et l'encodage des variables.
- Optimisation des hyperparamètres via GridSearchCV et RandomSearchCV.
- Évaluation des modèles avec les métriques R² et RMSE.

### 3. Application Interactive
- Saisie des informations utilisateur via une interface Streamlit.
- Prédictions en temps réel grâce à un modèle exporté en format `.pkl`.

### 4. Présentation Finale
- Synthèse des résultats clés et des insights pour un public non technique.
- Démonstration en direct de l'application interactive.

## Données Utilisées
Le dataset contient les variables suivantes :
- **BMI** : Indice de masse corporelle.
- **Sex** : Genre du souscripteur (homme/femme).
- **Age** : Âge du souscripteur principal.
- **Children** : Nombre d'enfants à charge.
- **Smoker** : Statut fumeur/non-fumeur.
- **Region** : Zone résidentielle (Nord-Est, Sud-Est, Sud-Ouest, Nord-Ouest).
- **Charges** : Prime d'assurance facturée (cible).

## Prérequis
- Python 3.8 ou plus récent.
- Bibliothèques : pandas, numpy, seaborn, matplotlib, scikit-learn, Streamlit.

## Installation
1. Clonez le dépôt :
   ```bash
   git clone <URL-du-dépôt>
   ```
2. Accédez au répertoire du projet :
   ```bash
   cd <nom-du-répertoire>
   ```
3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
4. Lancez l'application Streamlit :
   ```bash
   streamlit run app.py
   ```

## Structure des Fichiers
- `data/` : Contient le dataset brut.
- `notebooks/` : Jupyter Notebooks pour l'analyse exploratoire et la modélisation.
- `models/` : Modèles exportés en format `.pkl`.
- `app.py` : Application Streamlit.
- `requirements.txt` : Liste des dépendances.

## Résultats
- Visualisations clés des variables et des relations avec les primes d'assurance.
- Performance des modèles évaluée avec R² et RMSE.
- Identification des variables les plus importantes pour la prédiction.

## Technologies Utilisées
- **Langages** : Python.
- **Bibliothèques** : pandas, numpy, seaborn, matplotlib, scikit-learn, Streamlit.
- **Outils** : GridSearchCV, RandomSearchCV, PolynomialFeatures.

## Auteur
Ce projet a été réalisé par Sami Kabdani et David Scott dans le cadre d'un brief pour la formation Développeur IA/DATA.

