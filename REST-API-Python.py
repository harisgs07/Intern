from flask import Flask, jsonify
app = Flask(__name__)
details = [{'username': 'harisgs', 'age': 22},
             {'username': 'shnjk', 'age': 21},
             {'username': 'qwerty', 'age': 72}]

@app.route('/')
def index():
    return "Welcome To The Course API Lets start's"

@app.route('/details', methods = ['GET'])
def get():
    return jsonify({'Details': details})

@app.route('/details/<int:id>', methods = ['GET'])
def get_age(id):
    return jsonify({'Details_index': details[id]})

@app.route('/details', methods = ['POST'])
def create():
    """ Before Running The Code--
            1.Goto Terminal
            2.>curl -i -H "Content-Type: Application/json" -X POST http://localhost:5000/details """
    details_new = {'username': 'popo', 'age': 12}
    details.append(details_new)
    return jsonify({'Cerated': details_new})

@app.route('/details/<int:id>', methods = ['PUT'])
def update_age(id):
    """ Before Running The Code--
            1.Goto Terminal
            2.>curl -i -H "Content-Type: Application/json" -X POST http://localhost:5000/details/2
             in url last provided number is the index."""
    details[id]['username'] = 'jkhk'
    return jsonify({'update_age': details[id]})

if __name__ == '__main__':
    app.run(debug=True)
