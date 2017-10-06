import json

from flask import Flask, Response, request, jsonify
from managers.DbManager import init_db
from models.PlayerModel import Player

app = Flask(__name__)


def fix(list):
    new_list = []
    for item in list:
        new_list.append({
            'id': item.id,
            'firstname': item.firstname,
            'lastname': item.lastname,
            'twitter': item.twitter,
            'team': item.team,
            'elo': item.elo
        })
    return new_list


def create_response(resp):
    resp = Response(json.dumps({'players': fix(resp)}))
    resp.headers['Access-Control-Allow-Origin'] = 'http://passifyer.com'
    return resp


@app.route('/api/players', methods=['GET', 'POST', 'PUT', 'OPTIONS'])
def test():
    req = request.get_json()
    if request.method == 'GET':
        result = Player.query.all()
        return create_response(result)
    elif request.method == 'POST':
        print(req)
        result = Player.get_players(req)
        return create_response(result)
    elif request.method == 'PUT':
        Player.add_player(req)
        return 'Added: ' + str(req)
    elif request.method == 'OPTIONS':
        resp = Response()
        resp.headers['Allow'] = 'OPTIONS, GET, HEAD, POST'
        resp.headers['Access-Control-Allow-Origin'] = 'http://passifyer.com'
        return resp


@app.route('/api/player/<id>', methods=['GET'])
def player_id(id):
    try:
        result = create_response(Player.get_player(id))
        return result
    except TypeError:
        return "Invalid ID Number"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
