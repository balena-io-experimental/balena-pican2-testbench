# resin-pican2-testbench

### Installation

You need to set the following parameters in your config.txt:

```
dtoverlay=mcp2515-can0,oscillator=16000000,interrupt=25
dtoverlay=mcp2515-can1,oscillator=16000000,interrupt=24
dtoverlay=spi-bcm2835-overlay
```

### Usage

Once the container has started, open 2 App terminals from the dashboard.

In the first one, execute:

```
candump can1
```

In the second, execute:

```
cansend can0 456#43414e2054657374
```

Expected result: the message sent will appear in the dump
