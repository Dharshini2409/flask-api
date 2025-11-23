from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/paymentstatus', methods=['POST'])
def payment_status():
    data = request.get_json()
    payment_id = data.get("payment_id")

    if not payment_id:
        return jsonify({"error": "payment_id required"}), 400

    if payment_id == "PAY123":
        return jsonify({
            "payment_id": payment_id,
            "status": "Success",
            "amount": "₹500"
        })
    elif payment_id == "PAY999":
        return jsonify({
            "payment_id": payment_id,
            "status": "Failed",
            "amount": ""
        })
    else:
        return jsonify({
            "payment_id": payment_id,
            "status": "Not Found",
            "amount": ""
        })

@app.route('/checkrates', methods=['POST'])
def check_rates():
    data = request.get_json()

    pickup = data.get("pickup")
    drop = data.get("drop")

    # Validate
    if not pickup or not drop:
        return jsonify({"error": "pickup and drop are required"}), 400

    # ----- Simple Rate Logic -----
    # Example: flat rate based on pickup-drop pair
    if pickup.lower() == "chennai" and drop.lower() == "bangalore":
        rate = 500
        estimate = "2 days"
    elif pickup.lower() == "chennai" and drop.lower() == "mumbai":
        rate = 900
        estimate = "4 days"
    else:
        # default rate
        rate = 300
        estimate = "3 days"

    return jsonify({
        "pickup": pickup,
        "drop": drop,
        "rate": rate,
        "estimate": estimate
    })

@app.route('/')
def home():
    return "Flask API running..."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
