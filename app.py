from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    message = data['message']
    window_size = data['windowSize']
    
    sender_logs = []
    receiver_logs = []

    # Simulation Logic
    base = 0
    next_seq_num = 0
    total_packets = len(message)

    def simulate_loss():
        import random
        return random.random() < 0.2

    while base < total_packets:
        while next_seq_num < base + window_size and next_seq_num < total_packets:
            sender_logs.append(f"Sending packet {next_seq_num}: {message[next_seq_num]}")
            next_seq_num += 1

        for seq in range(base, next_seq_num):
            if simulate_loss():
                sender_logs.append(f"Packet {seq} lost!")
                receiver_logs.append(f"Packet {seq} not received!")
                break
            else:
                sender_logs.append(f"Packet {seq} acknowledged.")
                receiver_logs.append(f"Received packet {seq}: {message[seq]}")
                base = seq + 1

    receiver_logs.append("Message fully received!")

    return jsonify({'senderLogs': sender_logs, 'receiverLogs': receiver_logs})

if __name__ == '__main__':
    app.run(debug=True)
