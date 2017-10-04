from sqlalchemy import Column, Integer, String
from managers.DbManager import Base, DbManager

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    twitter = Column(String(250), nullable=True)
    team = Column(String(250), nullable=True)
    elo = Column(Integer, nullable=False)

    def add_player(self, firstname, lastname, twitter=None, team=None):
            player = Player(firstname=firstname, lastname=lastname, twitter=twitter, team=team, elo=1200)
            session = DbManager().get_session()
            session.add(player)
            session.commit()
