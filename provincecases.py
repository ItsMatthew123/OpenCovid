import requests, json

url = "https://api.opencovid.ca/other?stat=prov"
response = requests.get(url)
data = json.loads(response.text)

# print(data['prov'])

for province in data['prov']:
    if province['pop'] != "NULL":
        print(province['province'], ":", province['pop'])
        # print({}: {:.0f}.format(province['province'], province['pop']))

# with open("covidcases.json", "w") as w_file:
#     json.dump(data, w_file)

# with open("covidcases.json", "r") as r_file:
#     data = json.load(r_file)

# print(data)
# print(data["summary"][0]["active_cases"])