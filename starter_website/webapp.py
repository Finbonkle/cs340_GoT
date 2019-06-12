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
    query = "SELECT name, alive, mannerOfDeath,  portrayal, phil_id, id from Characters;"
    result = execute_query(db_connection, query).fetchall();

    phil_query = "SELECT name, id from Philosophies"
    phil_results = execute_query(db_connection, phil_query).fetchall();

    print(result)
    return render_template('characters.html', rows=result, phil=phil_results)

@webapp.route('/factions', methods=['POST','GET'])
def fact_page():
    db_connection = connect_to_database()
    if request.method == 'GET':
        fact_query = "SELECT id, name, type, strength, weakness, phil_id from Factions;"
        fact_result = execute_query(db_connection, fact_query).fetchall();
        print(fact_result)
        
        phil_query = "SELECT name, id from Philosophies"
        phil_result = execute_query(db_connection, phil_query).fetchall();
        print(phil_result)
        
        char_query = "SELECT id, name FROM Characters"
        char_result = execute_query(db_connection, char_query)
        print(char_result)
        
        fnum_query = "SELECT fact_id, char_id FROM Factions_Characters"
        fnum_result = execute_query(db_connection, fnum_query)
        print(fnum_result)

        test_query = "SELECT MAX(id) FROM Factions"
        test_result = execute_query(db_connection, test_query)
        
        return render_template('factions.html', facs=fact_result, phil=phil_result, char=char_result, fnum=fnum_result, test=test_result)
    elif request.method == 'POST':
        ch = request.form['addChar']
        fa = request.form['addFact']
        query = "INSERT INTO `Factions_Characters` (`fact_id`, `char_id`) VALUES (" + fa + ", " + ch +")"
        result = execute_query(db_connection, query)
        print(result)
        return ('Person added to faction!')

@webapp.route('/philosophies')
def phil_page():
    print("Fetching and rendering people web page")
    db_connection = connect_to_database()
    query = "SELECT name, type, supernatural, id from Philosophies;"
    result = execute_query(db_connection, query).fetchall();
    print(result)
    return render_template('philosophies.html', rows=result)

@webapp.route('/create', methods=['POST','GET'])
def create_page():
    db_connection = connect_to_database()
    if request.method == 'GET':
        phil_query = "SELECT id, name from Philosophies;"
        phil_result = execute_query(db_connection, phil_query).fetchall();
        print(phil_result)
        return render_template('create.html', phils=phil_result)

    elif request.method == 'POST':
        print("Add new people!");
        name = request.form['name']
        print("Name is " + name)
        mannerOfDeath = request.form['mannerOfDeath']
        portrayal = request.form['portrayal']
        philos = request.form['phil_id']
        alive = request.form['qAlive']
        if alive == "no":
            aliveValue = 0
        elif alive == "yes":
            aliveValue = 1
        query = 'INSERT INTO Characters (name, alive, mannerOfDeath, portrayal, phil_id) VALUES (%s,%s,%s,%s,%s)'
        data = (name, aliveValue, mannerOfDeath, portrayal, philos)
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
        char_query = 'SELECT id, name, alive, mannerOfDeath, portrayal, phil_id from Characters where id = %s' % (id)
        char_results = execute_query(db_connection, char_query).fetchone()
        if char_results == None:
            return "No such person found!"

        phil_query = 'SELECT name, id FROM Philosophies;'
        phil_results = execute_query(db_connection, phil_query).fetchall();
        return render_template('character_update.html', chars = char_results, phils = phil_results)
    elif request.method == 'POST':
        name = request.form['name']
        alive = request.form['qAlive']
        MoD = request.form['MoD']
        #alle = request.form['alleg']
        act = request.form['portrayal']
        philos = request.form['philosophy']

        print(request.form)

        query = "UPDATE Characters SET name = %s, alive = %s, mannerOfDeath = %s, portrayal = %s, phil_id = %s WHERE id = %s;"
        data = (name, alive, MoD, act, philos, (id))
        result = execute_query(db_connection, query, data)
        print(str(result.rowcount) + " row(s) updated");
        return redirect('/characters')

