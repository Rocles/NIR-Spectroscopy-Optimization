import pandas as pd

def load_data():
    """
    Charge un fichier Excel dans un DataFrame pandas.
    
    :return: DataFrame contenant les données du fichier Excel.
    """
    file_path = r'C:\\Users\\ADMIN\\Documents\\NIR_Spectroscopy_Optimization\\Data\\chemical_analysis.xlsx'
    try:
        df = pd.read_excel(file_path)
        print(f"Data loaded successfully from {file_path}")
        return df
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None
