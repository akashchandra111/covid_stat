from bottle import Bottle, run, route, template, response
import table_generator

app = Bottle()

total_cases_var = table_generator.total_cases_html()
new_cases_var = table_generator.new_cases_html()
active_cases_var = table_generator.active_cases_html()
total_deaths_var = table_generator.total_deaths_html()
new_deaths_var = table_generator.new_deaths_html()
total_recovery_var = table_generator.total_recovery_html()
serious_var = table_generator.serious_html()
cases_perm_var = table_generator.case_perm_html()
world_data_var = table_generator.ret_world_data_html()

def format_html(title, html_table):
	return '''
		<html>
		<head>
			<title> {} - COVID-19 </title>
			<link rel="stylesheet" href="https://unpkg.com/purecss@1.0.1/build/pure-min.css" integrity="sha384-oAOxQR6DkCoMliIh8yFnu25d7Eq/PHS21PClpwjOTeU2jRSq11vu66rf90/cZr47" crossorigin="anonymous">
		</head>
		<body>
			<div class="pure-g">
				<header class="pure-u-1">
					{} in India<br><br>
				</header>
				
				<div class="pure-u-1">
					{}
				</div>

				<div class="pure-u-1">
					<footer>
						Made with hearts& to see this page disapper soon!
					</footer>
				</div>
			</div>
		</body>
		</html>
	'''.format(title, title, html_table)


@app.route('/')
def index_page():
	return '''
		<!DOCTYPE html>
		<head>
			<title> COVID stats </title>
			<link rel="stylesheet" href="https://unpkg.com/purecss@1.0.1/build/pure-min.css" integrity="sha384-oAOxQR6DkCoMliIh8yFnu25d7Eq/PHS21PClpwjOTeU2jRSq11vu66rf90/cZr47" crossorigin="anonymous">
		</head>
		<body>
			<header>
				Get COVID-19 updates for India<br><br>
			</header>
			
			<div class="pure-menu pure-menu-horizontal pure-menu-scrollable">
				<ul class="pure-menu-list">
					<li class="pure-menu-item"> <a class="pure-menu-link" href="/total_cases">Total Cases</a><br> </li>
					<li class="pure-menu-item"> <a class="pure-menu-link" href="/new_cases">New Cases</a><br> </li>
					<li class="pure-menu-item"> <a class="pure-menu-link" href="/active_cases">Active Cases</a><br> </li>
					<li class="pure-menu-item"> <a class="pure-menu-link" href="/total_deaths">Total Deaths</a><br> </li>
					<li class="pure-menu-item"> <a class="pure-menu-link" href="/new_deaths">New Deaths</a><br> </li>
					<li class="pure-menu-item"> <a class="pure-menu-link" href="/total_recovered">Total Recovered</a><br> </li>
					<li class="pure-menu-item"> <a class="pure-menu-link" href="/serious">Serious</a><br> </li>
					<li class="pure-menu-item"> <a class="pure-menu-link" href="/case_perm">Cases per million</a><br><br> </li>
				</ul>
			</div>
				
				<div class="pure-u-1">
					{}
				</div>

			<footer>
				Made with &hearts; to see this page disapper soon!
			</footer>
		</body>
		</html>
	'''.format(world_data_var)

@app.route('/total_cases')
def total_cases():
	return format_html('Total Cases', total_cases_var)

@app.route('/new_cases')
def new_cases():
	return format_html('New Cases', new_cases_var)

@app.route('/active_cases')
def active_cases():
	return format_html('Active Cases', active_cases_var)

@app.route('/total_deaths')
def total_deaths():
	return format_html('Total Death Cases', total_deaths_var)

@app.route('/new_deaths')
def new_deaths():
	return format_html('New Death Cases', new_deaths_var)

@app.route('/total_recovered')
def total_recovered():
	return format_html('Total Recovered Cases', total_recovery_var)

@app.route('/serious')
def serious():
	return format_html('Serious Cases', serious_var)

@app.route('/case_perm')
def case_perm():
	return format_html('Cases/Million', cases_perm_var)

@app.route('/refresh')
def refresh_data():
	table_generator.refresh_data()

	global total_cases_var, new_cases_var, active_cases_var, total_deaths_var, new_deaths_var, total_recovery_var, serious_var, cases_perm_var, world_data_var

	total_cases_var = table_generator.total_cases_html()
	new_cases_var = table_generator.new_cases_html()
	active_cases_var = table_generator.active_cases_html()
	total_deaths_var = table_generator.total_deaths_html()
	new_deaths_var = table_generator.new_deaths_html()
	total_recovery_var = table_generator.total_recovery_html()
	serious_var = table_generator.serious_html()
	cases_perm_var = table_generator.case_perm_html()
	world_data_var = table_generator.ret_world_data_html()

	response.content_type = 'application/json'
	return '{"refresh": true}'

run(app, host='localhost', port=8080, reloader=True)
