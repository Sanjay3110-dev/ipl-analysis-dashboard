import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

deliveries = pd.read_csv('/Users/apple/Downloads/archive-2/deliveries_clean.csv')
matches = pd.read_csv('/Users/apple/Downloads/archive-2/matches_clean.csv')

# Chart 1: Runs per over
over_runs = deliveries.groupby('over')['total_runs'].mean()

plt.figure(figsize=(12, 5))
plt.bar(over_runs.index, over_runs.values, color='#FF6B35')
plt.xlabel('Over Number')
plt.ylabel('Average Runs per Over')
plt.title('IPL Run Rate by Over')
plt.tight_layout()
plt.savefig('runrate_by_over.png', dpi=150)
plt.show()

# Chart 2: Top 10 batsmen
batsman_runs = deliveries.groupby('batter')['batsman_runs'].sum()
top10 = batsman_runs.sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
top10.plot(kind='barh', color='#1E3A5F')
plt.xlabel('Total Runs')
plt.title('Top 10 Run Scorers in IPL History')
plt.tight_layout()
plt.savefig('top_batsmen.png', dpi=150)
plt.show()

# Chart 3: Season wins for top teams
top_teams = ['Mumbai Indians', 'Chennai Super Kings', 'Kolkata Knight Riders', 'Royal Challengers Bangalore']
season_wins = matches[matches['winner'].isin(top_teams)].groupby(['season', 'winner']).size().unstack(fill_value=0)

season_wins.plot(kind='bar', figsize=(14, 6))
plt.title('Season-wise Wins: Top 4 Teams')
plt.xlabel('Season')
plt.ylabel('Wins')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('season_wins.png', dpi=150)
plt.show()

print("Charts saved!")