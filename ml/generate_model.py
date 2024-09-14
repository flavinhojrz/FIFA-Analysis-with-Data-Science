def create_training_model():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt 
    import seaborn as sns
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import RandomizedSearchCV
    from sklearn.metrics import r2_score
    import joblib

    df = pd.read_csv('../data/male_players.csv', low_memory=False)
    fifa_df = df[df['fifa_version'] <= 23]
    # df.head()

    fifa_df.isnull().sum()

    fifa_df = fifa_df.dropna(subset=['overall', 'potential', 'value_eur'])

    fifa_df['growth_potential'] = fifa_df['potential'] - fifa_df['overall']

    fifa_df = fifa_df[['overall', 'potential', 'growth_potential', 'age', 'pace', 'shooting', 
            'passing', 'dribbling', 'defending', 'physic', 'international_reputation',
            'club_position', 'league_name', 'nationality_name', 'work_rate', 
            'release_clause_eur', 'value_eur']]

    # Definir X (features) e y (target)
    X = fifa_df.drop(columns='value_eur')
    y = fifa_df['value_eur']

    # Dividir em treino e teste (80% treino, 20% teste)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    X_train = X_train.select_dtypes(include=['float64', 'int64'])
    X_test = X_test.select_dtypes(include=['float64', 'int64'])

    # Definir o modelo base
    rf = RandomForestRegressor(random_state=42)

    # Definir os hiperparâmetros a serem ajustados
    param_grid = {
        'n_estimators': [100, 200],  
        'max_depth': [10, 20, None],  
        'min_samples_split': [2, 5],  
        'min_samples_leaf': [1, 2],   
        'bootstrap': [True]          
    }

    random_search = RandomizedSearchCV(estimator=rf, param_distributions=param_grid,
                                    n_iter=10, 
                                    cv=5, random_state=42, n_jobs=-1, verbose=2)

    # Ajustar o modelo
    random_search.fit(X_train, y_train)

    # Melhor modelo encontrado
    model = random_search.best_estimator_

    # Criando modelo
    joblib.dump(model, 'model.pk')
    print("Create model!")


def main():
    create_training_model()
    
if __name__ == "__main__":
    main()