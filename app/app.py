from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tickets = []

@app.route('/')
@app.route("/index")
def cloud_support_ticket_system():
    print("Homepage tickets:", tickets)
   
    return render_template("index.html", tickets=tickets)

@app.route("/new-ticket", methods=["GET", "POST"])
def new_ticket():
    if request.method == "POST":
    
       #1. Get the form values
       Name = request.form.get("Name")
       Email = request.form.get("Email")
       Summary = request.form.get("Summary")
       Category = request.form.get("Category")
       Priority = request.form.get("Priority")
       Date = request.form.get("Date")
       
       # 2. Create the ticket number
       ticket_number = len(tickets) + 1
       ticket_id = f"REQ-{ticket_number:03d}"
       
       #3. Crate the dictionary
       new_ticket = {
         "Ticket ID": ticket_id,
         "Name": Name,
         "Email": Email,
         "Summary": Summary,
         "Category": Category,
         "Priority": Priority,
         "Status": "Open",
         "Owner": "Unassigned",
         "Date": Date
       }

        #4. Add it to the list 
       tickets.append(new_ticket)
       return redirect(url_for("cloud_support_ticket_system"))

    return render_template("ticket.html")

@app.route("/ticket/<ticket_id>")
def view_ticket(ticket_id):
    for ticket in tickets:
        if ticket["Ticket ID"] == ticket_id:
            return render_template("ticket_detail.html", ticket=ticket)

    return "Ticket not found", 404


@app.route("/update-status/<ticket_id>", methods=["POST"])
def update_status(ticket_id):
    new_status = request.form.get("Status")

    for ticket in tickets:
        if ticket["Ticket ID"] == ticket_id:
            ticket["Status"] = new_status
            return redirect(url_for("view_ticket", ticket_id=ticket_id))

        return "Ticket not found", 404



@app.route("/update-owner/<ticket_id>", methods=["POST"])
def update_owner(ticket_id):
    new_owner = request.form.get("Owner")

    for ticket in tickets:
        if ticket["Ticket ID"] == ticket_id:
            ticket["Owner"] = new_owner
            return redirect(url_for("view_ticket", ticket_id=ticket_id))

        return "Ticket not found", 404


@app.route("/delete-ticket/<ticket_id>", methods=["POST"])
def delete_ticket(ticket_id):

    for ticket in tickets:
        if ticket["Ticket ID"] == ticket_id:

            tickets.remove(ticket)

            return redirect(url_for("cloud_support_ticket_system"))

    return "Ticket not found", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)