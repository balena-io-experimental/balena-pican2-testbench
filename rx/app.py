import can
bus_RX = can.interface.Bus(channel='can1', bustype='socketcan_native')
notifier = can.Notifier(bus_RX, [can.Printer()])
