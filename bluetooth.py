import bluetooth

# Create a Bluetooth socket
client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# Set up Bluetooth connection XX:XX:XX:XX:XX:XXparameters
server_address = "1d:c1:b7:14:1d:6a"  # Replace with the MAC address of the Bluetooth device you want to connect to
port = 1  # RFCOMM port number, typically 1 for most devices

# Connect to the Bluetooth device
client_socket.connect((server_address, port))

# Transmit data
data = "Hello, Bluetooth!"  # Example data to transmit
client_socket.send(data)

# Close the socket
client_socket.close()