@webapp.route('/delete_char/<int:id>')
def delete_char(id):
    '''deletes a character with the given id'''
    db_connection = connect_to_database()

    fact_query = "DELETE FROM Factions_Characters WHERE char_id = %s" % (id)
    fact_results = execute_query(db_connection, fact_query)

    query = "DELETE FROM Characters WHERE id = %s" % (id)
    result = execute_query(db_connection, query)
    return (str(result.rowcount) + "row deleted")

@webapp.route('/search', methods=['POST','GET'])
def search_char():
    db_connection = connect_to_database()
    if request.method == 'GET':
        return render_template('search.html')
    elif request.method == 'POST':
        usrSearch = request.form['usrStr']
        query = "SELECT id, name, alive, mannerOfDeath, portrayal, phil_id from Characters where Characters.name = '" + usrSearch + "'"
        result = execute_query(db_connection, query)

        phil_query = "SELECT name, id from Philosophies"
        phil_results = execute_query(db_connection, phil_query).fetchall();

        print(result)
        return render_template('search.html', chars=result, phils=phil_results)

@webapp.route('/seasons', methods=['POST','GET'])
def seasons():
    db_connection = connect_to_database()
    if request.method == 'GET':
        snum_query = "SELECT DISTINCT id FROM Seasons"
        snum_result = execute_query(db_connection, snum_query)
        print(snum_result)
        seas_query = "SELECT id, char_id FROM Seasons"
        seas_result = execute_query(db_connection, seas_query)
        print(seas_result)
        char_query = "SELECT id, name FROM Characters"
        char_result = execute_query(db_connection, char_query)
        print(char_result)
        return render_template('seasons.html', snum=snum_result, seas=seas_result, char=char_result)
    elif request.method == 'POST':
        ch = request.form['addChar']
        se = request.form['addSeas']
        query = "INSERT INTO `Seasons` (`id`, `char_id`) VALUES (" + se + ", " + ch +")"
        result = execute_query(db_connection, query)
        print(result)
        return ('Person added to season!')

@webapp.route('/newFaction', methods=['POST','GET'])
def new_faction():
    db_connection = connect_to_database()
    if request.method == 'GET':
        phil_query = "SELECT id, name from Philosophies;"
        phil_result = execute_query(db_connection, phil_query).fetchall();
        print(phil_result)
        fact_query = "SELECT id, name, type, strength, weakness, phil_id from Factions;"
        fact_result = execute_query(db_connection, fact_query).fetchall();
        print(fact_result)
        return render_template('newFaction.html', phils=phil_result, facts=fact_result)
    elif request.method == 'POST':
        print("Add new faction!");
        name = request.form['name']
        typ = request.form['type']
        stre = request.form['strength']
        weak = request.form['weakness']
        philos = request.form['phil_id']
        query = 'INSERT INTO Factions (name, type, strength,  weakness, phil_id) VALUES (%s,%s,%s,%s,%s)'
        data = (name, typ, stre, weak, philos)
        attempt = execute_query(db_connection, query, data)
        print(attempt)
        return ('Faction added!');

@webapp.route('/newPhilosophy', methods=['POST','GET'])
def new_philosophy():
    db_connection = connect_to_database()
    if request.method == 'GET':
        phil_query = "SELECT name, type, supernatural, id from Philosophies;"
        phil_result = execute_query(db_connection, phil_query).fetchall();
        print(phil_result)
        return render_template('newPhilosophy.html', phils=phil_result)
    elif request.method == 'POST':
        print("Add new philosophy!");
        name = request.form['name']
        typ = request.form['type']
        superNat = request.form['sn']
        query = 'INSERT INTO Philosophies (name, type, supernatural) VALUES (%s,%s,%s)'
        data = (name, typ, superNat)
        attempt = execute_query(db_connection, query, data)
        print(attempt)
        return ('Philosophy added!');


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
        return render_template('season_create.html')
    elif request.method == 'POST':
        print("Add new season!");
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
    query = "DELETE FROM bsg_people WHERE id = %s"
    data = (id,)

    result = execute_query(db_connection, query, data)
    return (str(result.rowcount) + "row deleted")
