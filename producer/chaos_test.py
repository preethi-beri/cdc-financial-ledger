import random
import os
import time

while True:
    action = random.choice(["stop", "start"])

    if action == "stop":
        print("Stopping Kafka...")
        os.system("docker stop kafka")

    else:
        print("Starting Kafka...")
        os.system("docker start kafka")

    time.sleep(30)