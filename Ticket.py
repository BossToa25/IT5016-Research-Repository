class Ticket:
    counter = 2000
    tickets = []
    # Initial ticket entry creation statistic display
    def __init__ (self, staff_id, ticket_creator_name, contact_email, description):
        self.ticket_number = Ticket.counter + 1
        Ticket.counter += 1
        self.staff_id = staff_id
        self.ticket_creator_name = ticket_creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.ticket_status = "Open"
        # Password change request resolved display
        if "password change" in self.description.lower():
            new_password = self.staff_id[:2] + self.ticket_creator_name[:3]
            self.response = "New password generated: " + new_password
            self.ticket_status = "Closed"

    # Reopening ticket display
    def reopen(self):
        self.ticket_status = "Open"
        self.response = "Ticket Reopened"

