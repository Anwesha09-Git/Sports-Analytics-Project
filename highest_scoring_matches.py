import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("archive/database.sqlite")

query = """
SELECT
    date,
    home_team_goal,
    away_team_goal,
    (home_team_goal + away_team_goal) AS Total_Goals
FROM Match
ORDER BY Total_Goals DESC
LIMIT 10;
"""

df = pd.read_sql_query(query, conn)

plt.figure(figsize=(10,6))

plt.bar(
    [f"Match {i+1}" for i in range(len(df))],
    df["Total_Goals"]
)

plt.title("Top 10 Highest Scoring Matches")
plt.xlabel("Matches")
plt.ylabel("Total Goals")

plt.tight_layout()

plt.savefig(
    "screenshots/top10_highest_scoring_matches.png",
    dpi=300,
    bbox_inches="tight"
)

print("Image saved successfully!")

plt.show()

conn.close()