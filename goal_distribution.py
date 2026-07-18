import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("archive/database.sqlite")

query = """
SELECT
(home_team_goal + away_team_goal) AS Total_Goals
FROM Match;
"""

df = pd.read_sql_query(query, conn)

plt.figure(figsize=(10,6))

plt.hist(df["Total_Goals"], bins=10)

plt.title("Distribution of Goals per Match")
plt.xlabel("Total Goals")
plt.ylabel("Number of Matches")

plt.tight_layout()

plt.savefig(
    "screenshots/goal_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

print("Image saved successfully!")

plt.show()

conn.close()