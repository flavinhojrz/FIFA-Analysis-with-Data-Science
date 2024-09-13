# FIFA 24 Player Data Analysis

This project provides an analysis of football (soccer) players using a dataset related to FIFA 24. The project includes functions to filter players by country, team, position, and potential, along with visualizations of player positions and nationalities.

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
  - [Visualizations](#visualizations)
- [How to Run](#how-to-run)
- [Requirements](#requirements)
- [File Structure](#file-structure)
- [Acknowledgments](#acknowledgments)

## Project Overview
This project analyzes the characteristics of players included in FIFA 24, such as their positions, overall rating, potential, and more. Several functions are implemented to filter players based on different attributes, and the analysis is accompanied by visualizations that provide insights into the distribution of players across different positions and nationalities.

## Dataset
The dataset used in this project is called `male_players.csv` and includes various attributes of players from FIFA 24, such as:
- `short_name`: Player's name.
- `overall`: Player's overall rating.
- `potential`: Player's potential rating.
- `player_positions`: The positions a player can play in.
- `nationality_name`: Player's nationality.
- `club_name`: Club the player belongs to.
- `value_eur`: Player's market value in euros.

## Functions and Features

### Get Players by Country
This function retrieves the top 10 players from a specified country, sorted by their overall rating.

### Get Players by Team
This function retrieves players from a specified club, displaying details such as age, value, jersey number, and overall rating.

### Get High Potential Players
This function lists young players (under 21) with high potential and a difference of at least 5 points between their current overall rating and potential.

### List All Positions
Lists all unique positions that players in the dataset can play.

### Get Players by Position
Retrieves players who play a specified position.

### Get Best Players by Position
Fetches the top 10 players by overall rating for a specific position.

### Visualizations
Count of Players by Position
This plot shows the count of players for various football positions, such as CAM, CB, CM, GK, and ST.
Nations Participating in FIFA 24
This bar plot visualizes the top 80 nations participating in FIFA 24 based on the number of players

### How to Run
- Clone the repository.
- Ensure you have the required Python packages installed (see below).
- Place the male_players.csv dataset in the archive folder.
- Execute the provided Jupyter notebook or Python scripts to explore player data and generate visualizations.

### Requirements
- Python 3.12+
- pandas
- numpy
- seaborn
- matplotlib

### To install the required dependencies, run:
```bash
  pip install pandas numpy seaborn matplotlib
```

### Acknowledgments
- Dataset provided by Kaggle. Special thanks to the contributors who compiled the FIFA 24 dataset.

### Key Additions:
- **File Structure**: Added a clear structure to give users an overview of the project’s file organization.
  
Let me know if you'd like any additional changes!
