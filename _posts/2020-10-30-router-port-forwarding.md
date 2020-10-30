---
layout: article
title: "Port Forwarding with Netgear Routers"
tags:
  - Math
  - Machine Learning
permalink: /port_forwarding_netgear.html
mathjax: false
---

In order to forward a port in Netgear, first access your router. If you're connected to the router already, you can either reach it via http://www.routerlogin.net or via http://192.168.1.1

You'll be on the `BASIC` tab. Click on the `ADVANCED`. Now go to `Advanced Setup > Port Forwarding / Port Triggering`. Here's where you'll be allowing ports in computers to be accessed for remote purposes. 

So click on the button `+ Add Custom Service`. There, enter the following:

- **Service Name**: Choose any name 
- **Service Type**: TCP/UDP
- **External Port Range**: Choose the port that you wish to forward (e.g. 8080)
- **Internal Port Range**: Use the same as the "External Port Range"
- **Internal IP Address**: Enter or choose the machine that you wish its port to be exposed. 

Finally, click on the `Apply` button, and you should have access. 