
import streamlit as st
import pandas as pd
import sqlite3

# Connect to the database
conn = sqlite3.connect("sql/nextgen.db")

# Load data from the database
applicants = pd.read_sql_query("SELECT * FROM applicants;", conn)
interns = pd.read_sql_query("SELECT * FROM interns;", conn)
scores = pd.read_sql_query("SELECT * FROM hackathon_scores;", conn)

# Dashboard title
st.title("NextGen Internship Dashboard")
st.write("Explore applicant, internship, and hackathon performance data.")

# Domain filter
domain_list = ["All"] + sorted(
    applicants["domain_applied"].dropna().unique().tolist()
)

selected_domain = st.selectbox("Filter by Domain", domain_list)

# Filter the tables based on the selected domain
if selected_domain != "All":
    applicants_filtered = applicants[
        applicants["domain_applied"] == selected_domain
    ]

    interns_filtered = interns[
        interns["domain"] == selected_domain
    ]

    scores_filtered = scores[
        scores["domain"] == selected_domain
    ]
else:
    applicants_filtered = applicants
    interns_filtered = interns
    scores_filtered = scores


# Section 1: Internship Funnel
st.header("Internship Funnel")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label="Total Applicants",
        value=len(applicants_filtered)
    )

with col2:
    st.metric(
        label="Total Interns",
        value=len(interns_filtered)
    )


# Section 2: Completion Rate per Domain
st.header("Completion Rate per Domain")

completion_query = """
SELECT
    a.domain_applied AS domain,
    COUNT(DISTINCT a.applicant_id) AS total_applicants,
    COUNT(DISTINCT i.intern_id) AS total_completed,
    ROUND(
        100.0 * COUNT(DISTINCT i.intern_id)
        / COUNT(DISTINCT a.applicant_id),
        2
    ) AS completion_rate_pct
FROM applicants a
LEFT JOIN interns i
    ON a.applicant_id = i.applicant_id
    AND i.completion_status = 'Completed'
GROUP BY a.domain_applied
ORDER BY completion_rate_pct DESC;
"""

completion_data = pd.read_sql_query(completion_query, conn)

# Apply the selected domain filter
if selected_domain != "All":
    completion_data = completion_data[
        completion_data["domain"] == selected_domain
    ]

st.bar_chart(
    completion_data,
    x="domain",
    y="completion_rate_pct"
)


# Section 3: Average Hackathon Score per Domain
st.header("Average Hackathon Score per Domain")

score_query = """
SELECT
    domain,
    ROUND(AVG(score), 2) AS average_score
FROM hackathon_scores
GROUP BY domain
ORDER BY average_score DESC;
"""

average_scores = pd.read_sql_query(score_query, conn)

# Apply the selected domain filter
if selected_domain != "All":
    average_scores = average_scores[
        average_scores["domain"] == selected_domain
    ]

st.bar_chart(
    average_scores,
    x="domain",
    y="average_score"
)


# Section 4: Top 10 Hackathon Performers
st.header("Top 10 Hackathon Performers")

leaderboard_query = """
SELECT
    i.intern_id,
    a.applicant_name,
    i.domain,
    hs.score
FROM hackathon_scores hs
JOIN interns i
    ON hs.intern_id = i.intern_id
JOIN applicants a
    ON i.applicant_id = a.applicant_id
"""

# Apply domain filtering before selecting the top 10
if selected_domain != "All":
    leaderboard_query += " WHERE i.domain = ?"

leaderboard_query += """
ORDER BY hs.score DESC
LIMIT 10;
"""

if selected_domain != "All":
    leaderboard = pd.read_sql_query(
        leaderboard_query,
        conn,
        params=(selected_domain,)
    )
else:
    leaderboard = pd.read_sql_query(
        leaderboard_query,
        conn
    )

st.dataframe(leaderboard, use_container_width=True)

# Close database connection
conn.close()
