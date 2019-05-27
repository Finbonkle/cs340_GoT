from flask import Flask, render_template
from flask import request, redirect
from db_connector.db_connector import connect_to_database, execute_query
#create the web application
webapp = Flask(__name__)

#provide a route where requests on the web application can be addressed
@webapp.route('/hello')
#provide a view (fancy name for a function) which responds to any requests on this route
def hello():
    return "Hello World!";

@webapp.route('/index')
def index_page():
    return render_template('index.html')

@webapp.route('/characters')
def char_page():
    print("Fetching and rendering people web page")
    db_connection = connect_to_database()
    query = "SELECT name, alive, mannerOfDeath, allegiance, portrayal, phil_id from Characters;"
    result = execute_query(db_connection, query).fetchall();


    phil_query = "SELECT name, id from Philosophies"
    phil_results = execute_query(db_connection, phil_query).fetchall();

    print(result)
    return render_template('characters.html', rows=result, phil=phil_results)

@webapp.route('/factions')
def fact_page():
    print("Fetching and rendering people web page")
    db_connection = connect_to_database()
    query = "SELECT name, type, strength, weakness, phil_id from Factions;"
    result = execute_query(db_connection, query).fetchall();
    print(result)
    return render_template('factions.html', rows=result)

@webapp.route('/philosophies')
def phil_page():
    print("Fetching and rendering people web page")
    db_connection = connect_to_database()
    query = "SELECT name, type, supernatural from Philosophies;"
    result = execute_query(db_connection, query).fetchall();
    print(result)
    return render_template('philosophies.html', rows=result)

@webapp.route('/create', methods=['POST','GET'])
def create_page():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = "SELECT id, name from Philosophies;"
        result = execute_query(db_connection, query).fetchall();
        print(result)
        return render_template('create.html', phils = result)

    elif request.method == 'POST':
        print("Add new people!");
        name = request.form['name']
        print("Name is ", name)
        mannerOfDeath = request.form['mannerOfDeath']
        allegiance = request.form['allegiance']
        portrayal = request.form['portrayal']
        philos = request.form['phil_id']
        alive = request.form['qAlive']
        if alive == "no":
            aliveValue = 0
        elif alive == "yes":
            aliveValue = 1
        query = 'INSERT INTO Characters (name, alive, mannerOfDeath, allegiance, portrayal, phil_id) VALUES (%s,%s,%s,%s,%s,%s)'
        data = (name, aliveValue, mannerOfDeath, allegiance, portrayal, philos)
        attempt = execute_query(db_connection, query, data)
        print(attempt)
        return ('Person added!');

@webapp.route('/edit')
def edit_page():
    print("Fetching and rendering people web page")
    db_connection = connect_to_database()
    query = "SELECT name, id from Characters;"
    result = execute_query(db_connection, query).fetchall();
    print(result)
    return render_template('edit.html', rows=result)


@webapp.route('/character_update/<int:id>', methods=['POST','GET'])
def update_char(id):
    db_connection = connect_to_database()
    #display existing data
    if request.method == 'GET':
        char_query = 'SELECT id, name, alive, mannerOfDeath, allegiance, portrayal, phil_id from Characters where id = %s' % (id)
        char_results = execute_query(db_connection, char_query).fetchone()
        if char_results == None:
            return "No such person found!"

        phil_query = 'SELECT name, id FROM Philosophies;'
        phil_results = execute_query(db_connection, phil_query).fetchall();
        return render_template('character_update.html', chars = char_results, phils = phil_results)
    elif request.method == 'POST':
        name = request.form['name']
        alive = request.form['alive']
        MoD = request.form['MoD']
        alle = request.form['alleg']
        act = request.form['portrayal']
        #philos = request.form['philosophy']

        #philos_query = 'SELECT id FROM Philosophies WHERE name = %s' % philos
        #philos_result = execute_query(db_connection, philos_query).fetchone()

        print(request.form);

        query = "UPDATE Characters SET name = %s, alive = %s, mannerOfDeath = %s, allegiance = %s, portrayal = %s WHERE id = %s;"
        data = (name, alive, MoD, alle, act, (id))
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated");

        return redirect('/characters')




#################################################################

@webapp.route('/browse_bsg_people')
#the name of this function is just a cosmetic thing
def browse_people():
    print("Fetching and rendering people web page")
    db_connection = connect_to_database()
    query = "SELECT fname, lname, homeworld, age, id from bsg_people;"
    result = execute_query(db_connection, query).fetchall();
    print(result)
    return render_template('people_browse.html', rows=result)

@webapp.route('/add_new_people', methods=['POST','GET'])
def add_new_people():
    db_connection = connect_to_database()
    if request.method == 'GET':
        query = 'SELECT id, name from bsg_planets'
        result = execute_query(db_connection, query).fetchall();
        print(result)

        return render_template('people_add_new.html', planets = result)
    elif request.method == 'POST':
        print("Add new people!");
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        homeworld = request.form['homeworld']

        query = 'INSERT INTO bsg_people (fname, lname, age, homeworld) VALUES (%s,%s,%s,%s)'
        data = (fname, lname, age, homeworld)
        execute_query(db_connection, query, data)
        return ('Person added!');

@webapp.route('/')
def index():
    return "<p>Are you looking for /db-test or /hello or <a href='/browse_bsg_people'>/browse_bsg_people</a> or /add_new_people or /update_people/id or /delete_people/id </p>"

@webapp.route('/db-test')
def test_database_connection():
    print("Executing a sample query on the database using the credentials from db_credentials.py")
    db_connection = connect_to_database()
    query = "SELECT * from bsg_people;"
    result = execute_query(db_connection, query);
    return render_template('db_test.html', rows=result)

#display update form and process any updates, using the same function
@webapp.route('/update_people/<int:id>', methods=['POST','GET'])
def update_people(id):
    db_connection = connect_to_database()
    #display existing data
    if request.method == 'GET':
        people_query = 'SELECT id, fname, lname, homeworld, age from bsg_people WHERE id = %s' % (id)
        people_result = execute_query(db_connection, people_query).fetchone()

        if people_result == None:
            return "No such person found!"

        planets_query = 'SELECT id, name from bsg_planets'
        planets_results = execute_query(db_connection, planets_query).fetchall();

        return render_template('people_update.html', planets = planets_results, person = people_result)
    elif request.method == 'POST':
        print("Update people!");
        char_id = request.form['character_id']
        fname = request.form['fname']
        lname = request.form['lname']
        age = request.form['age']
        homeworld = request.form['homeworld']

        print(request.form);

        query = "UPDATE bsg_people SET fname = %s, lname = %s, age = %s, homeworld = %s WHERE id = %s"
        data = (fname, lname, age, homeworld, char_id)
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated");

        return redirect('/browse_bsg_people')

@webapp.route('/delete_people/<int:id>')
def delete_people(id):
    '''deletes a person with the given id'''
    db_connection = connect_to_database()
    query = "DELETE FROM bsg_people WHERE character_id = %s"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return (str(result.rowcount) + "row deleted")
