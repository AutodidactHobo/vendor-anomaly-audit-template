import pandas as pd
import numpy as np
from datetime import datetime

def load_ledger(file_path):
    """
    Load the ledger CSV file into a pandas DataFrame.
    """
    try:
        df = pd.read_csv(file_path, parse_dates=['Date'])
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def detect_anomalies(df, amount_threshold=10000):
    """
    Detect anomalies in the ledger DataFrame.
    """
    anomalies = pd.DataFrame()

    # 1. Duplicate Transactions: Same Vendor, Amount, and Date
    duplicates = df[df.duplicated(subset=['Vendor', 'Amount', 'Date'], keep=False)]
    duplicates['Anomaly'] = 'Duplicate Transaction'
    anomalies = pd.concat([anomalies, duplicates])

    # 2. High-Value Transactions
    high_value = df[df['Amount'] > amount_threshold]
    high_value['Anomaly'] = 'High-Value Transaction'
    anomalies = pd.concat([anomalies, high_value])

    # 3. Payments Outside Business Hours (Assuming 8 AM to 6 PM)
    df['Hour'] = df['Date'].dt.hour
    off_hours = df[(df['Hour'] < 8) | (df['Hour'] > 18)]
    off_hours['Anomaly'] = 'Off-Hours Payment'
    anomalies = pd.concat([anomalies, off_hours])

    # Remove duplicate anomaly entries
    anomalies = anomalies.drop_duplicates()

    # Drop the 'Hour' column if it exists
    if 'Hour' in anomalies.columns:
        anomalies = anomalies.drop(columns=['Hour'])

    return anomalies

def save_anomalies(anomalies, output_path):
    """
    Save the anomalies DataFrame to a CSV file.
    """
    try:
        anomalies.to_csv(output_path, index=False)
        print(f"Anomalies saved to {output_path}")
    except Exception as e:
        print(f"Error saving anomalies: {e}")

def main():
    input_file = 'ledger.csv'  # Replace with your input file path
    output_file = 'anomalies_report.csv'  # Replace with your desired output file path

    df = load_ledger(input_file)
    if df is not None:
        anomalies = detect_anomalies(df)
        if not anomalies.empty:
            save_anomalies(anomalies, output_file)
        else:
            print("No anomalies detected.")
    else:
        print("Failed to process ledger.")

if __name__ == "__main__":
    main()
