# **Prometheus Alert Rules with Python Scripts**

This repository contains Prometheus alert rules implemented using Python scripts. Each Python script corresponds to a specific task such as increasing CPU utilization, increase the disk space, increase the request error and increasing memory utilization. Additionally, YAML files are provided to define the corresponding alert rules.

<br/>

## Getting Started
1. **Clone the Repository:**
- Clone this repository to your Linux machine.


2. **Install Prometheus and Node Exporter:**
- Download Prometheus and Node Exporter binaries suitable for your Linux environment.
- Extract the binaries to a directory on your machine.
- Make sure both Prometheus and Node Exporter binaries are executable.


3. **Configuration:**
- Modify the prometheus.yml file to include the configuration for scraping metrics from Node Exporter. Ensure that the Node Exporter endpoint is correctly specified.
- Add all alert YAML files (*.yml) to the prometheus.yml file under the alert_rules section.


4. **Run Prometheus and Node Exporter:**
- Navigate to the directory where Prometheus and Node Exporter binaries are located.
- Start Prometheus and Node Exporter by running the following commands: ./prometheus and ./node_exporter
- Prometheus running at port 9090


5. **Test Alerts:**
- Execute the Python scripts corresponding to the desired alert rules.
- Example : python3 memory_utilization.py

<br/>

## Usage
- **Prometheus Configuration:** Ensure that the prometheus.yml file is correctly configured to scrape metrics from Node Exporter, Flask node, and includes all alert rules.
  
- **Node Exporter and Flask Node:** Ensure both Node Exporter and Flask node are running and exposing metrics for Prometheus to scrape.

- **Python Scripts:** Each Python script is responsible for simulating a specific condition that might trigger an alert. You can customize these scripts or create new ones based on your requirements.
  
- **Alert Rules:** The YAML files define the alert rules that Prometheus will use to detect issues based on the metrics provided by the Python scripts.



