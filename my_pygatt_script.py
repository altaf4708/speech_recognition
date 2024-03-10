import pygatt

# Create a BLE adapter object
adapter = pygatt.GATTToolBackend()

try:
    # Start the BLE adapter
    adapter.start()

    # Connect to the Bluetooth device
    device = adapter.connect("4F:51:49:69:8B:58")  # Replace with the address of your Bluetooth device

    # Perform Bluetooth operations (e.g., read/write characteristics)

finally:
    # Stop the BLE adapter when done
    adapter.stop()
