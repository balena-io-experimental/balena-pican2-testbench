# Bring CAN bus 1 up
/sbin/ip link set can1 up type can bitrate 500000

python3 /usr/src/app/app.py

echo "Starting listening to can1"

candump can1
