import pandas as pd
import ast
import numpy as np

# Read the CSV file
df = pd.read_csv('/Users/ardacakil/Desktop/projects/cr-sheets/data/BattlesStaging_01022021_WL_tagged.csv')

# Function to sort card list in descending order
def sort_card_list_desc(card_list_str):
    try:
        # Convert string representation of list to actual list
        card_list = ast.literal_eval(card_list_str)
        # Sort in descending order
        card_list.sort(reverse=True)
        # Convert back to string
        return str(card_list)
    except:
        # If there's any error, return original
        return card_list_str

# Apply sorting to both winner and loser card lists
df['winner.cards.list'] = df['winner.cards.list'].apply(sort_card_list_desc)
df['loser.cards.list'] = df['loser.cards.list'].apply(sort_card_list_desc)

# Select only the two columns we need
df_selected = df[['winner.cards.list', 'loser.cards.list']].copy()

# Function to convert deck list to a big number by concatenation
def deck_to_number(deck_str):
    try:
        deck_list = ast.literal_eval(deck_str)
        # Convert each card ID to string with 8 digits and concatenate
        number_str = ''.join([str(card_id).zfill(8) for card_id in deck_list])
        return number_str
    except:
        return '0'

# Convert decks to numbers (as strings for comparison)
df_selected['winner_num'] = df_selected['winner.cards.list'].apply(deck_to_number)
df_selected['loser_num'] = df_selected['loser.cards.list'].apply(deck_to_number)

# Create new dataframe with proper ordering
result_data = []
for index, row in df_selected.iterrows():
    if row['winner_num'] >= row['loser_num']:
        # Keep original order - but store as concatenated numbers
        result_data.append({
            'player1.cards.list': row['winner_num'],  # Store the big number
            'player2.cards.list': row['loser_num'],   # Store the big number
            'check': 0
        })
    else:
        # Flip the order
        result_data.append({
            'player1.cards.list': row['loser_num'],   # Store the big number
            'player2.cards.list': row['winner_num'],  # Store the big number
            'check': 1
        })

# Create final dataframe
df_final = pd.DataFrame(result_data)

# Sort by player1.cards.list in descending order
df_final = df_final.sort_values('player1.cards.list', ascending=False)

# Convert to numpy array
numpy_array = df_final.to_numpy()

# Save to CSV
df_final.to_csv('/Users/ardacakil/Desktop/projects/cr-sheets/data/data_modified1.csv', index=False)

print(f"Analysis complete!")
print(f"Total rows: {len(df_final)}")
print(f"Rows flipped: {df_final['check'].sum()}")
print(f"Data saved to: data_modified.csv")
print(f"\nNumPy array shape: {numpy_array.shape}")

# Show first few rows to verify
print("\nFirst 3 rows:")
for i in range(min(3, len(df_final))):
    print(f"Player1: {df_final.iloc[i]['player1.cards.list']}")
    print(f"Player2: {df_final.iloc[i]['player2.cards.list']}")
    print(f"Check: {df_final.iloc[i]['check']}\n")