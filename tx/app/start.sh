# Bring CAN bus 0 up
/sbin/ip link set can0 up type can bitrate 500000

while [[ true ]]; do
  echo "Sending test message from can0"
  cansend can0 456#43414e2054657374
  sleep 5
done
