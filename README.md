
---

# FIFA 24 Player Data Analysis & Market Value Prediction

This project provides an in-depth analysis of football players from FIFA 24. It includes functions for filtering players by country, team, position, and potential, along with visualizations of player positions and nationalities. Additionally, the project features a machine learning model that predicts player market values based on attributes such as overall rating, potential, and physical/technical skills.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Functions and Features](#functions-and-features)
  - [Get Players by Country](#get-players-by-country)
  - [Get Players by Team](#get-players-by-team)
  - [Get High Potential Players](#get-high-potential-players)
  - [List All Positions](#list-all-positions)
  - [Get Players by Position](#get-players-by-position)
  - [Get Best Players by Position](#get-best-players-by-position)
  - [Predict Player Market Value](#predict-player-market-value)
  - [Visualizations](#visualizations)
- [Machine Learning Model](#machine-learning-model)
- [How to Run](#how-to-run)
- [Requirements](#requirements)
- [File Structure](#file-structure)
- [Acknowledgments](#acknowledgments)

## Project Overview
This project analyzes key player characteristics in FIFA 24, such as their positions, overall rating, potential, and more. It also includes a machine learning model that predicts player market values, enabling insights into the financial worth of players based on their attributes.

## Dataset
The dataset used for this project is `male_players.csv` and contains various attributes of FIFA 24 players, including:
- `short_name`: Player's name.
- `overall`: Player's overall rating.
- `potential`: Player's potential rating.
- `player_positions`: The positions a player can play.
- `nationality_name`: Player's nationality.
- `club_name`: Club the player belongs to.
- `value_eur`: Player's market value in euros.
  
Additional columns, such as player performance metrics (`pace`, `shooting`, etc.), are also included.

## Functions and Features

### Get Players by Country
Retrieve the top 10 players from a specific country, sorted by their overall rating.

### Get Players by Team
Retrieve players from a specific club, displaying details such as age, market value, jersey number, and overall rating.

### Get High Potential Players
Lists young players (under 21) with high potential, highlighting players with at least a 5-point gap between their overall rating and potential.

### List All Positions
Lists all unique positions that players in the dataset can play.

### Get Players by Position
Retrieve players who play a specific position, offering flexibility in filtering by player roles.

### Get Best Players by Position
Fetch the top 10 players by overall rating for any given position.

### Predict Player Market Value
Predict a player's market value based on attributes such as:
- Overall rating
- Potential rating
- Physical and technical attributes (pace, shooting, passing, etc.)
This functionality uses a machine learning model trained on real-world FIFA player data.

### Visualizations
- **Count of Players by Position**: Displays the distribution of players across various football positions (e.g., CAM, CB, ST).
- **Top Nations in FIFA 24**: Visualizes the top 80 nations with the highest number of players participating in FIFA 24.

## Machine Learning Model
The machine learning model is designed to predict the market value of players. The model was trained using a Random Forest Regressor, fine-tuned with hyperparameter optimization to achieve strong performance:
- **Train R²**: 0.9915
- **Test R²**: 0.9627

### Model Inputs
The model takes the following features:
- `overall`, `potential`, `growth_potential`
- Key performance metrics like pace, shooting, dribbling, passing, etc.
- Age, international reputation, and release clause.

### How to Run
1. Clone the repository.
2. Place the `male_players.csv` dataset in the `data` folder.
3. Install the required dependencies (see below).
4. Execute the Jupyter notebook or Python scripts to analyze data and predict player values.

### Requirements
- Python 3.12+
- pandas
- numpy
- seaborn
- matplotlib
- scikit-learn

Install the required dependencies:
```bash
pip install pandas numpy seaborn matplotlib scikit-learn
```

## File Structure
```
FIFA24-Player-Analysis/
│
├── data/
│   └── male_players.csv      
├── notebooks/
│   └── analysis.ipynb       
├── ml/
│   └── model.ipynb  
└── README.md
```

## Acknowledgments
- Dataset provided by Kaggle. Special thanks to the contributors who compiled the FIFA 24 dataset.
---
