from IoTClient import IoTClient
import threading

if __name__ == '__main__':
    client = IoTClient()

    thread = threading.Thread(target=client.run, args=())
    thread.daemon = True  # Daemonize thread
    thread.start()  # Start the execution