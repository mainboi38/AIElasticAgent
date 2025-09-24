from elasticsearch import Elasticsearch

# Connect to your local Elasticsearch
es = Elasticsearch("http://localhost:9200")

# Define explicit mappings
mapping = {
  "mappings": {
    "properties": {
      "duration": { "type": "long" },
      "protocol_type": { "type": "keyword" },
      "service": { "type": "keyword" },
      "label": { "type": "keyword" },
      "Indicator": { "type": "keyword" },
      "Action": { "type": "keyword" },
      "Severity": { "type": "keyword" },
      "timestamp": { "type": "date" }
    }
  }
}

# Create the index (ignore=400 means skip if already exists)
es.indices.create(index="network-logs", body=mapping, ignore=400)

print("Index created with correct mappings.")
