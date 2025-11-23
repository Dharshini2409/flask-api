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

@app.route('/invoice', methods=['POST'])
def invoice():
    data = request.get_json()
    order_id = data.get("order_id")

    if not order_id:
        return jsonify({"error": "order_id is required"}), 400

    if order_id == "ORD123":
        return jsonify({
            "order_id": "ORD123",
            "status": "Available",
            "invoice_link": "https://example.com/invoice/ORD123.pdf"
        })
    elif order_id == "ORD999":
        return jsonify({
            "order_id": "ORD999",
            "status": "Processing"
        })
    else:
        return jsonify({
            "order_id": order_id,
            "status": "Not Found"
        })

@app.route('/refundstatus', methods=['POST'])
def refund_status():
    data = request.get_json()

    order_id = data.get("order_id")

    if not order_id:
        return jsonify({"error": "order_id is required"}), 400

    # ----- Sample Refund Logic -----
    if order_id == "ORD123":
        return jsonify({
            "order_id": order_id,
            "status": "Refund Initiated",
            "amount": "₹500"
        })
    elif order_id == "ORD555":
        return jsonify({
            "order_id": order_id,
            "status": "Refund Completed",
            "amount": "₹750"
        })
    else:
        return jsonify({
            "order_id": order_id,
            "status": "Not Found",
            "amount": ""
        })
    
@app.route('/trackshipment', methods=['POST'])
def track_shipment():
    data = request.get_json()
    tracking_id = data.get("tracking_id")

    # Validate
    if not tracking_id:
        return jsonify({"error": "tracking_id is required"}), 400

    # ---- Example Shipment Data ----
    if tracking_id == "TRK123":
        return jsonify({
            "tracking_id": tracking_id,
            "status": "In Transit",
            "current_location": "Chennai",
            "expected_delivery": "2025-11-28"
        })

    elif tracking_id == "TRK777":
        return jsonify({
            "tracking_id": tracking_id,
            "status": "Delivered",
            "delivered_on": "2025-11-20"
        })

    elif tracking_id == "TRK999":
        return jsonify({
            "tracking_id": tracking_id,
            "status": "Pending Pickup"
        })

    else:
        return jsonify({
            "tracking_id": tracking_id,
            "status": "Not Found"
        })
    
@app.route('/')
def home():
    return "Flask API running..."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
