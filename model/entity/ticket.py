from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model.entity.base import Base

class Ticket(Base):
    __tablename__ = "ticket_tbl"
    id = Column(Integer, primary_key=True)
    group = Column(String(30))
    subject = Column(String(30))
    description = Column(String(250))
    data_time = Column(DateTime)
    status = Column(Boolean)

    user_id = Column(Integer, ForeignKey("user_tbl.id"))
    user = relationship("User")

    def __init__(self, group, subject, description, date_time, user, status="Open"):
        self.id = None
        self.group = group
        self.subject = subject
        self.description = description
        self.date_time = date_time
        self.user = user
        self.status = status
