DDoS Attack Detection and Mitigation in SD-IoT Networks using Machine Learning

Overview

This project implements a Machine Learning-based Intrusion Prevention System (IPS) designed to detect and mitigate Distributed Denial-of-Service (DDoS) attacks in Software Defined Internet of Things (SD-IoT) environments.
Key Idea 
•	SDN separates control and data planes, allowing centralized monitoring.
•	The Ryu Controller collects traffic statistics from switches.
•	A Machine Learning model analyzes traffic patterns.
•	If malicious behavior is detected, the controller blocks the attacker automatically.
________________________________________

Objectives

•	Real-time detection of DDoS attacks using Machine Learning
•	Continuous monitoring of network flows via OpenFlow
•	Accurate classification of traffic (Normal vs Attack)
•	Automated mitigation using SDN controller logic
•	Maintain network availability and performance
________________________________________

Technologies Used

•	Python → Core programming language
•	Mininet → Network emulation
•	MiniEdit → GUI-based topology design
•	Ryu Controller → SDN controller
•	OpenFlow → Communication protocol between switches and controller
•	Scikit-learn → ML model training
•	Random Forest → Classification algorithm
•	Wireshark → Packet analysis
•	hping3 → Attack simulation tool
•	Ubuntu Linux 20.04 LTS→ Development environment
________________________________________

Project Architecture

Components Explained
•	Mininet Network
o	Simulates IoT devices, switches, and hosts
•	OpenFlow Switches
o	Forward packets and send statistics to controller
•	Ryu Controller
o	Central brain of the network
o	Collects flow statistics
o	Applies mitigation rules
•	Machine Learning Module
o	Processes traffic features
o	Predicts whether traffic is normal or malicious
________________________________________

Workflow

Step-by-Step Process
•	Start Mininet topology
•	Connect switches to Ryu controller
•	Generate normal traffic
•	Launch attack traffic
•	Collect flow statistics
•	Extract features
•	Run ML prediction
•	Apply mitigation if attack detected
________________________________________

Machine Learning Model

Model Details
•	Algorithm: Random Forest
•	Type: Supervised Learning
Input Features
•	Packet count
•	Byte count
•	Flow duration
•	Packet rate
Output
•	Normal Traffic
•	DDoS Attack
________________________________________

Results

Traffic Flow
•	Shows normal vs attack traffic behavior
Detection Output
•	Displays classification results
Confusion Matrix
•	Evaluates model performance
Model Accuracy
•	Measures prediction accuracy
________________________________________

Repository Structure 

root/
│
├── assets/│
├── topology /
├── ryu_controller/
├── dataset/
├── scripts/│
├── ml/
├── results/
├── README.md                  
├── requirements.txt           
└── LICENSE                    
________________________________________

Repository Contents

topology/
Contains Mininet topology scripts used to simulate the SD-IoT network environment. 

dataset/
Contains captured traffic data and processed datasets used for training and testing the ML model. 

ryu_controller/
Contains the Ryu SDN controller responsible for:
•	Flow monitoring
•	Feature extraction
•	Traffic classification
•	DDoS mitigation
•	OpenFlow rule installation

scripts/
Contains shell scripts for:
•	Generating DDoS attacks using hping3
•	Capturing network traffic
•	Testing connectivity between hosts

models/
Contains trained Machine Learning models and related files used for traffic classification. 

result/
•	Controller output
•	Evaluation results
•	Attack detection

docs/
Project documentation including architecture, workflow, dataset description, and future scope.
________________________________________

Installation

Clone the repository
git clone https://github.com/Darshangn3/DDoS-Detection-and-Mitigation-in-SD-IoT-using-ML.git

Move into the project directory
cd DDoS-Detection-and-Mitigation-in-SD-IoT-using-ML

Install dependencies
pip install -r requirements.txt
________________________________________

Running the Project

Start the Ryu Controller
ryu-manager controller/ryu_controller.py

Launch the Mininet topology
sudo python3 topology/topology.py

Generate attack traffic
bash scripts/syn_flood.sh
________________________________________

Learning Outcomes

•	Software Defined Networking (SDN) architecture
•	Mininet network simulation
•	OpenFlow protocol and flow rule management
•	Ryu SDN Controller 
•	hping3
•	Feature extraction 
•	Machine Learning for intrusion detection
•	Random Forest classifier
•	Real-time DDoS attack detection and mitigation
•	Integration of networking and machine learning concepts
•	Measures prediction accuracy
________________________________________

Future Improvements

•	Support for multiple attack types
•	Integration of Deep Learning models (LSTM, CNN)
•	Explainable AI techniques (SHAP, LIME)
•	Real-time monitoring dashboard
________________________________________

