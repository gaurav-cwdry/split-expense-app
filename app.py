from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage
trips = []


# ---------- HOME ----------
@app.route("/")
def home():
    return render_template("index.html", trips=trips)


# ---------- ADD TRIP ----------
@app.route("/add_trip", methods=["POST"])
def add_trip():
    trips.append({
        "name": request.form["trip_name"],
        "members": [],
        "balances": {},
        "settled": False
    })
    return redirect(url_for("home"))


# ---------- TRIP PAGE ----------
@app.route("/trip/<int:i>")
def trip_page(i):
    return render_template("trip.html", trip=trips[i], index=i)


# ---------- ADD MEMBER ----------
@app.route("/add_member", methods=["POST"])
def add_member():
    i = int(request.form["trip_index"])
    name = request.form["member_name"]
    email = request.form["member_email"]

    trips[i]["members"].append({
        "name": name,
        "email": email
    })
    trips[i]["balances"][name] = 0

    return redirect(url_for("trip_page", i=i))


# ---------- ADD EXPENSE ----------
@app.route("/add_expense", methods=["POST"])
def add_expense():
    i = int(request.form["trip_index"])
    amount = float(request.form["amount"])
    paid_by = request.form["paid_by"]

    members = trips[i]["members"]
    share = amount / len(members)

    for m in members:
        trips[i]["balances"][m["name"]] -= share

    trips[i]["balances"][paid_by] += amount

    return redirect(url_for("trip_page", i=i))


# ---------- SETTLEMENT LOGIC ----------
def calculate_settlement(balances):
    creditors, debtors, result = [], [], []

    for name, bal in balances.items():
        if bal > 0:
            creditors.append([name, bal])
        elif bal < 0:
            debtors.append([name, -bal])

    i = j = 0
    while i < len(debtors) and j < len(creditors):
        amt = min(debtors[i][1], creditors[j][1])
        result.append({
            "from": debtors[i][0],
            "to": creditors[j][0],
            "amount": round(amt, 2)
        })
        debtors[i][1] -= amt
        creditors[j][1] -= amt
        if debtors[i][1] == 0:
            i += 1
        if creditors[j][1] == 0:
            j += 1

    return result


# ---------- SETTLEMENT PAGE ----------
@app.route("/settlement/<int:i>")
def settlement(i):
    settlements = calculate_settlement(trips[i]["balances"])
    return render_template(
        "settlement.html",
        trip=trips[i],
        settlements=settlements,
        index=i
    )


# ---------- MARK AS SETTLED ----------
@app.route("/settle_trip/<int:i>", methods=["POST"])
def settle_trip(i):
    trips[i]["settled"] = True
    return redirect(url_for("home"))


# ---------- DELETE TRIP ----------
@app.route("/delete_trip/<int:i>", methods=["POST"])
def delete_trip(i):
    trips.pop(i)
    return redirect(url_for("home"))


# ---------- RUN APP ----------
if __name__ == "__main__":
    app.run(debug=True)
