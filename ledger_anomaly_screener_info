How to Use:
Prepare Your Ledger File: Ensure you have a ledger.csv file with at least the following columns:

Date: Date and time of the transaction (e.g., 2025-05-05 14:30:00)
Vendor: Name of the vendor
Amount: Transaction amount

Run the Script:
Save the script as ledger_anomaly_screener.py.
Open a terminal or command prompt.
Navigate to the directory containing the script.

Execute the script using:
bash
Copy
Edit
python ledger_anomaly_screener.py

Review the Output:
After execution, check the anomalies_report.csv file for the list of detected anomalies.

Notes:
Threshold Adjustment: The amount_threshold parameter in the detect_anomalies function is set to $10,000 by default. Adjust this value based on your organization's policies or typical transaction amounts.
Business Hours: The script considers payments made between 8 AM and 6 PM as standard business hours. Modify the detect_anomalies function if your business hours differ.
Date Format: Ensure that the Date column in your ledger.csv file is in a recognizable datetime format. If your dates are in a different format, you may need to adjust the parse_dates parameter in the load_ledger function.
