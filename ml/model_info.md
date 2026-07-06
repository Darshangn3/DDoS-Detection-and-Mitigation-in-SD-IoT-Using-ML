# Machine Learning Model

## Algorithm

- **Random Forest Classifier**

## Purpose

- Detect DDoS attacks in Software Defined IoT (SD-IoT) networks.
- Classify network traffic as Normal or Attack.
- Enable real-time DDoS detection and mitigation using the Ryu SDN controller.

## Input Features

- Packet Count
- Total Bytes
- Average Packet Size
- SYN Count
- ACK Count
- Unique Source IPs & ports
- Unique Destination IPs & ports
- flow duration

## Libraries Used

- Scikit-learn
- Pandas
- NumPy
- Joblib

## Model Output

- Trained Model: `ddos_rf_model.pkl`

## Notes

- The model is trained using statistical traffic features extracted from network packet captures.
- The trained model is loaded by the Ryu SDN controller for real-time DDoS attack detection.
- When malicious traffic is detected, the controller automatically installs OpenFlow drop rules to block the attacker.