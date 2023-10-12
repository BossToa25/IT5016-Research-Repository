from Ticket import Ticket;

#Staff request information
tickets = []
ticket_1 = Ticket("INNAM", "Inna", "Inna@whitecliffe.co.n", "My monitor stopped working")
tickets.append(ticket_1)
ticket_2 = Ticket("MARIAH", "Mariah", "Mariah@whitecliffe.co.n", "Request for a videocamera to conduct webinars")
tickets.append(ticket_2)
ticket_3 = Ticket("JOHNS", "John", "John@whitecliffe.co.n", "Password Change")
tickets.append(ticket_3)


# Ticket request display output
def display(ticket):
    print("Ticket Number:", ticket.ticket_number)
    print("Ticket Creator:", ticket.ticket_creator_name)
    print("Staff ID:", ticket.staff_id)
    print("Email Address:", ticket.contact_email)
    print("Description:", ticket.description)
    print("Response:", ticket.response)
    print("Ticket Status:", ticket.ticket_status)
# Ticket creation display output
def create_ticket():
    print("Create a New Ticket:")
    staff_id = input("Staff ID: ")
    ticket_creator_name = input("Ticket Creator Name: ")
    contact_email = input("Contact Email: ")
    description = input("Issue Description: ")
    ticket = Ticket(staff_id, ticket_creator_name, contact_email, description)
    print("Ticket: ", ticket.ticket_number)
    tickets.append(ticket)
    print("Ticket Created\n")

    display(ticket)
    display_ticket_statistics()
# Ticket resolution display output
def resolve_ticket():
    print("Resolve a Ticket: ")
    ticket_number = int(input("Enter Ticket Number to Resolve: "))
    found = False
    for ticket in tickets:
        if ticket.ticket_number == ticket_number:
            resolution_message = input("Resolution: ")
            ticket.response = resolution_message
            print("Ticket Resolved\n")
            found = True
            break
    if not found: 
        print("Ticket not found.\n")

# Ticket reopening display output
def reopen_ticket():
    print("Reopen a ticket: ")
    ticket_number = int(input("Enter Ticket Number to Reopen: "))
    for ticket in tickets:
        if ticket.ticket_number == ticket_number:
            ticket.reopen()
            print("Ticket Reopened\n")
            return
        print("Ticket not found.\n")

# Ticket statistics display output
def display_ticket_statistics():
    created_count = len(tickets)
    resolved_count = len([ticket for ticket in tickets if ticket.ticket_status == "Closed"])
    open_count = len([ticket for ticket in tickets if ticket.ticket_status == "Open"])

    print("Displaying Ticket Statistics")
    print("Tickets Created:", created_count)
    print("Tickets Resolved:", resolved_count)
    print("Tickets to Solve:", open_count, "\n")

# Help desk option list output
def main():
    while True:
        print("Help Desk Ticketing System")
        print("1. Create Ticket")
        print("2. Resolve Ticket")
        print("3. Reopen Ticket")
        print("4. Display Ticket Statistics")
        print("5. Display a Ticket") 
        print("6. Display all Tickets")
        print("7. End Program")
        choice = input("Enter option: ")
# List number input options
        if choice == "1":
            create_ticket()
        elif choice == "2":
            resolve_ticket()
        elif choice == "3":
            reopen_ticket()
        elif choice == "4":
            display_ticket_statistics()
        elif choice == "5":
            ticket_number = int(input("Enter Ticket Number to display: "))
            for ticket in tickets:
                if ticket.ticket_number == ticket_number:
                    display(ticket)
                    break
        elif choice == "6":
            for ticket in tickets:
                display(ticket)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.\n")

main()
