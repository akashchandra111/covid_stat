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

@app.route('/')
def index_page():
	return '''
		<html>
		<head>
			<title> COVID stats </title>
		</head>
		<body>
			<header>
				Get COVID-19 updates for India<br><br>
			</header>
			
			Get info on <a href="/total_cases">Total Cases</a><br>
			Get info on <a href="/new_cases">New Cases</a><br>
			Get info on <a href="/active_cases">Active Cases</a><br>
			Get info on <a href="/total_deaths">Total Deaths</a><br>
			Get info on <a href="/new_deaths">New Deaths</a><br>
			Get info on <a href="/total_recovered">Total Recovered</a><br>
			Get info on <a href="/serious">Serious</a><br>
			Get info on <a href="/case_perm">Total Cases/million</a><br><br>
			
			{}

			<footer>
				Made with <3 to see this page disapper soon!
			</footer>
		</body>
		</html>
	'''.format(world_data_var)

@app.route('/total_cases')
def total_cases():
	return '''
		<html>
		<head>
			<title> Total Cases - COVID-19 </title>
		</head>
		<body>
			<header>
				Total cases in India<br><br>
			</header>
			
			{}

			<footer>
				Made with <3 to see this page disapper soon!
			</footer>
		</body>
		</html>
	'''.format(total_cases_var)


@app.route('/new_cases')
def new_cases():
	return '''
		<html>
		<head>
			<title> New Cases - COVID-19 </title>
		</head>
		<body>
			<header>
				New cases in India<br><br>
			</header>
			
			{}

			<footer>
				Made with <3 to see this page disapper soon!
			</footer>
		</body>
		</html>
	'''.format(new_cases_var)

@app.route('/active_cases')
def active_cases():
	return '''
		<html>
		<head>
			<title> Active Cases - COVID-19 </title>
		</head>
		<body>
			<header>
				Active cases in India<br><br>
			</header>
			
			{}

			<footer>
				Made with <3 to see this page disapper soon!
			</footer>
		</body>
		</html>
	'''.format(active_cases_var)

@app.route('/total_deaths')
def total_deaths():
	return '''
		<html>
		<head>
			<title> Total Deaths - COVID-19 </title>
		</head>
		<body>
			<header>
				 Total Deaths in India<br><br>
			</header>
			
			{}

			<footer>
				Made with <3 to see this page disapper soon!
			</footer>
		</body>
		</html>
	'''.format(total_deaths_var)

@app.route('/new_deaths')
def new_deaths():
	return '''
		<html>
		<head>
			<title> New Deaths - COVID-19 </title>
		</head>
		<body>
			<header>
				 New Deaths in India<br><br>
			</header>
			
			{}

			<footer>
				Made with <3 to see this page disapper soon!
			</footer>
		</body>
		</html>
	'''.format(new_deaths_var)

@app.route('/total_recovered')
def total_recovered():
	return '''
		<html>
		<head>
			<title> Total Recovered - COVID-19 </title>
		</head>
		<body>
			<header>
				 Total Recovered in India<br><br>
			</header>
			
			{}

			<footer>
				Made with <3 to see this page disapper soon!
			</footer>
		</body>
		</html>
	'''.format(total_recovery_var)

@app.route('/serious')
def serious():
	return '''
		<html>
		<head>
			<title> Serious Persons - COVID-19 </title>
		</head>
		<body>
			<header>
				 Serious Persons in India<br><br>
			</header>
			
			{}

			<footer>
				Made with <3 to see this page disapper soon!
			</footer>
		</body>
		</html>
	'''.format(serious_var)

@app.route('/case_perm')
def case_perm():
	return '''
		<html>
		<head>
			<title> Cases/Million - COVID-19 </title>
		</head>
		<body>
			<header>
				 Cases/Million in India<br><br>
			</header>
		
			{}

			<footer>
				Made with <3 to see this page disapper soon!
			</footer>
		</body>
		</html>
	'''.format(cases_perm_var)

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
