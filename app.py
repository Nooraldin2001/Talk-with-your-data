import pandas as pd
from datetime import datetime
import spacy

# Load the dataset
df = pd.read_csv('data/Dataset.csv')

# Convert the 'Time' column to datetime
df['Time'] = pd.to_datetime(df['Time'])

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def process_query(query):
    # Parse the query using spaCy
    doc = nlp(query)
    
    # Extract key information from the query
    time_related = any(token.lemma_ in ["minute", "hour", "day", "time"] for token in doc)
    visitor_related = any(token.lemma_ in ["visitor", "people", "person", "male", "female", "child", "hijab", "niqab", "bag"] for token in doc)
    most_common = any(token.lemma_ in ["most", "common", "frequent"] for token in doc)
    count = any(token.lemma_ in ["count", "number"] for token in doc)
    cluster_related = any(token.lemma_ in ["cluster"] for token in doc)
    peak = any(token.lemma_ in ["peak"] for token in doc)
    average = any(token.lemma_ in ["average", "mean"] for token in doc)

    # Process the query based on extracted information
    if time_related and most_common and "minute" in query:
        return most_visitors_time()
    elif time_related and most_common and "hour" in query:
        return peak_visitors_hour()
    elif time_related and average and "hour" in query:
        return average_visitors_per_hour()
    elif visitor_related and most_common:
        return most_common_visitor()
    elif count and visitor_related:
        return count_visitors()
    elif cluster_related and count:
        return count_clusters()
    elif cluster_related and most_common:
        return most_common_cluster()
    else:
        return "I'm sorry, I couldn't understand the query. Please try rephrasing it."

def most_visitors_time():
    # Group by minute and count visitors
    visitors_per_minute = df.groupby(df['Time'].dt.floor('T')).size()
    max_visitors_time = visitors_per_minute.idxmax()
    return f"The minute with the most visitors was {max_visitors_time.strftime('%Y-%m-%d %H:%M')}"

def peak_visitors_hour():
    # Group by hour and count visitors
    visitors_per_hour = df.groupby(df['Time'].dt.floor('H')).size()
    max_visitors_hour = visitors_per_hour.idxmax()
    return f"The hour with the most visitors was {max_visitors_hour.strftime('%Y-%m-%d %H:%M')}"

def average_visitors_per_hour():
    # Group by hour and count visitors, then calculate the average
    visitors_per_hour = df.groupby(df['Time'].dt.floor('H')).size()
    average_visitors = visitors_per_hour.mean()
    return f"The average number of visitors per hour is {average_visitors:.2f}"

def most_common_visitor():
    # Determine the most common visitor type
    visitor_types = ['Is Male', 'Is Female', 'Is Hijab', 'Is Child', 'Is Niqab', 'Has Bag']
    visitor_counts = df[visitor_types].sum()
    most_common = visitor_counts.idxmax()
    return f"The most common visitor type is {most_common}"

def count_visitors():
    # Count the number of each type of visitor
    visitor_types = ['Is Male', 'Is Female', 'Is Hijab', 'Is Child', 'Is Niqab', 'Has Bag']
    visitor_counts = df[visitor_types].sum()
    return visitor_counts.to_string()

def count_clusters():
    # Count the number of unique clusters
    cluster_count = df['Cluster ID'].nunique()
    return f"There are {cluster_count} unique clusters"

def most_common_cluster():
    # Determine the most common cluster ID
    most_common_cluster = df['Cluster ID'].mode()[0]
    return f"The most common cluster ID is {most_common_cluster}"

def query_data():
    while True:
        query = input("Enter your question about the data (or 'quit' to exit): ")
        if query.lower() == 'quit':
            break
        response = process_query(query)
        print(f"Answer: {response}\n")

# Run the query interface
query_data()

# Example usage
# print(process_query("Which minute did I get the most visitors?"))
# print(process_query("Which hour did I get the peak visitors?"))
# print(process_query("What is the average number of visitors per hour?"))
# print(process_query("Who is my most common visitor?"))
# print(process_query("How many male visitors did I get?"))
# print(process_query("How many clusters are there?"))
# print(process_query("What is the most common cluster?"))