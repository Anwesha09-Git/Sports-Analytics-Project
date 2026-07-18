import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("archive/database.sqlite")

query = """
SELECT
    team_long_name,
    SUM(Wins) AS Total_Wins
FROM (
    SELECT
        T.team_long_name,
        COUNT(*) AS Wins
    FROM Match M
    JOIN Team T
    ON M.home_team_api_id = T.team_api_id
    WHERE M.home_team_goal > M.away_team_goal
    GROUP BY T.team_long_name

    UNION ALL

    SELECT
        T.team_long_name,
        COUNT(*) AS Wins
    FROM Match M
    JOIN Team T
    ON M.away_team_api_id = T.team_api_id
    WHERE M.away_team_goal > M.home_team_goal
    GROUP BY T.team_long_name
)
GROUP BY team_long_name
ORDER BY Total_Wins DESC
LIMIT 10;
"""

df = pd.read_sql_query(query, conn)

plt.figure(figsize=(10,6))
plt.bar(df["team_long_name"], df["Total_Wins"])
plt.title("Top 10 Teams with Most Wins")
plt.xlabel("Team")
plt.ylabel("Total Wins")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("screenshots/top10_wins.png", dpi=300, bbox_inches="tight")
print("Image saved successfully!")

plt.show()

conn.close()