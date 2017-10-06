from sqlalchemy import Column, Integer, String
from managers.DbManager import Base, db_session

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    twitter = Column(String(250), nullable=True)
    team = Column(String(250), nullable=True)
    elo = Column(Integer, nullable=False)

    @staticmethod
    def add_player(data):
            player = Player(firstname=data.get('firstname'), lastname=data.get('lastname'), twitter=data.get('twitter'),
                            team=data.get('team'), elo=1200)
            db_session.add(player)
            db_session.commit()

    @staticmethod
    def get_player(id):
        return Player.query.get(id)

    @staticmethod
    def get_players(data):
        fn = data.get('firstname') or '%'
        ln = data.get('lastname') or '%'
        tw = data.get('twitter') or '%'
        tm = data.get('team') or '%'
        elo = data.get('elo') or '%'
        result = Player.query\
            .filter(Player.firstname.like(fn))\
            .filter(Player.lastname.like(ln))\
            .filter(Player.twitter.like(tw))\
            .filter(Player.team.like(tm))\
            .filter(Player.elo.like(elo))
        print(result)
        return result
