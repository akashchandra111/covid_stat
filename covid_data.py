import http.client
import json
import requests

connection = http.client.HTTPSConnection("coronavirus-monitor.p.rapidapi.com")
	
headers =	{
	'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
	'x-rapidapi-key': "e1b2a0ba45mshb461b67d726c622p194592jsn98cad9e4187f"
}

def ret_json(country, date):
	#connection.request("GET", "/coronavirus/history_by_country_and_date.php?country={}&date={}".format(country, date), headers=headers)
	#response = connection.getresponse()
	#return json.loads(response.read().decode('utf-8'))
	query_string =	{
		'country': country,
		'date': date
	}
	
	return requests.request("GET", "https://coronavirus-monitor.p.rapidapi.com/coronavirus/history_by_country_and_date.php", headers=headers, params=query_string).json()

def ret_world_cases():
	#connection.request("GET", "/coronavirus/worldstat.php", headers=headers)
	#response = connection.getresponse()
	#return json.loads(response.read().decode('utf-8'))
	return requests.request("GET", "https://coronavirus-monitor.p.rapidapi.com/coronavirus/worldstat.php", headers=headers).json()

# Visualize JSON data
#print("INDIA COVID-19 STATS: (be safe)")

#for i in json_data['stat_by_country']:
#	print("Date: " + i['record_date'] + ", Total Cases: " + i['total_cases'] + ", New Cases: " + i['new_cases'] + ", Active Cases: " + i['active_cases'] + ", Total Deaths: " + i['total_deaths'] + ", New Deaths: " + i['new_deaths'] + ", Total Recovered: " + i['total_recovered'] + ", Serious: " + i['serious_critical'] + ", Total cases/million: " + i['total_cases_per1m'])
