import csv

import pandas as pd
from collections import Counter

# Load the data
data = pd.read_csv('data/Dataset.csv')

# Helper functions to analyze the data
def most_common_visitor(data):
    return "Females" if data['Is Female'].sum() > data['Is Male'].sum() else "Males"

def count_by_feature(data, feature):
    return data[feature].sum()

def most_common_cluster(data):
    return data['Cluster ID'].mode().iloc[0]

def visitor_counts(data):
    return data['Cluster ID'].value_counts()

# Generate questions and answers
questions_and_answers = [
    ["Who is my most common visitor?", f"Your most common visitors are {most_common_visitor(data)}."],
    ["How many male visitors do I have?", f"You have {count_by_feature(data, 'Is Male')} male visitors."],
    ["How many female visitors do I have?", f"You have {count_by_feature(data, 'Is Female')} female visitors."],
    ["How many visitors wear hijabs?", f"{count_by_feature(data, 'Is Hijab')} visitors wear hijabs."],
    ["How many child visitors do I have?", f"You have {count_by_feature(data, 'Is Child')} child visitors."],
    ["How many visitors wear niqabs?", f"{count_by_feature(data, 'Is Niqab')} visitors wear niqabs."],
    ["How many visitors have bags?", f"{count_by_feature(data, 'Has Bag')} visitors have bags."],
    ["Which cluster has the most visitors?", f"Cluster {most_common_cluster(data)} has the most visitors."],
    ["How many visitors are in cluster 35?", f"Cluster 35 has {visitor_counts(data)[35]} visitors."],
    ["How many visitors are in cluster 36?", f"Cluster 36 has {visitor_counts(data)[36]} visitors."],
    # Additional questions to reach 50
    ["How many visitors are in cluster 37?", f"Cluster 37 has {visitor_counts(data)[37]} visitors."],
    ["How many visitors are in cluster 38?", f"Cluster 38 has {visitor_counts(data)[38]} visitors."],
    ["How many visitors are in cluster 39?", f"Cluster 39 has {visitor_counts(data)[39]} visitors."],
    ["How many visitors are in cluster 40?", f"Cluster 40 has {visitor_counts(data)[40]} visitors."],
    ["How many visitors are in cluster 41?", f"Cluster 41 has {visitor_counts(data)[41]} visitors."],
    ["How many visitors are in cluster 42?", f"Cluster 42 has {visitor_counts(data)[42]} visitors."],
    ["How many visitors are in cluster 43?", f"Cluster 43 has {visitor_counts(data)[43]} visitors."],
    ["How many visitors are in cluster 44?", f"Cluster 44 has {visitor_counts(data)[44]} visitors."],
    ["How many visitors are in cluster 45?", f"Cluster 45 has {visitor_counts(data)[45]} visitors."],
    ["How many visitors are in cluster 46?", f"Cluster 46 has {visitor_counts(data)[46]} visitors."],
    ["How many visitors are in cluster 47?", f"Cluster 47 has {visitor_counts(data)[47]} visitors."],
    ["How many visitors are in cluster 48?", f"Cluster 48 has {visitor_counts(data)[48]} visitors."],
    ["How many visitors are in cluster 49?", f"Cluster 49 has {visitor_counts(data)[49]} visitors."],
    ["How many visitors are in cluster 50?", f"Cluster 50 has {visitor_counts(data)[50]} visitors."],
    ["How many visitors are in cluster 51?", f"Cluster 51 has {visitor_counts(data)[51]} visitors."],
    ["Which cluster has the fewest visitors?", f"Cluster {visitor_counts(data).idxmin()} has the fewest visitors."],
    ["What is the total number of visitors?", f"The total number of visitors is {len(data)}."],
    ["What is the percentage of female visitors?", f"The percentage of female visitors is {(count_by_feature(data, 'Is Female') / len(data)) * 100:.2f}%."],
    ["What is the percentage of male visitors?", f"The percentage of male visitors is {(count_by_feature(data, 'Is Male') / len(data)) * 100:.2f}%."],
    ["How many visitors arrived between 14:30 and 14:40?", f"{len(data[(data['Time'] >= '17/07/2024 14:30') & (data['Time'] <= '17/07/2024 14:40')])} visitors arrived between 14:30 and 14:40."],
    ["How many visitors arrived between 14:40 and 14:50?", f"{len(data[(data['Time'] >= '17/07/2024 14:40') & (data['Time'] <= '17/07/2024 14:50')])} visitors arrived between 14:40 and 14:50."],
    ["How many visitors arrived between 14:50 and 15:00?", f"{len(data[(data['Time'] >= '17/07/2024 14:50') & (data['Time'] <= '17/07/2024 15:00')])} visitors arrived between 14:50 and 15:00."],
    ["How many visitors arrived between 15:00 and 15:10?", f"{len(data[(data['Time'] >= '17/07/2024 15:00') & (data['Time'] <= '17/07/2024 15:10')])} visitors arrived between 15:00 and 15:10."],
    ["How many visitors arrived between 15:10 and 15:20?", f"{len(data[(data['Time'] >= '17/07/2024 15:10') & (data['Time'] <= '17/07/2024 15:20')])} visitors arrived between 15:10 and 15:20."],
    ["How many visitors arrived after 15:20?", f"{len(data[data['Time'] > '17/07/2024 15:20'])} visitors arrived after 15:20."],
    ["How many visitors with hijabs are in cluster 35?", f"{len(data[(data['Cluster ID'] == 35) & (data['Is Hijab'] == 1)])} visitors with hijabs are in cluster 35."],
    ["How many visitors with niqabs are in cluster 35?", f"{len(data[(data['Cluster ID'] == 35) & (data['Is Niqab'] == 1)])} visitors with niqabs are in cluster 35."],
    ["How many visitors with bags are in cluster 35?", f"{len(data[(data['Cluster ID'] == 35) & (data['Has Bag'] == 1)])} visitors with bags are in cluster 35."],
    ["How many child visitors are in cluster 35?", f"{len(data[(data['Cluster ID'] == 35) & (data['Is Child'] == 1)])} child visitors are in cluster 35."],
    ["How many male visitors are in cluster 35?", f"{len(data[(data['Cluster ID'] == 35) & (data['Is Male'] == 1)])} male visitors are in cluster 35."],
    ["How many female visitors are in cluster 35?", f"{len(data[(data['Cluster ID'] == 35) & (data['Is Female'] == 1)])} female visitors are in cluster 35."],
    ["How many female visitors with hijabs are there?", f"{len(data[(data['Is Female'] == 1) & (data['Is Hijab'] == 1)])} female visitors with hijabs are there."],
    ["How many female visitors with niqabs are there?", f"{len(data[(data['Is Female'] == 1) & (data['Is Niqab'] == 1)])} female visitors with niqabs are there."],
    ["How many female visitors with bags are there?", f"{len(data[(data['Is Female'] == 1) & (data['Has Bag'] == 1)])} female visitors with bags are there."],
    ["How many female child visitors are there?", f"{len(data[(data['Is Female'] == 1) & (data['Is Child'] == 1)])} female child visitors are there."],
    ["How many male visitors with hijabs are there?", f"{len(data[(data['Is Male'] == 1) & (data['Is Hijab'] == 1)])} male visitors with hijabs are there."],
    ["How many male visitors with niqabs are there?", f"{len(data[(data['Is Male'] == 1) & (data['Is Niqab'] == 1)])} male visitors with niqabs are there."],
    ["How many male visitors with bags are there?", f"{len(data[(data['Is Male'] == 1) & (data['Has Bag'] == 1)])} male visitors with bags are there."],
    ["How many male child visitors are there?", f"{len(data[(data['Is Male'] == 1) & (data['Is Child'] == 1)])} male child visitors are there."],
]

