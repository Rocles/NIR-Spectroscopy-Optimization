from sklearn.ensemble import StackingRegressor, RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
import joblib

def train_and_evaluate_models(df, features, targets):
    results = {}
    
    X = df[features]
    
    for target in targets:
        y = df[target]
        
        # Division en ensembles d'entraînement et de test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Standardisation des caractéristiques
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # Création des modèles
        lr = LinearRegression()
        rf = RandomForestRegressor(n_estimators=100, random_state=42)
        gbr = GradientBoostingRegressor(n_estimators=100, random_state=42)
        
        # Entraînement des modèles
        lr.fit(X_train_scaled, y_train)
        rf.fit(X_train_scaled, y_train)
        gbr.fit(X_train_scaled, y_train)
        
        # Création du modèle de stacking
        estimators = [
            ('lr', lr),
            ('rf', rf),
            ('gbr', gbr)
        ]
        
        stacking_regressor = StackingRegressor(estimators=estimators, final_estimator=LinearRegression())
        stacking_regressor.fit(X_train_scaled, y_train)
        
        # Prédictions
        y_pred_lr = lr.predict(X_test_scaled)
        y_pred_rf = rf.predict(X_test_scaled)
        y_pred_gbr = gbr.predict(X_test_scaled)
        y_pred_stacking = stacking_regressor.predict(X_test_scaled)
        
        # Évaluation des modèles
        def evaluate_model(y_true, y_pred):
            mse = mean_squared_error(y_true, y_pred)
            r2 = r2_score(y_true, y_pred)
            return mse, r2
        
        mse_lr, r2_lr = evaluate_model(y_test, y_pred_lr)
        mse_rf, r2_rf = evaluate_model(y_test, y_pred_rf)
        mse_gbr, r2_gbr = evaluate_model(y_test, y_pred_gbr)
        mse_stacking, r2_stacking = evaluate_model(y_test, y_pred_stacking)
        
        # Stockage des résultats
        results[target] = {
            'Régression Linéaire': {'MSE': mse_lr, 'R2': r2_lr},
            'Forêt Aléatoire': {'MSE': mse_rf, 'R2': r2_rf},
            'Boosting Gradient': {'MSE': mse_gbr, 'R2': r2_gbr},
            'Stacking': {'MSE': mse_stacking, 'R2': r2_stacking}
        }
        
        # Sauvegarde du modèle de stacking pour chaque propriété chimique
        joblib.dump(stacking_regressor, f'stacking_model_{target}.pkl')
    
    return results
