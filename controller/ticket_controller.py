from model.entity.ticket import Ticket
from model.da.ticket_da import TicketDa


class TicketController:
        def save(self, group, subject, description, date_time, user, status="Open"):
            try:
                user = Ticket(group, subject, description, date_time, user, status)
                da = TicketDa()
                da.save(TicketDa)