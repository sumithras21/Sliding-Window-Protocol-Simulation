# Sliding-Window-Protocol-Simulation
A Python-based Sliding Window Protocol Simulation with packet loss handling and a Flask web interface.

---

##  Overview
This project demonstrates a Sliding Window Protocol (Go-Back-N) simulation using Python Sockets and Flask.  
It includes:
- Sender & Receiver scripts for real-time simulation  
- Packet Loss Simulation to mimic real network issues  
- Sliding Window Mechanism for reliable and efficient data transfer  
- Flask Web Interface for easy visualization  

---

##  Features
- TCP-based communication between sender and receiver  
- Configurable window size for sending packets  
- Random packet loss simulation (20%) for testing reliability  
- Automatic retransmission on timeout or packet loss  
- **Web-based simulation using Flask for visualization  

---

##  Project Structure

├── sender.py         # Sender script using Go-Back-N protocol
├── receiver.py       # Receiver script with packet loss simulation
├── app.py            # Flask web application for simulation
├── static/index.html # Web interface for simulation
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation


---

##  Installation

Clone the repository:

git clone https://github.com/<your-username>/Sliding-Window-Protocol-Simulation.git
cd Sliding-Window-Protocol-Simulation


Install dependencies:

pip install -r requirements.txt

##  How to Run

### 1.  Socket-based Simulation (Command Line)

Start the Receiver:

python receiver.py

Start the Sender:

python sender.py


You will be prompted for:

* Receiver IP (e.g., `127.0.0.1`)
* Window Size (e.g., `4`)
* Message (e.g., `HELLO`)


### 2.  Web-based Simulation (Flask)

Run the Flask app:


python app.py

Open your browser and visit: http://127.0.0.1:5000

##  Example Output (Socket)


Receiver is listening on 0.0.0.0:12345
Connected to Sender at ('127.0.0.1', 54321)
Received: Packet 0: H
Packet 0 processed!
Packet 1 lost! Retransmitting...

##  Technologies Used

* Python (Sockets, Flask)
* HTML/CSS for Web Interface
* TCP Protocol for reliable communication


##  License

This project is open-source and free to use for educational purposes.


