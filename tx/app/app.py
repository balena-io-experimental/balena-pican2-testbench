import can

# Set can0 as TX bus and send example msg
bus_TX = can.interface.Bus(channel='can0', bustype='socketcan_native')
msg = can.Message(arbitration_id=0x7de,data=[0, 25, 0, 1, 3, 1, 4, 1])
bus_TX.send(msg)
