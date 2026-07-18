import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("archive/database.sqlite")

query = """
SELECT
    HT.team_long_name,
    COUNT(*) AS Matches_Played
FROM Match M
JOIN Team HT
ON M.home_team_api_id = HT.team_api_id
GROUP BY HT.team_long_name
ORDER BY Matches_Played DESC
LIMIT 10;
"""

df = pd.read_sql_query(query, conn)

plt.figure(figsize=(10,6))
plt.bar(df["team_long_name"], df["Matches_Played"])
plt.title("Top 10 Teams by Home Matches Played")
plt.xlabel("Team")
plt.ylabel("Matches Played")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(
    "screenshots/top10_home_matches.png",
    dpi=300,
    bbox_inches="tight",
    format="png"
)

print("Image saved successfully!")

plt.show()
plt.close()

conn.close()