from collectors.http import HTTPCollector
from fingerprinting.http_parser import HTTPParser

collector = HTTPCollector()

evidence = collector.collect(
    "10.0.9.5",
    80,
    "http"
)

parser = HTTPParser()

result = parser.parse(evidence.banner)

print(result)
