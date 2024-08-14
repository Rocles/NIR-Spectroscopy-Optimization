from data_loading import load_data
from data_preprocessing import preprocess_data
from data_visualization import plot_distributions, plot_correlation_matrix
from model_training import train_and_evaluate_models
from utils import print_results

def main():
    # Charger le dataset
    file_path = r'C:\\Users\\ADMIN\\Documents\\NIR_Spectroscopy_Optimization\\Data\\chemical_analysis.xlsx'
    df = load_data(file_path)
    
    # Visualiser les données
    plot_distributions(df, ['DM', 'NH4', 'N', 'CaO', 'K2O', 'MgO', 'P2O5'])
    plot_correlation_matrix(df)
    
    # Prétraiter les données
    df = preprocess_data(df)
    
    # Préparer les caractéristiques et les cibles
    features = ['type_manure', 'spectrometer', 'township', 'country']
    targets = ['DM', 'NH4', 'N', 'CaO', 'K2O', 'MgO', 'P2O5']
    
    # Entraîner et évaluer les modèles
    results = train_and_evaluate_models(df, features, targets)
    print_results(results)

if __name__ == '__main__':
    main()
