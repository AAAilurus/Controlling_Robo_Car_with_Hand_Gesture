from flask import Flask, request, jsonify
import serial

app = Flask(__name__)

# Set up Bluetooth serial connection
try:
    arduino_serial = serial.Serial("/dev/rfcomm0", baudrate=9600, timeout=1)
    print("Bluetooth connected to Arduino successfully!")
except Exception as e:
    print("Failed to connect to HC-05 Bluetooth:", e)
    arduino_serial = None

@app.route("/command", methods=["POST"])
def handle_command():
    data = request.get_json()

    if not data or "command" not in data:
        return jsonify({"error": "No command received"}), 400

    command = data["command"]
    print("Received command from client:", command)

    if arduino_serial and arduino_serial.isOpen():
        arduino_serial.write(command.encode())  # Convert to bytes and send
        return jsonify({"status": f"Command '{command}' sent to Arduino"}), 200
    else:
        return jsonify({"error": "Bluetooth serial not available"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) # hosting
