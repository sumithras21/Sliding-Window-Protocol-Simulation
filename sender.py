import socket

# Sender Configuration
RECEIVER_IP = input("Enter Receiver's IP address: ")
RECEIVER_PORT = 12345
WINDOW_SIZE = int(input("Enter Window Size: "))
MESSAGE = input("Enter the message to send: ")

try:
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sender_socket.connect((RECEIVER_IP, RECEIVER_PORT))
    print(f"Connected to Receiver at {RECEIVER_IP}:{RECEIVER_PORT}")

    base = 0
    next_seq_num = 0
    total_packets = len(MESSAGE)

    def send_packet(seq_num):
        packet = f"Packet {seq_num}: {MESSAGE[seq_num]}"
        sender_socket.sendall(packet.encode())
        print(f"Sent: {packet}")

    while base < total_packets:
        while next_seq_num < base + WINDOW_SIZE and next_seq_num < total_packets:
            send_packet(next_seq_num)
            next_seq_num += 1

        try:
            ack = sender_socket.recv(1024).decode()
            print(f"Received: {ack}")
            if ack.startswith("ACK"):
                ack_num = int(ack.split()[1])
                base = ack_num + 1
            elif ack == "NAK":
                print("NAK received, retransmitting...")
                next_seq_num = base
        except socket.timeout:
            print("Timeout, retransmitting...")
            next_seq_num = base
except Exception as e:
    print(f"Error: {e}")
finally:
    sender_socket.close()
    print("Sender socket closed.")
