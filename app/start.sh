# Bring CAN bus 0 up
/sbin/ip link set can0 up type can bitrate 500000

# Bring CAN bus 1 up
/sbin/ip link set can1 up type can bitrate 500000

while [[ true ]]; do
  sleep 5
done
