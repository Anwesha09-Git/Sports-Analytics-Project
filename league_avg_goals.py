import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("archive/database.sqlite")

query = """
SELECT
    L.name AS League,
    ROUND(AVG(M.home_team_goal + M.away_team_goal), 2) AS Average_Goals
FROM Match M
JOIN League L
ON M.league_id = L.id
GROUP BY L.name
ORDER BY Average_Goals DESC;
"""

df = pd.read_sql_query(query, conn)

plt.figure(figsize=(12,6))

plt.bar(df["League"], df["Average_Goals"])

plt.title("Average Goals per Match by League")
plt.xlabel("League")
plt.ylabel("Average Goals")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig(
    "screenshots/league_average_goals.png",
    dpi=300,
    bbox_inches="tight"
)

print("Image saved successfully!")

plt.show()

conn.close()