# Convert to DataFrame
qa_df = pd.DataFrame(questions_and_answers, columns=["Question", "Answer"])

# Save to CSV
qa_df.to_csv('data.csv', index=False)

# data = [
    # ["How many records are there?", "📊 Total records: 60"],
    # ["How many males are in the dataset?", "👨 Count of males: 3"],
    # ["How many females are in the dataset?", "👩 Count of females: 57"],
    # ["How many records have a person wearing a hijab?", "🧕 Hijab count: 36"],
    # ["How many children are in the dataset?", "🧒 Count of children: 1"],
    # ["How many records have a person wearing a niqab?", "👩‍🦳 Niqab count: 4"],
    # ["How many records have a person carrying a bag?", "👜 Bag count: 8"],
    # ["What is the total number of unique clusters?", "🔢 Unique clusters: 17"],
    # ["Which cluster ID has the most records?", "🏆 Cluster ID 36 with 9 records"],
    # ["Which cluster ID has the least records?", "🔻 Cluster ID 35 with 3 records"],
    # ["What is the timestamp of the first record?", "⏱️ First record timestamp: 17/07/2024 14:30"],
    # ["What is the timestamp of the last record?", "⏱️ Last record timestamp: 17/07/2024 15:12"],
    # ["How many records are between 14:30 and 15:00?", "🕰️ Records between 14:30 and 15:00: 38"],
    # ["How many records are after 15:00?", "🕰️ Records after 15:00: 22"],
    # ["What is the total number of males in cluster ID 36?", "👨 Total males in cluster 36: 1"],
    # ["What is the total number of females in cluster ID 36?", "👩 Total females in cluster 36: 8"],
    # ["How many records have both a hijab and a bag?", "🧕👜 Hijab and bag count: 1"],
    # ["How many records have a female wearing a niqab?", "👩‍🦳 Female with niqab count: 4"],
    # ["How many records have a child?", "🧒 Total child records: 1"],
    # ["Which cluster IDs have records with a child?", "🔍 Cluster IDs with child: 36"],
    # ["How many records have a person with a bag in cluster ID 38?", "👜 Bag count in cluster 38: 1"],
    # ["How many unique timestamps are in the dataset?", "📅 Unique timestamps: 28"],
    # ["Which timestamp appears the most in the dataset?", "⏱️ Most frequent timestamp: 17/07/2024 14:33 (5 times)"],
    # ["How many records are there for cluster ID 37?", "🔢 Total records for cluster 37: 3"],
    # ["What is the average number of records per cluster?", "📊 Average records per cluster: ~3.53"],
    # ["How many records are there in the dataset for 17/07/2024 14:45?", "⏰ Records at 14:45: 3"],
    # ["How many records have a person wearing a hijab and carrying a bag?", "🧕👜 Hijab and bag count: 1"],
    # ["What is the count of records for 17/07/2024 14:58?", "⏰ Records at 14:58: 3"],
    # ["How many records do not have any males?", "👨🚫 Male absent records: 57"],
    # ["How many records do not have any females?", "👩🚫 Female absent records: 3"],
    # ["What is the count of records for cluster ID 45?", "🔢 Cluster 45 count: 2"],
    # ["Which cluster IDs have a person carrying a bag?", "🔍 Clusters with bags: 36, 38, 39, 41, 42, 43, 46, 50"],
    # ["What is the total number of records for clusters with a person carrying a bag?", "📊 Total records with bags: 8"],
    # ["How many records have a person wearing a hijab and no bag?", "🧕🚫👜 Hijab without bag count: 35"],
    # ["What is the count of records for cluster ID 50?", "🔢 Cluster 50 count: 4"],
    # ["How many records have timestamps between 14:45 and 15:00?", "🕰️ Records between 14:45 and 15:00: 18"],
    # ["What is the count of records for 17/07/2024 14:33?", "⏰ Records at 14:33: 5"],
    # ["How many records have a timestamp of 17/07/2024 15:12?", "⏰ Records at 15:12: 5"],
    # ["Which cluster IDs have the most records?", "🏆 Clusters with most records: 36 (9)"],
    # ["What is the count of records for cluster ID 39?", "🔢 Cluster 39 count: 2"],
    # ["How many records have a person with a niqab in cluster ID 50?", "👩‍🦳 Niqab count in cluster 50: 1"],
    # ["How many records have timestamps after 14:50?", "🕰️ Records after 14:50: 23"],
    # ["What is the count of records for 17/07/2024 14:50?", "⏰ Records at 14:50: 2"],
    # ["What is the count of records for cluster ID 48?", "🔢 Cluster 48 count: 4"],
    # ["How many records have a person wearing a hijab in cluster ID 36?", "🧕 Hijab count in cluster 36: 6"],
    # ["How many records have a person with a bag in cluster ID 39?", "👜 Bag count in cluster 39: 1"],
    # ["What is the count of records for cluster ID 43?", "🔢 Cluster 43 count: 3"],
    # ["How many records have a person wearing a hijab and a niqab?", "🧕👩‍🦳 Hijab and niqab count: 4"],
    # ["How many records have a timestamp between 14:45 and 15:15?", "🕰️ Records between 14:45 and 15:15: 28"],
    # ["How many records have a timestamp of 17/07/2024 14:46?", "⏰ Records at 14:46: 3"],
    # ["What is the count of records for cluster ID 41?", "🔢 Cluster 41 count: 4"],
    # ["How many records have a person with a hijab and carrying a bag?", "🧕👜 Hijab and bag count: 1"],
    # ["What is the count of records for cluster ID 42?", "🔢 Cluster 42 count: 3"],
    # ["What is the count of records for cluster ID 44?", "🔢 Cluster 44 count: 4"],
    # ["How many records have a timestamp between 14:30 and 14:50?", "🕰️ Records between 14:30 and 14:50: 30"],
    # ["How many records have a timestamp between 14:50 and 15:10?", "🕰️ Records between 14:50 and 15:10: 25"],
    # ["What is the count of records for cluster ID 47?", "🔢 Cluster 47 count: 3"],
    # ["How many records have a person with a hijab and no bag?", "🧕🚫👜 Hijab without bag count: 35"],
    # ["How many records have a timestamp of 17/07/2024 14:42?", "⏰ Records at 14:42: 2"],
    # ["How many records have a person with a hijab and no niqab?", "🧕🚫👩‍🦳 Hijab without niqab count: 32"],
    # ["What is the count of records for cluster ID 46?", "🔢 Cluster 46 count: 3"],
    # ["How many records have a person with a niqab in cluster ID 43?", "👩‍🦳 Niqab count in cluster 43: 1"],
    # ["How many records have a timestamp between 14:30 and 14:40?", "🕰️ Records between 14:30 and 14:40: 6"],
    # ["What is the count of records for cluster ID 35?", "🔢 Cluster 35 count: 3"],
    # ["How many records have a person with a hijab and a bag in cluster ID 50?", "🧕👜 Hijab and bag count in cluster 50: 1"],
    # ["How many records have a person wearing a hijab in cluster ID 36?", "🧕 Hijab count in cluster 36: 6"],
    # ["How many records have a timestamp between 14:30 and 14:45?", "🕰️ Records between 14:30 and 14:45: 21"],
    # ["How many records have a timestamp of 17/07/2024 14:36?", "⏰ Records at 14:36: 2"],
    # ["What is the count of records for cluster ID 48?", "🔢 Cluster 48 count: 5"],
    # ["How many records have a person with a hijab and carrying a bag in cluster ID 41?", "🧕👜 Hijab and bag count in cluster 41: 1"],
    # ["What is the count of records for cluster ID 49?", "🔢 Cluster 49 count: 7"],
    # ["How many records have a person with a hijab and carrying a bag in cluster ID 38?", "🧕👜 Hijab and bag count in cluster 38: 1"],
    # ["How many records have a timestamp between 14:30 and 15:00?", "🕰️ Records between 14:30 and 15:00: 39"],
    # ["What is the count of records for cluster ID 46?", "🔢 Cluster 46 count: 3"],
    # ["How many records have a person with a hijab and a niqab in cluster ID 50?", "🧕👩‍🦳 Hijab and niqab count in cluster 50: 1"],
    # ["How many records have a timestamp of 17/07/2024 14:44?", "⏰ Records at 14:44: 1"],
    # ["How many records have a timestamp of 17/07/2024 14:45?", "⏰ Records at 14:45: 3"],
    # ["What is the count of records for cluster ID 44?", "🔢 Cluster 44 count: 4"],
    # ["How many records have a timestamp between 14:30 and 14:45?", "🕰️ Records between 14:30 and 14:45: 21"],
    # ["How many records have a timestamp of 17/07/2024 15:01?", "⏰ Records at 15:01: 2"],
    # ["How many records have a timestamp of 17/07/2024 14:58?", "⏰ Records at 14:58: 3"],
    # ["What is the count of records for cluster ID 45?", "🔢 Cluster 45 count: 2"],
    # ["How many records have a person with a hijab in cluster ID 47?", "🧕 Hijab count in cluster 47: 2"],
    # ["How many records have a timestamp of 17/07/2024 15:12?", "⏰ Records at 15:12: 2"],
    # ["How many records have a timestamp of 17/07/2024 14:55?", "⏰ Records at 14:55: 5"],
    # ["What is the count of records for cluster ID 51?", "🔢 Cluster 51 count: 1"],
    # ["How many records have a person with a hijab and carrying a bag in cluster ID 49?", "🧕👜 Hijab and bag count in cluster 49: 0"],
    # ["How many records have a timestamp of 17/07/2024 14:54?", "⏰ Records at 14:54: 3"],
    # ["How many records have a timestamp of 17/07/2024 14:56?", "⏰ Records at 14:56: 2"],
    # ["What is the count of records for cluster ID 47?", "🔢 Cluster 47 count: 2"],
    # ["How many records have a person with a hijab and carrying a bag in cluster ID 44?", "🧕👜 Hijab and bag count in cluster 44: 0"],
    # ["How many records have a person with a hijab and a niqab in cluster ID 36?", "🧕👩‍🦳 Hijab and niqab count in cluster 36: 1"],
    # ["How many records have a timestamp between 14:45 and 15:15?", "🕰️ Records between 14:45 and 15:15: 28"],
    # ["What is the count of records for cluster ID 43?", "🔢 Cluster 43 count: 3"],
    # ["How many records have a person with a hijab and carrying a bag in cluster ID 42?", "🧕👜 Hijab and bag count in cluster 42: 0"],
    # ["How many records have a timestamp of 17/07/2024 14:51?", "⏰ Records at 14:51: 1"],
    # ["How many records have a timestamp of 17/07/2024 14:33?", "⏰ Records at 14:33: 5"],
    # ["What is the count of records for cluster ID 35?", "🔢 Cluster 35 count: 3"],
    # ["How many records have a timestamp of 17/07/2024 14:40?", "⏰ Records at 14:40: 1"],
    # ["How many records have a person with a hijab and carrying a bag in cluster ID 36?", "🧕👜 Hijab and bag count in cluster 36: 0"],
    # ["How many records have a timestamp of 17/07/2024 14:42?", "⏰ Records at 14:42: 2"],
    # ["How many records have a timestamp of 17/07/2024 14:46?", "⏰ Records at 14:46: 2"],
    # ["What is the count of records for cluster ID 38?", "🔢 Cluster 38 count: 4"],
    # ["How many records have a person with a hijab and carrying a bag in cluster ID 41?", "🧕👜 Hijab and bag count in cluster 41: 1"],
    # ["How many records have a timestamp between 14:30 and 15:00?", "🕰️ Records between 14:30 and 15:00: 30"],
    # ["What is the count of records for cluster ID 49?", "🔢 Cluster 49 count: 5"],
    # ["How many records have a person with a hijab and carrying a bag in cluster ID 50?", "🧕👜 Hijab and bag count in cluster 50: 1"],
    # ["How many records have a timestamp of 17/07/2024 15:03?", "⏰ Records at 15:03: 2"],
    # ["How many records have a timestamp of 17/07/2024 14:58?", "⏰ Records at 14:58: 3"],
    # ["What is the count of records for cluster ID 45?", "🔢 Cluster 45 count: 2"],
    # ["How many records have a person with a hijab in cluster ID 47?", "🧕 Hijab count in cluster 47: 2"],
    # ["How many records have a timestamp of 17/07/2024 15:12?", "⏰ Records at 15:12: 2"],
    # ["How many records have a timestamp of 17/07/2024 14:55?", "⏰ Records at 14:55: 2"],
    # ["What is the count of records for cluster ID 51?", "🔢 Cluster 51 count: 2"],
    # ["How many records have a person with a hijab and carrying a bag in cluster ID 44?", "🧕👜 Hijab and bag count in cluster 44: 0"],
    # ["How many records have a person with a hijab and a niqab in cluster ID 36?", "🧕👩‍🦳 Hijab and niqab count in cluster 36: 1"]
# ]

# # Define the file path
# file_path = '/data/prompts_responses.csv'

# # Write the data to a CSV file
# with open(file_path, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Prompt", "Response"])  # Write header
#     writer.writerows(data)  # Write data

# file_path
