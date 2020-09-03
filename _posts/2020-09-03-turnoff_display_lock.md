---
layout: page
title: "Turn Off Display with Lock (KDE 5.18)"
categories:
  - Instructions
---

When using KDE 5.18, in order to make your computer turn off its display after locking the screen, do the following. 

Go to your __Systems Settings__, and go to the __Notifications__ section

Next, in the __Applications__, click on the _Configure..._ button. This will open a dialog of "Notifications -> Application Settings"

Next, select the __Screen Saver__ application, and click on the _Configure Events..._ button. 

Next, select the action of your choice (i.e. "_Screen locked_"), check the box _Run command_, and then enter the command below. The command below will run as soon as the screen gets locked. 

```
/bin/sleep 5; /usr/bin/xset dpms force off
```
