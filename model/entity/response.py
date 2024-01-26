from sqlalchemy import Column, Integer, String, Boolean, DateTime

from model.entity.base import Base

class Response(Base):
    __tablename__ = "user_tbl"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    family = Column(String(30))
    username = Column(String(30))
    password = Column(String(30))
    role = Column(String(30))
    status = Column(Boolean)
class Response:
    def __init__(self, ticket, response_text, date_time, user, status="Open"):
        self.id = None
        self.ticket = ticket
        self.response_text = response_text
        self.date_time = date_time
        self.user = user
        self.status = status
    def __repr__(self):
        return str(self.__dict__)