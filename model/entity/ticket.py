class Ticket:
    def __init__(self, group, subject, description, date_time, user, status="Open"):
        pass

    def __repr__(self):
        return str(self.__dict__)
