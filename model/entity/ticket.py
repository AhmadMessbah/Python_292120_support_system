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
