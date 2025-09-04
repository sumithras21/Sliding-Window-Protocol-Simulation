# Sliding-Window-Protocol-Simulation
A Python-based Sliding Window Protocol Simulation with packet loss handling and Flask web interface
# Sliding Window Protocol Simulation (Go-Back-N)

This project demonstrates a **Sliding Window Protocol (Go-Back-N)** simulation using Python Sockets and Flask.  
It includes:
- **Sender & Receiver scripts** for real-time simulation  
- **Packet Loss Simulation** to mimic real network issues  
- **Sliding Window Mechanism** for reliable and efficient data transfer  
- **Flask Web Interface** for easy visualization  

---

## 🚀 Features
- **TCP-based communication** between sender and receiver  
- **Configurable window size** for sending packets  
- **Random packet loss simulation** (20%) for testing reliability  
- **Automatic retransmission** on timeout or packet loss  
- **Web-based simulation** using Flask for visualization  

---

## 📂 Project Structure
├── sender.py # Sender script using Go-Back-N protocol
├── receiver.py # Receiver script with packet loss simulation
├── app.py # Flask web application for simulation
├── index.html # Web interface for simulation
├── requirements.txt # Python dependencies
└── README.md # Project documentation


Install dependencies:

pip install -r requirements.txt

▶️ How to Run
1️⃣ Socket-based Simulation (Command Line)
Start Receiver:
python receiver.py

Start Sender:
python sender.py


You will be prompted for:

Receiver IP (e.g., 127.0.0.1)

Window Size (e.g., 4)

Message (e.g., HELLO)

Web-based Simulation (Flask)

Run the Flask app: python app.py

Then open in your browser: http://127.0.0.1:5000

Example Output (Socket)

Receiver is listening on 0.0.0.0:12345
Connected to Sender at ('127.0.0.1', 54321)
Received: Packet 0: H
Packet 0 processed!
Packet 1 lost! Retransmitting...

🧰 Technologies Used

1. Python (Sockets, Flask)
2. HTML/CSS for Web Interface
3. TCP Protocol for reliable communication
