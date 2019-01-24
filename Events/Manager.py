import redis
import json


class Manager:
    def run(self, condition):
        r = redis.Redis(host="localhost", port=6379)
        p = r.pubsub()
        p.subscribe("events")

        while True:
            message = p.get_message()
            if message:
                if type(message['data']) is not bytes:
                    continue
                data = json.loads(message['data'].decode('utf-8'))
                print(data)
            else:
                with condition:
                    condition.wait()
