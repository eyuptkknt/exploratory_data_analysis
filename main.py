import pandas as pd

# Load source data from a directory
file_path_new = "/mnt/data/*.csv"
df_new_sample = pd.read_csv(file_path_new)

# Convert the timestamp to datetime
df_new_sample['timestamp'] = pd.to_datetime(df_new_sample['timestamp'])

# Define core functions for the pipeline
def clean_data(df):
    # Impute missing values with the mean of the column (if any)
    df['power_output'] = df['power_output'].fillna(df['power_output'].mean())

    # Remove outliers outside of 3 standard deviations
    mean = df['power_output'].mean()
    std = df['power_output'].std()
    df = df[(df['power_output'] >= mean - 3 * std) & (df['power_output'] <= mean + 3 * std)]

    return df

def calculate_summary_statistics(df):
    summary = df.groupby('turbine_id')['power_output'].agg(['min', 'max', 'mean']).reset_index()
    summary.rename(columns={'min': 'min_output', 'max': 'max_output', 'mean': 'avg_output'}, inplace=True)
    return summary

def identify_anomalies(df):
    anomalies = []
    for turbine_id, group in df.groupby('turbine_id'):
        mean = group['power_output'].mean()
        std = group['power_output'].std()
        outliers = group[(group['power_output'] < mean - 2 * std) | (group['power_output'] > mean + 2 * std)]
        if not outliers.empty:
            anomalies.append({'turbine_id': turbine_id, 'anomaly_count': len(outliers)})
    return pd.DataFrame(anomalies)

# Process the new data 
cleaned_data_new = clean_data(df_sample)
summary_statistics_new = calculate_summary_statistics(cleaned_data)
anomalies_new = identify_anomalies(cleaned_data)

# Display results
print("Cleaned Data (Sample):")
print(cleaned_data.head())

print("\nSummary Statistics:")
print(summary_statistics)

print("\nAnomalies:")
print(anomalies)
