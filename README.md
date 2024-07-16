# README.txt

## Network Traffic Monitoring System

This project monitors network traffic, logs data to a CSV file, and provides alerts for high traffic via email. It includes a web interface for visualizing the data. The project is built using Python, Flask, Scapy, and D3.js.

### Project Structure

- `monitor.py`: Captures network packets and logs the data to a CSV file.
- `app.py`: Provides a web interface to visualize the logged network traffic data.
- `alert.py`: Checks the logged data for high traffic and sends email alerts if thresholds are exceeded.
- `run_alerts.bat`: A batch script to run `alert.py` in a loop with a delay.
- `run_batch.py`: Python script to run `run_alerts.bat`.
- `static/styles.css`: Stylesheet for the web interface.
- `templates/index.html`: HTML template for the web interface.

### Prerequisites

- Python 3.x
- `venv` (Python virtual environment)
- Pip (Python package installer)

### Setup

1. **Clone the repository:**
   ```sh
   git clone <repository_url>
   cd NetworkMonitoringSystem
   ```

2. **Create and activate the virtual environment:**
   ```sh
   python -m venv myvenv
   source myvenv/bin/activate   # On Windows use: myvenv\Scripts\activate
   ```

3. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```

### Running the Project

#### 1. Monitor Network Traffic

To start monitoring network traffic and logging data to the CSV file:

```sh
python monitor.py
```

#### 2. Run the Web Interface

To start the Flask web server and view the network traffic data:

```sh
python app.py
```

Open your web browser and navigate to `http://127.0.0.1:5000` to see the network traffic visualization.

#### 3. Alert System

The alert system checks for high network traffic and sends email alerts if the traffic exceeds a specified threshold.

1. **Configure Email Alerts:**

   Update the following configurations in `alert.py` with your email details:
   - `EMAIL_ADDRESS`: Your email address.
   - `EMAIL_PASSWORD`: Your email app password.
   - `ALERT_RECIPIENT`: Recipient's email address.

2. **Run the Alert System:**

   To continuously run the alert system, execute the batch script:
   ```sh
   python run_batch.py
   ```

### Additional Information

- **CSV File Path:** The path to the CSV file where network traffic data is logged is defined in `csv_file_path` variable in each script.
- **Email Configuration:** Ensure that your email settings in `alert.py` are correctly configured to send emails using SMTP.
- **Data Visualization:** The web interface refreshes every 5 seconds to display the latest data.

### Troubleshooting

- **Virtual Environment Issues:** Ensure that the virtual environment is activated before running the scripts.
- **Package Installation Issues:** Verify that all required packages are installed by checking the `requirements.txt` file.
- **Email Sending Issues:** Check your email configuration in `alert.py` and ensure that your email service allows SMTP access.


---

This README file provides detailed instructions for setting up, running, and maintaining the Network Traffic Monitoring System. For any further assistance, please contact the project maintainer.