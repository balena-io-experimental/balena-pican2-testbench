# Bring CAN bus 1 up
/sbin/ip link set can1 up type can bitrate 500000

python3 /usr/src/app/app.py
