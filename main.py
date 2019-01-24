from IRControlSystem.receiver import Receiver
from IoTClient.IoTClient import IoTClient
import redis
import json
import threading

from pip._vendor.distlib.compat import raw_input

from Events.Manager import Manager
import time

if __name__ == '__main__':
    r = redis.Redis(host="localhost", port=6379)

    p = r.pubsub()
    p.subscribe("event_change")
    client = IoTClient()

    thread = threading.Thread(target=client.run, args=())
    thread.daemon = True  # Daemonize thread
    thread.start()  # Start the execution

    receiver = Receiver()

    thread2 = threading.Thread(target=receiver.run, args=())
    thread2.daemon = True  # Daemonize thread
    thread2.start()  # Start the execution

    eventsManager = Manager()
    condition = threading.Condition()
    thread3 = threading.Thread(target=eventsManager.run, args=(condition,))
    thread3.daemon = True  # Daemonize thread
    thread3.start()  # Start the execution

    with open('Events/event_sample.json') as f:
        eventDocument = json.load(f)

    while True:
        message = p.get_message()
        if message:
            with condition:
                condition.notifyAll()
