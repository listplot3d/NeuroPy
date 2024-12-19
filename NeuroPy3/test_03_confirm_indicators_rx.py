import time
import matplotlib.pyplot as plt
from NeuroPy3 import NeuroPy3  # 使用NeuroPy库连接设备

neuropy = NeuroPy3("COM5")


def attention_callback(value):
    print("attention Value is: ", value)
    return None


neuropy.setCallBack("attention", attention_callback)

neuropy.start()
try:
    while True:
        time.sleep(0.2)
except KeyboardInterrupt:
    print("\n* Session stopped\n")
finally:
    neuropy.stop()