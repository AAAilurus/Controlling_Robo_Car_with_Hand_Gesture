from flask import Flask, request
import serial

bt = serial.Serial('/dev/rfcomm0', 9600, timeout=1)

app = Flask(__name__)

@app.route('/command', methods=['POST'])
def send_command():
    data = request.get_json()
    cmd = data.get('command', '').upper()  

    if cmd in ['F', 'B', 'L', 'R', 'S']:
        bt.write(cmd.encode())
        print(f"Sent to Arduino: {cmd}")
        return {'status': 'ok', 'sent': cmd}
    else:
        return {'status': 'error', 'message': 'Invalid command'}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
