import requests
from prometheus_client.parser import text_string_to_metric_families

response = requests.get("http://euclid:9100/metrics")
for family in text_string_to_metric_families(response.text):
    for sample in family.samples:
        #print("Name: {0} Labels: {1} Value: {2}".format(*sample))
        print(sample)