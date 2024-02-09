from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model.entity.base import Base

class Response(Base):
    __tablename__ = "response_tbl"

    id = Column(Integer, primary_key=True)
    Response_text = Column(String(250))
    DateTime = Column(DateTime)
    password = Column(String(30))
    status = Column(Boolean)

    ticket_id = Column(Integer, ForeignKey("ticket_tbl.id"))
    user_id = Column(Integer, ForeignKey("user_tbl.id"))

    user = relationship("User")
    ticket = relationship("Ticket")

    def __init__(self, ticket, response_text, date_time, user, status="Open"):
        self.id = None
        self.ticket = ticket
        self.response_text = response_text
        self.date_time = date_time
        self.user = user
        self.status = status

