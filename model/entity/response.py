from sqlalchemy import Column, Integer, String, Boolean, DateTime

from model.entity.base import Base

class Response(Base):
    __tablename__ = "response_tbl"
    id = Column(Integer, primary_key=True)
    ticket = Column(String(30))
    Response_text = Column(String(30))
    DateTime = Column(String(30))
    password = Column(String(30))
    user = Column(String(30))
    status = Column(Boolean)

    def __init__(self, ticket, response_text, date_time, user, status="Open"):
        self.id = None
        self.ticket = ticket
        self.response_text = response_text
        self.date_time = date_time
        self.user = user
        self.status = status