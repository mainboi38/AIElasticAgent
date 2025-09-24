import pandas as pd
import json

# Load the CSV
file_path = "./updated_cybersecurity_attacks.csv"
df = pd.read_csv(file_path)

# Function to map CSV fields → your desired schema
def to_bulk_format(row):
    return [
        {"index": {"_index": "network-logs"}},   # bulk action line
        {
            "duration": int(row.get("Packet Length", 0)),  # using Packet Length as duration
            "protocol_type": row.get("Protocol", "").lower(),
            "service": row.get("Traffic Type", "").lower(),
            "label": row.get("Attack Type", "").lower(),
            "Indicator": row.get("Malware Indicators", "").lower(),
            "Action": row.get("Action Taken", "").lower(),
            "Severity": row.get("Severity Level").lower()
        },
    ]

# Build up records in bulk JSONL format
records = []
for _, row in df.iterrows():
    records.extend(to_bulk_format(row))

# Save to JSONL
output_path = "./network_logs_bulk.jsonl"
with open(output_path, "w") as f:
    for rec in records:
        f.write(json.dumps(rec) + "\n")

print(f"Saved bulk JSONL file at {output_path}")
