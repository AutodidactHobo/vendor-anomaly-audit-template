# Standard Operating Procedure (SOP): Vendor Payment Fraud Investigation

## Purpose
To provide a standardized method for detecting, investigating, and responding to potential vendor payment fraud.

## Scope
Applies to all vendor transactions processed through accounting, ERP, or procurement systems.

## Trigger Events
- Unusual payment timing (weekends, after-hours)
- Duplicate payment amounts
- Rapidly added or modified vendor accounts
- Mismatched invoice metadata

## Step-by-Step Process

### 1. Data Collection
- Extract ledger data from NetSuite, SAP, or QBO
- Include: Vendor ID, Invoice #, Payment Date, Payment Amount, Entry Creator

### 2. Pattern Screening
- Use Python, SQL, or Excel to flag:
  - Duplicate amounts within 30-day windows
  - Payments to new vendors > $5,000
  - Off-cycle transactions

### 3. Cross-Check Metadata
- Validate vendor existence (OpenCorporates, SAM.gov)
- Match EIN to known records
- Check for prior complaints, sanctions, or red flags

### 4. Document Findings
- Populate investigation worksheet (see `vendor_recon_sample.xlsx`)
- Label each issue as: False Positive, Inconclusive, Fraud Suspected

### 5. Report & Escalate
- Summarize case in audit report
- Escalate confirmed anomalies to compliance/legal
- Update SOP based on new findings

## Tools Used
- NetSuite, SAP, QuickBooks
- Python (Pandas), SQL
- OSINT platforms: Pipl, OpenCorporates, WHOIS

## Last Reviewed
April 2025
