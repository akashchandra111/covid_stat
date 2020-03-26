import http.client
import json
import requests

connection = http.client.HTTPSConnection("coronavirus-monitor.p.rapidapi.com")
	
headers =	{
	'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
	'x-rapidapi-key': "e1b2a0ba45mshb461b67d726c622p194592jsn98cad9e4187f"
}

def ret_json(country, date):
	query_string =	{
		'country': country,
		'date': date
	}
	
	return requests.request("GET", "https://coronavirus-monitor.p.rapidapi.com/coronavirus/history_by_country_and_date.php", headers=headers, params=query_string).json()

def ret_world_cases():
	return requests.request("GET", "https://coronavirus-monitor.p.rapidapi.com/coronavirus/worldstat.php", headers=headers).json()
