from sqlalchemy import Column, Integer, String, Boolean, DateTime

from model.entity.base import Base

class Ticket(Base):
    __tablename__ = "user_tbl"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    family = Column(String(30))
    username = Column(String(30))
    password = Column(String(30))
    role = Column(String(30))
    status = Column(Boolean)
class Ticket:
    def __init__(self, group, subject, description, date_time, user, status="Open"):
        self.id = None
        self.group = group
        self.subject = subject
        self.description = description
        self.date_time = date_time
        self.user = user
        self.status = status

    def __repr__(self):
        return str(self.__dict__)
