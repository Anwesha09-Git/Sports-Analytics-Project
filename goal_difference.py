import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("archive/database.sqlite")

query = """
SELECT
    T.team_long_name,

    SUM(
        CASE
            WHEN M.home_team_api_id = T.team_api_id THEN M.home_team_goal
            WHEN M.away_team_api_id = T.team_api_id THEN M.away_team_goal
        END
    ) -

    SUM(
        CASE
            WHEN M.home_team_api_id = T.team_api_id THEN M.away_team_goal
            WHEN M.away_team_api_id = T.team_api_id THEN M.home_team_goal
        END
    ) AS Goal_Difference

FROM Match M
JOIN Team T
ON T.team_api_id IN (M.home_team_api_id, M.away_team_api_id)

GROUP BY T.team_long_name
ORDER BY Goal_Difference DESC
LIMIT 10;
"""

df = pd.read_sql_query(query, conn)

plt.figure(figsize=(10,6))
plt.bar(df["team_long_name"], df["Goal_Difference"])

plt.title("Top 10 Teams by Goal Difference")
plt.xlabel("Team")
plt.ylabel("Goal Difference")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(
    "screenshots/top10_goal_difference.png",
    dpi=300,
    bbox_inches="tight"
)

print("Image saved successfully!")

plt.show()

conn.close()