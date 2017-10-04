import json

from flask import Flask, Response, request
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


@app.route('/api/players', methods=['GET', 'POST'])
def test():
    print(request.args.to_dict())
    if request.method == 'GET':
        session = DbManager().get_session()
        result = session.execute('SELECT * FROM players;').fetchall()
        resp = Response(str(result))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return result
    elif request.method == 'POST':
        req = request.args.to_dict()
        Player().add_player(req.get('firstname'), req.get('lastname'), req.get('twitter'), req.get('team'))
        return 'thanks!'


if __name__ == '__main__':
    app.run()
