---
layout: article
title: "New NVIDIA Card on Linux"
tags:
  - Instructions
  - Linux
permalink: /nvidia_on_ubuntu_20_04.html
---

There are a few things that need to be done when first installing a new Linux system on a built PC. One problem that I had a bit was with regards to the monitors and the colors. When I first built a PC, with a new RTX 2070, it couldn't handle more than 1 monitor, nor could it use the Night Color/Light (or Redshift) options until I installed the correct drivers, which I learned from [Ashley Tharp's post](https://medium.com/@ashley.tharp/ubuntu-18-04b-solved-could-not-see-second-monitor-nvidia-graphics-card-a9cb67317288). Prior to reading such post, nothing was working in either Ubuntu 18.04, Ubuntu 20.04, Kubuntu 18.04, Kubuntu 20.04, Pop_OS 20.04.

```bash
$ lsb_release -a
No LSB modules are available
Distributor ID: Ubuntu
Description:    Ubuntu 20.04 LTS
Release:        20.04
Codename:       focal
```

First, get the current version of the pci.ids
```bash
sudo update-pciids
```

Next, figure out what graphics card you have:
```bash
lspci -nn | grep 'VGA'
```

My output is
```
7:00.0 VGA compatible controller [0300]: NVIDIA Corporation TU106 [GeForce RTX 2070 Rev. A] [10de:1f07]
```

So next go get the new drivers from the NVIDIA website

https://www.nvidia.com/Download/index.aspx

In my case, I placed the following parameters

| Keys             | Parameters            |
| ---------------- | --------------------- |
| Product Type     | GeForce               |
| Product Series   | GeForce RTX 20 Series |
| Product          | GeForce RTX 2070      |
| Operating System | Linux 64-bit          |
| Download Type    | Linux Long Lived      |
| Language         | English (US`)         |

And then I downloaded the respective `*.run` file.

Next, I installed some prerequisites

```bas
sudo apt install gcc make cmake
```

Next, go to where you downloaded the file, make it executable, and then run it

```bas
sudo chmod +x NVIDIA-Linux-x86_64-450.57.run
sudo ./NVIDIA-Linux-x86_64-450.57.run
```

Select the following:

1. An alternate method of installing the NVIDIA driver was detected. (This is usually a package provided by your distributor.) A driver installed via that method may integrate better with your system than a driver installed by nvidia-installer. Please review the message provided by the maintainer of this alternate installation method and decide how to proceed:
   - Continue installation
2. Install NVIDIA's 32-bit compatibility libraries?
   - Yes
3. WARNING: Unable to determine the path to install the libglvnd EGL vendor library config files. Check that you have pkg-config and the libglvnd development libraries installed, or specify a path with --glvnd-egl-config-path
   - OK
4. Would you like to run the nvidia-xconfig utility to automatically update your X configuration file so that the NVIDIA X driver will be used when you restart X? Any pre-existing X configuration file will be backed up.
   - Yes
5. Your X configuration file has been successfully updated. Installation of the NVIDIA Accelearated Graphics Driver for Linux-x86_64 (version: 450.57) is now complete.
   - OK
