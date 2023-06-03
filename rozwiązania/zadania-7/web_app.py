from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/new')
def new_employee():
    forma = """ <form action="/add">
  <label for="fname">First name:</label><br>
  <input type="text" id="name" name="name"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="surname" name="surname">
  <input type="submit" value="Dodaj pracownika">
</form> """
    return forma


@app.route('/add')
def add_employee():
    # --- wydrukuj na ekranie parametry, jakie wysłała przeglądarka
    print(request.args)
    # --- odbierz wartości, których potrzebujemy: imię i nazwisko pracownika
    name = request.args["name"]
    surname = request.args["surname"]
    return '<b> dodano: %s %s</b>' % (name, surname)

if __name__ == "__main__":
    app.run(debug=True)




