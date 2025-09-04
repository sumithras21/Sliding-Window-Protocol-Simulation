import socket
import random

RECEIVER_IP = "0.0.0.0"
RECEIVER_PORT = 12345

try:
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receiver_socket.bind((RECEIVER_IP, RECEIVER_PORT))
    receiver_socket.listen(1)
    print(f"Receiver is listening on {RECEIVER_IP}:{RECEIVER_PORT}")

    conn, addr = receiver_socket.accept()
    print(f"Connected to Sender at {addr}")

    expected_seq_num = 0

    def simulate_loss():
        return random.random() < 0.2

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        print(f"Received: {data}")
        seq_num = int(data.split()[1].replace(":", ""))

        if simulate_loss():
            print(f"Packet {seq_num} lost!")
            continue

        if seq_num == expected_seq_num:
            print(f"Packet {seq_num} processed!")
            ack = f"ACK {seq_num}"
            conn.sendall(ack.encode())
            expected_seq_num += 1
        else:
            print(f"Out-of-order packet {seq_num}, sending NAK")
            conn.sendall("NAK".encode())
except KeyboardInterrupt:
    print("\nReceiver stopped by user.")
except Exception as e:
    print(f"Error: {e}")
finally:
    receiver_socket.close()
    print("Receiver socket closed.")
