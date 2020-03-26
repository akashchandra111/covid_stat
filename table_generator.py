from covid_data import ret_json, ret_world_cases
import time

w_data = ret_world_cases()
data = ret_json(country='india', date=time.strftime('%Y-%m-%d', time.gmtime()))

def format_data(t):
	str_formatted = "<table border='1'> <tr> <th> Date </th> <th> Count </th> </tr>"
	
	for d in data['stat_by_country']:
		str_formatted += "<tr> <td> {} </td> <td> {} </td> </tr>".format(d['record_date'], d[t])
	
	str_formatted += "</table>"

	return str_formatted

def total_cases_html():
	return format_data('total_cases')
	
def new_cases_html():
	return format_data('new_cases')

def active_cases_html():
	return format_data('active_cases')

def total_deaths_html():
	return format_data('total_deaths')

def new_deaths_html():
	return format_data('new_deaths')

def total_recovery_html():
	return format_data('total_recovered')

def serious_html():
	return format_data('serious_critical')

def case_perm_html():
	return format_data('total_cases_per1m')

def ret_world_data_html():
	return '<table border="1"> <tr> <th>Total Cases</th> <th>Total Death</th> <th>Total Recovered</th> <th>New Cases</th> <th>New Deaths</th> <th>Statistics Updated At</th> </tr> <tr> <td>{}</td> <td>{}</td> <td>{}</td> <td>{}</td> <td>{}</td> <td>{}</td> </tr> </table> </br>'.format(w_data['total_cases'], w_data['total_deaths'], w_data['total_recovered'], w_data['new_cases'], w_data['new_deaths'], w_data['statistic_taken_at'])

def refresh_data():
	global w_data
	global data

	try:
		w_data = ret_world_cases()
		data = ret_json(country='india', date=time.strftime('%Y-%m-%d', time.gmtime()))
		print('Data refreshed, Time: World=>{}, India=>{}'.format(w_data['statistic_taken_at'], data['stat_by_country'][0]['record_date']))
	except:
		print("Remote disconnected")
