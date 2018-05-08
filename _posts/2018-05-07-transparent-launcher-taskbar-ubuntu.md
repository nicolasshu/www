---
layout: page
title: "Making the Launcher and Taskbar Transparent in Ubuntu 16.04"
categories:
  - Instructions
---
![Step]({{ "/assets/images/transparency/step14.png" | relative_url }})
### Goal
The goal of this post is to make the **launcher** and the **taskbar** of Ubuntu 16.04 to be transparent

### Steps
![Step]({{ "/assets/images/transparency/step1.png" | absolute_url }})
First, you'll start with everything being opaque.
1. Install Unity Tweak Tool with `sudo apt-get install unity-tweak-tool`
1. Open Unity Tweak Tool
![Step]({{ "/assets/images/transparency/step2.png" | absolute_url }})
1. Click on the "Launcher" category
![Step]({{ "/assets/images/transparency/step3.png" | absolute_url }})
![Step]({{ "/assets/images/transparency/step4.png" | absolute_url }})
1. Under the "Appearance" section, bring the *Transparency Level* to 100%
![Step]({{ "/assets/images/transparency/step5.png" | absolute_url }})
1. This will make the Launcher to be transparent
![Step]({{ "/assets/images/transparency/step6.png" | absolute_url }})
1. Install CompizConfig Settings Manager with `sudo apt-get install compizconfig-settings-manager`
![Step]({{ "/assets/images/transparency/step7.png" | absolute_url }})
1. Under the "Desktop" section, click on *Ubuntu Unity Plugin*
![Step]({{ "/assets/images/transparency/step8.png" | absolute_url }})
1. At this point, the "Background Color" should be **black**. Click on the color to change its settings
![Step]({{ "/assets/images/transparency/step10.png" | absolute_url }})
1. Bring the "Opacity" level down to **1** (If you set it to zero, it will reset the colors in the Launcher)
![Step]({{ "/assets/images/transparency/step11.png" | absolute_url }})
![Step]({{ "/assets/images/transparency/step12.png" | absolute_url }})
1. Now the Taskbar should also be transparent. Exit by clicking "Back" > "Close"
![Step]({{ "/assets/images/transparency/step13.png" | absolute_url }})
1. Yay! Done!
![Step]({{ "/assets/images/transparency/step14.png" | absolute_url }})
