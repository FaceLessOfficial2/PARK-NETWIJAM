![Picsart_24-10-25_23-38-34-949](https://github.com/user-attachments/assets/97ca35b0-7b1e-4444-b2c7-177bcac2f587)

*tutorial on how to install and use the NETWIJAM network and Wi-Fi jammer tool. 


# NETWIJAM: Network and Wi-Fi Jammer Tool Tutorial

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Running the Tool](#running-the-tool)
5. [Understanding the Code](#understanding-the-code)
6. [Troubleshooting](#troubleshooting)

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Python 3.x
- Scapy
- Root privileges (the tool must be run as root)

You can install Python and Scapy using the following commands:

```bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install scapy
```

---

## Installation

1. **Clone the Repository**:
   Clone the NETWIJAM repository from GitHub:

   ```bash
   git clone https://github.com/yourusername/NETWIJAM.git
   cd NETWIJAM
   ```

2. **Create Configuration File**:
   Create a `config.ini` file in the same directory as the script. Here's an example configuration file:

   ```ini
   [interface]
   name = wlan0

   [targets]
   targets = 00:11:22:33:44:55, 66:77:88:99:AA:BB
   ```

   Replace `wlan0` with your Wi-Fi interface name and add the MAC addresses of the targets you want to jam.

---

## Configuration

Ensure your `config.ini` file is correctly set up. Here’s a breakdown of the configuration:

```ini
[interface]
name = wlan0  # Replace with your Wi-Fi interface name

[targets]
targets = 00:11:22:33:44:55, 66:77:88:99:AA:BB  # Comma-separated list of MAC addresses
```

---

## Running the Tool

1. **Run the Script**:
   Execute the script with root privileges:

   ```bash
   sudo python3 NETWIJAM.py
   ```

2. **Monitor Mode**:
   The script will set your Wi-Fi interface to monitor mode. This is necessary for capturing and sending packets.

3. **Jamming Process**:
   The script will start capturing packets and sending deauthentication packets to the specified targets.

---

## Understanding the Code

Here’s a brief overview of the script:

- **Imports**:
  The script imports necessary modules for network operations and threading.

- **Configure Logging**:
  Logging is configured to provide detailed information and error messages.

- **Set Monitor Mode**:
  The script sets the specified Wi-Fi interface to monitor mode using `ifconfig` and `iwconfig`.

- **Jam Networks**:
  This function continuously captures packets and sends deauthentication packets to the specified targets.

- **Send Deauth Packets**:
  This function sends deauthentication packets to the specified MAC address.

- **Signal Handling**:
  The script handles signal interrupts to ensure a graceful shutdown.

- **Main Function**:
  The main function reads the configuration, sets the interface to monitor mode, starts the jamming process, and handles user input and signals.

---

## Troubleshooting

If you encounter issues, check the following:

1. **Permissions**:
   Ensure the script is run with root privileges (`sudo`).

2. **Interface Name**:
   Verify the Wi-Fi interface name in the `config.ini` file.

3. **Target MAC Addresses**:
   Ensure the MAC addresses in the `config.ini` file are correct.

4.## Troubleshooting (Continued)

5. **Logging**:
   Check the logs for any error messages. The script uses the `logging` module to provide detailed information about what is happening.

6. **Dependencies**:
   Ensure all required dependencies are installed. You can reinstall Scapy using:

   ```bash
   pip3 install --upgrade scapy
   ```

7. **Network Interface**:
   Ensure your Wi-Fi interface is up and running. You can check the status using:

   ```bash
   iwconfig
   ```

8. **Permissions**:
   Verify that you have the necessary permissions to run the script and set the interface to monitor mode.

---

### Example Logs

```plaintext
2024-10-28 12:34:56 - INFO - Set wlan0 to monitor mode
2024-10-28 12:35:01 - INFO - Detected AP: 00:11:22:33:44:55
2024-10-28 12:35:02 - INFO - Sent deauth packets to 00:11:22:33:44:55
```

### Common Issues and Solutions

1. **Interface Not Found**:
   - **Error**: `Interface not found`
   - **Solution**: Ensure the interface name in `config.ini` is correct and the interface is up.

2. **Permission Denied**:
   - **Error**: `Permission denied`
   - **Solution**: Run the script with `sudo` to gain root privileges.

3. **Scapy Not Installed**:
   - **Error**: `ModuleNotFoundError: No module named 'scapy'`
   - **Solution**: Install Scapy using `pip3 install scapy`.

4. **Monitor Mode Failed**:
   - **Error**: `Failed to set interface to monitor mode`
   - **Solution**: Ensure the interface supports monitor mode and try restarting the network service.

---

### Conclusion

**NETWIJAM is a powerful tool for network and Wi-Fi jamming. By following this tutorial, you should be able to install, configure, and run the tool effectively. Always remember to use such tools responsibly and within the bounds of the law and authorized testing environments.
