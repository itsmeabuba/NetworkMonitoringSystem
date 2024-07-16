import scapy.all as scapy
import datetime
import csv
import os

# CSV file path
csv_file_path = 'network_traffic.csv'  # Path to the CSV file

# Ensure the CSV file exists and has headers
def initialize_csv():
    if not os.path.exists(csv_file_path):  # Check if the file doesn't exist
        with open(csv_file_path, mode='w', newline='') as file:  # Open the file in write mode
            writer = csv.writer(file)
            writer.writerow(['date', 'time', 'src_ip', 'dst_ip', 'protocol', 'length'])  # Write headers

def packet_callback(packet):
    if scapy.IP in packet:  # Check if the packet has an IP layer
        now = datetime.datetime.now()  # Get the current timestamp
        date_str = now.strftime('%Y-%m-%d')  # Format the date
        time_str = now.strftime('%H:%M:%S.%f')  # Format the time
        src_ip = packet[scapy.IP].src  # Source IP address
        dst_ip = packet[scapy.IP].dst  # Destination IP address
        protocol = packet[scapy.IP].proto  # Protocol used
        length = len(packet)  # Length of the packet

        with open(csv_file_path, mode='a', newline='') as file:  # Open the file in append mode
            writer = csv.writer(file)
            writer.writerow([date_str, time_str, src_ip, dst_ip, protocol, length])  # Write packet data to the CSV file

# Initialize the CSV file
initialize_csv()

# Start sniffing
scapy.sniff(prn=packet_callback, store=0)  # Sniff packets and call packet_callback for each packet
