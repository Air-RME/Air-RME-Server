from IoTClient.IoTClient import IoTClient
import threading

if __name__ == '__main__':
    client = IoTClient()

    client.run()

    # thread = threading.Thread(target=client.run, args=())
    # thread.daemon = True  # Daemonize thread
    # thread.start()  # Start the execution