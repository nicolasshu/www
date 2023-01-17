---
layout: article
title: "Using Conbee II on Synology"
tags:
  - Server
  - Linux
permalink: /synology_conbeeii.html
mathjax: false
---


Task Scheduler -> Create

User: `root`

Task Settings -> Run command

```bash
/sbin/modprobe usbserial
/sbin/modprobe ftdi_sio
/sbin/modprobe cdc-acm
```

Unplug and plug in Conbee II again. You'll now see:

```
ls /dev/ttyA*
/dev/ttyACM0
```

Source: https://www.youtube.com/watch?v=S2Uu35xi11E