import yaml
import requests
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

with open("/etc/prometheus/prometheus.yml", "r") as stream:
    yaml_data = yaml.safe_load(stream)

all_jobs = requests.get("http://galileo.gb.nrao.edu:9090/api/v1/label/__name__/values")
job_names = all_jobs.json()['data']

q1 = {
	"query": "Weather_Weather1_S_weather1",
	"start": 1698788638,
	"end": 1701207838,
	"step": 9676,
    }

url = "http://galileo.gb.nrao.edu:9090/api/v1/query_range"
response = requests.get(url, q1)
plt.figure()
for m in response.json()['data']['result']:
    name = m['metric']['name']
    x = [m['values'][i][0] for i in range(np.shape(m['values'])[0])]
    y = [float(m['values'][i][1]) for i in range(np.shape(m['values'])[0])]
    plt.plot(x, y, label=name)
plt.xlabel('timestamp')
plt.legend()
plt.show()