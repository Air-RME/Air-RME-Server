from IoTClient.IoTClient import IoTClient
from IRControlSystem.ir.receiver import Receiver
import threading
import time

if __name__ == '__main__':
    client = IoTClient()

    # client.run()

    thread = threading.Thread(target=client.run, args=())
    thread.daemon = True  # Daemonize thread
    thread.start()  # Start the execution

    receiver = Receiver()

    thread = threading.Thread(target=receiver.run, args=())
    thread.daemon = True  # Daemonize thread
    thread.start()  # Start the execution

    while True:
        time.sleep(1)
