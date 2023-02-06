from flask import Flask
from flask_restful import Resource, Api, request
import mysql.connector

app = Flask(__name__)
api = Api(app)

# Connect to MySQL database
def connect_to_db():
    mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="killedbygoogle",
    password="MyStrongPassword!",
    database="KilledByGoogle"
    )

    return mydb


class KilledByGoogle(Resource):
    # Get services: default route
    @app.route('/api/services')
    @app.route('/api/services/<int:service_id>')
    def get(service_id=None):
        if not service_id:
            sql_select = "SELECT * FROM Graveyard"
        else:
            sql_select = "SELECT * FROM Graveyard WHERE id = '%s'" % service_id

        # Connect to database and execute query
        mydb = connect_to_db()
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute(sql_select)
        result = mycursor.fetchall()
        mydb.close()
	
        return {'data': result} if result else ({'data': result}, 404)

    # Filter service by open date
    @app.route("/api/open_date/<string:open_date>")
    def get_FilterByOpenDate(open_date):
        # Argument grab and inline validation check
        operator = request.args.get('operator') if request.args.get('operator') == 'less_than' or request.args.get('operator') == 'greater_than' else 'less_than'
        order_by = request.args.get('order_by') if request.args.get('order_by') == 'asc' or request.args.get('order_by') == 'desc' else 'asc'

        if operator == 'less_than':
            sql_select = "SELECT * FROM Graveyard WHERE dateOpen < '%s' ORDER BY dateOpen %s" % (open_date, order_by)
        elif operator == 'greater_than':
            sql_select = "SELECT * FROM Graveyard WHERE dateOpen > '%s' ORDER BY dateOpen %s" % (open_date, order_by)
        
        # Connect to database and execute query
        mydb = connect_to_db()
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute(sql_select)
        result = mycursor.fetchall()
        mydb.close()

        return {'data' : result} if result else ({'data': result}, 404)

    # Filter service by close date
    @app.route("/api/close_date/<string:close_date>")
    def get_FilterByCloseDate(close_date):
        # Argument grab and inline validation check
        operator = request.args.get('operator') if request.args.get('operator') == 'less_than' or request.args.get('operator') == 'greater_than' else 'less_than'
        order_by = request.args.get('order_by') if request.args.get('order_by') == 'asc' or request.args.get('order_by') == 'desc' else 'asc'

        if operator == 'less_than':
            sql_select = "SELECT * FROM Graveyard WHERE dateClose < '%s' ORDER BY dateClose %s" % (close_date, order_by)
        elif operator == 'greater_than':
            sql_select = "SELECT * FROM Graveyard WHERE dateClose > '%s' ORDER BY dateClose %s" % (close_date, order_by)

        # Connect to database and execute query
        mydb = connect_to_db()
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute(sql_select)
        result = mycursor.fetchall()
        mydb.close()

        return {'data' : result} if result else ({'data': result}, 404)

    # Filter service by type
    @app.route("/api/type/<string:service_type>")
    def get_FilterByType(service_type):
        # Argument grab
        service_type = service_type if service_type == 'app' or service_type == 'service' or service_type == 'hardware' else ''

        # Argument validation
        if not service_type:
            return ({'data': 'Type of service not valid. Search by either app, service or hardware'}, 400)
        
        sql_select = "SELECT * FROM Graveyard WHERE type = '%s'" % service_type

        # Connect to database and execute query
        mydb = connect_to_db()
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute(sql_select)
        result = mycursor.fetchall()
        mydb.close()

        return {'data' : result} if result else ({'data': result}, 404)
    
    # Filter service by name
    @app.route('/api/name/<string:service_name>')
    def get_FilterByName(service_name):
        # Prepare string for query
        service_name = "%"+service_name+"%"
        sql_select = "SELECT * FROM Graveyard WHERE name LIKE '%s'" % service_name

        # Connect to database and execute query
        mydb = connect_to_db()
        mycursor = mydb.cursor(dictionary=True)
        mycursor.execute(sql_select)
        result = mycursor.fetchall()
        mydb.close()

        return {'data' : result} if result else ({'data': result}, 404)








api.add_resource(KilledByGoogle, "/api/services/<int:service_id>", # All services or filter by ID
"/api/open_date/<string:open_date>", "/api/close_date/<string:close_date>", # Filter by open date or close date
"/api/type/<string:service_type>", # Filter by type
"/api/name/<string:service_name>") # Filter by name


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
