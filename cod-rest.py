import json

from flask import Flask, Response, request, jsonify
from managers.DbManager import DbManager
from models.PlayerModel import Player

DbManager.set_engine('sqlite:///db/player.db')

app = Flask(__name__)

players = [
    {
        'id': 1,
        'firstName': 'Aaron',
        'lastName': 'O\'Rourke',
        'team': 'Numbah Juans',
        'rating': 1000
    },
    {
        'id': 2,
        'firstName': 'Tyler',
        'lastName': 'McGraw',
        'team': 'Twotally Awesome',
        'rating': 1000
    },
    {
        'id': 3,
        'firstName': 'Jordan',
        'lastName': 'Hyland',
        'team': 'Three-Fiddy',
        'rating': 2600
    }
]

def fix(list):
    new_list = []
    for item in list:
        new_list.append({
            'firstname' : item[1],
            'lastname' : item[2],
            'twitter' : item[3],
            'team' : item[4],
            'elo' : item[5]
        })
    return new_list


@app.route('/api/players', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        session = DbManager().get_session()
        result = session.execute("SELECT * FROM players;").fetchall()
        resp = Response(json.dumps({'players': fix(result)}))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    elif request.method == 'POST':
        req = request.get_json()
        Player().add_player(req.get('firstname'), req.get('lastname'), req.get('twitter'), req.get('team'))
        return 'Added: ' + str(req)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
