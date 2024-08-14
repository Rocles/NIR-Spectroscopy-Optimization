import seaborn as sns
import matplotlib.pyplot as plt

def plot_distributions(df, columns):
    for column in columns:
        plt.figure(figsize=(10, 5))
        sns.histplot(df[column].dropna(), kde=True)
        plt.title(f'Distribution of {column}')
        plt.show()

def plot_correlation_matrix(df):
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Matrix')
    plt.show()
