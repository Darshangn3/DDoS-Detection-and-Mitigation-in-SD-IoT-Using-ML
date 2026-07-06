# DDoS Attack Detection and Mitigation in SD-IoT Networks using Machine Learning

## Overview

This project implements a **Machine Learning-based Intrusion Prevention System (IPS)** designed to detect and mitigate **Distributed Denial-of-Service (DDoS)** attacks in **Software Defined Internet of Things (SD-IoT)** environments.

### Key Idea

- SDN separates the **Control Plane** and **Data Plane**, allowing centralized monitoring.
- The **Ryu Controller** collects traffic statistics from OpenFlow switches.
- A **Machine Learning** model analyzes network traffic patterns.
- If malicious behavior is detected, the controller automatically blocks the attacker.

---

## Objectives

- Real-time detection of DDoS attacks using Machine Learning
- Continuous monitoring of network flows via OpenFlow
- Accurate classification of traffic (Normal vs Attack)
- Automated mitigation using SDN controller logic
- Maintain network availability and performance

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Mininet | Network emulation |
| MiniEdit | GUI-based topology design |
| Ryu Controller | SDN controller |
| OpenFlow | Communication protocol between switches and controller |
| Scikit-learn | Machine Learning model training |
| Random Forest | Classification algorithm |
| Wireshark | Packet analysis |
| hping3 | Attack simulation tool |
| Ubuntu Linux 20.04 LTS | Development environment |

---

## Project Architecture

### Components Explained

### Mininet Network
- Simulates IoT devices, switches, and hosts.

### OpenFlow Switches
- Forward packets.
- Send flow statistics to the controller.

### Ryu Controller
- Central brain of the network.
- Collects flow statistics.
- Applies mitigation rules.

### Machine Learning Module
- Processes traffic features.
- Predicts whether traffic is normal or malicious.

---

## Workflow

### Step-by-Step Process

1. Start the Mininet topology.
2. Connect switches to the Ryu Controller.
3. Generate normal traffic.
4. Launch attack traffic.
5. Collect flow statistics.
6. Extract traffic features.
7. Run Machine Learning prediction.
8. Apply mitigation if an attack is detected.

---

## Machine Learning Model

### Model Details

- **Algorithm:** Random Forest
- **Type:** Supervised Learning

### Input Features

- Packet Count
- Byte Count
- Flow Duration
- Packet Rate

### Output

- Normal Traffic
- DDoS Attack

---

## Results

### Traffic Flow
- Shows normal vs attack traffic behavior.

### Detection Output
- Displays classification results.

### Confusion Matrix
- Evaluates model performance.

### Model Accuracy
- Measures prediction accuracy.

---

## Repository Structure

```text
DDoS-Detection-and-Mitigation-in-SD-IoT-Using-ML/
│
├── assets/
├── attack_scripts/
├── controller/
├── dataset/
├── docs/
├── ml/
├── results/
├── topology/
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Repository Contents

### topology/

Contains Mininet topology scripts used to simulate the SD-IoT network environment.

---

### dataset/

Contains captured traffic data and processed datasets used for training and testing the Machine Learning model.

---

### controller/

Contains the Ryu SDN Controller responsible for:

- Flow monitoring
- Feature extraction
- Traffic classification
- DDoS mitigation
- OpenFlow rule installation

---

### attack_scripts/

Contains shell scripts for:

- Generating DDoS attacks using hping3
- Capturing network traffic
- Testing connectivity between hosts

---

### ml/

Contains trained Machine Learning models and related files used for traffic classification.

---

### results/

Contains:

- Controller output
- Evaluation results
- Attack detection results

---

### docs/

Contains project documentation including:

- Architecture
- Workflow
- Dataset description
- Future scope

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/Darshangn3/DDoS-Detection-and-Mitigation-in-SD-IoT-Using-ML.git
```

### Move into the Project Directory

```bash
cd DDoS-Detection-and-Mitigation-in-SD-IoT-Using-ML
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Start the Ryu Controller

```bash
ryu-manager controller/ryu_controller.py
```

### Launch the Mininet Topology

```bash
sudo python3 topology/topology.py
```

### Generate Attack Traffic

```bash
bash attack_scripts/syn_flood.sh
```

---

## Learning Outcomes

This project provides practical experience in:

- Software Defined Networking (SDN) architecture
- Mininet network simulation
- OpenFlow protocol and flow rule management
- Ryu SDN Controller
- hping3 attack simulation
- Traffic feature extraction
- Machine Learning for intrusion detection
- Random Forest classifier
- Real-time DDoS attack detection and mitigation
- Integration of networking and Machine Learning concepts
- Network traffic analysis and performance evaluation

---

## Future Improvements

- Support multiple DDoS attack types
- Integrate Deep Learning models (LSTM, CNN)
- Implement Explainable AI techniques (SHAP, LIME)
- Develop a real-time monitoring dashboard

---

## License

This project is licensed under the **MIT License**.
