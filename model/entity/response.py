class response:
    def __init__(self, ticket, response_text, date_time, user, status="Open"):
        self.id = None
        self.ticket = ticket
        self.response_text = response_text
        self.date_time = date_time
        self.user = user
        self.status = status
