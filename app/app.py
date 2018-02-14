import can
import time
bus0 = can.interface.Bus(channel='can0', bustype='socketcan_native')
bus1 = can.interface.Bus(channel='can1', bustype='socketcan_native')
msg = can.Message(arbitration_id=0x7de, data=[0, 25, 0, 1, 3, 1, 4, 1])
notifier = can.Notifier(bus1, [can.Printer()])

while True:
    bus0.send(msg)
    time.sleep(10)   # Delay for 10 seconds.
