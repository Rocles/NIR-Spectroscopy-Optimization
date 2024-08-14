Le projet est organisé comme suit :

data/ : Contient les fichiers de données brutes.
chemical_analysis.xlsx : Le fichier Excel contenant les données chimiques.
notebooks/ : Contient les notebooks Jupyter pour l'analyse exploratoire et la visualisation des données.
NIR_Spectroscopy_Analysis.ipynb : Notebook principal pour l'analyse des données et l'expérimentation avec les modèles.
src/ : Contient les scripts Python pour le traitement des données, la visualisation, l'entraînement des modèles et les fonctions utilitaires.
__init__.py : Fichier pour rendre le répertoire src un package Python.
data_preprocessing.py : Script pour le prétraitement des données (imputation, encodage).
data_visualization.py : Script pour la visualisation des distributions et des matrices de corrélation.
model_training.py : Script pour l'entraînement et l'évaluation des modèles de régression.
utils.py : Script pour les fonctions utilitaires telles que l'affichage des résultats.
requirements.txt : Liste des dépendances nécessaires pour exécuter le projet.
README.md : Ce fichier, contenant des informations sur le projet.
.gitignore : Liste des fichiers et répertoires à ignorer par Git.