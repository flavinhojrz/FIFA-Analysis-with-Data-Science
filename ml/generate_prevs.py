def generate_prevs():
    import pandas as pd
    import joblib
    
    data = pd.read_csv('../data/male_players.csv', low_memory=False)
    model = joblib.load('./model.pk')

    data.isnull().sum()

    print('Tratando dados..\n')
    male_players = data[data['fifa_version'] >= 24]
    male_players['growth_potential'] = male_players['potential'] - male_players['overall']

    selected_columns =['short_name', 'overall', 'potential', 'growth_potential', 'age', 'pace', 
                        'shooting', 'passing', 'dribbling', 'defending', 'physic', 
                        'international_reputation', 'club_position', 'league_name', 
                        'nationality_name', 'work_rate', 'release_clause_eur', 'value_eur']

    male_players = male_players[selected_columns]
    male_players = male_players.dropna()

    print('Fazendo previsões...\n')
    # Fazer previsões
    male_players_predictions = model.predict(
        male_players.drop(columns=['club_position', 'league_name', 'nationality_name', 'work_rate', 'short_name', 'value_eur'])
    )

    male_players['predicted_value_eur'] = male_players_predictions

    male_players['predicted_value_eur'] = male_players['predicted_value_eur'].apply(lambda x: f"{x:,.0f} €")
    male_players['value_eur'] = male_players['value_eur'].apply(lambda x: f"{x:,.0f} €")
    male_players['release_clause_eur'] = male_players['release_clause_eur'].apply(lambda x: f"{x:,.0f} €")

    print('Previsões feitas!\n')
    male_players[['short_name','overall', 'potential', 'growth_potential', 'age', 'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic', 'predicted_value_eur', 'value_eur']].nlargest(20, 'growth_potential')
    print(male_players)
    
def main():
    generate_prevs()
    
if __name__ == "__main__":
    main()