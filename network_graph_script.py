
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

# Reading the CSV data
data = pd.read_csv('/Users/galateaswart/Desktop/Practice Data.csv', header=0, delimiter=',')
print(data.head())

# Drop the first column
data = data.iloc[:, 1:]
print(data.head())

# Filter data for the period of 1950-1980
filtered_data = data[(data['year'] >= 1950) & (data['year'] <= 1980)]

# Select specific diseases
selected_diseases = ['Hepatitis A', 'Polio', 'Smallpox']
filtered_data = filtered_data[filtered_data['disease'].isin(selected_diseases)]

# Create a graph
G = nx.Graph()

# Create dictionaries to store aggregated data based on state names and years
# This will be used to reduce repeated labels on the graph
state_nodes = {}
year_nodes = {}

# Create sets to store unique diseases, states, and years
diseases = set(filtered_data['disease'])
states = set(filtered_data['state'])
years = set(filtered_data['year'])

# Add edges between diseases and states/years
for _, row in filtered_data.iterrows():
    disease = row['disease']
    state = row['state']
    year = row['year']

    # Add nodes and edges to the graph
    G.add_edge(disease, state)
    G.add_edge(disease, year)

    # Populate dictionaries to track unique states and years
    state_nodes[state] = 1
    year_nodes[year] = 1

# Assign colors to diseases
disease_colors = {
    'Hepatitis A': 'yellow',
    'Polio': 'lavender',
    'Smallpox': 'teal'
}

# Coloring nodes based on 'diseases' values
node_colors = [disease_colors.get(node, 'grey') for node in G.nodes()]

# Draw the graph
plt.figure(figsize=(20, 10))
# Get default position from spring layout
pos = nx.spring_layout(G)
nx.draw(G, pos=pos, with_labels=False, node_color=node_colors, font_size=10)

# Label aggregated nodes
for node, degree in G.degree():
    if node in state_nodes or node in year_nodes:
        plt.text(pos[node][0], pos[node][1], node, fontsize=10)

plt.savefig('/Users/galateaswart/Desktop/Network_Plot_Selected_Diseases.pdf', dpi=300)
plt.show()