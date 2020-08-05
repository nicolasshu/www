---
layout: page
title: "Glitched Linux Startup/Installation"
categories:
  - Instructions
---

If you are dealing with a glitched Linux startup or installation, in order to fix it, as per [fossfreedom's](https://askubuntu.com/a/38834/754346) and [Coldfish's](https://askubuntu.com/a/38782/754346) answers, 

## Option 1 - fossfreedom

Edit the Grub boot process, press `e` to edit the kernel displayed, and change the line which has `quiet splash` to `nomodeset quiet splash`

For example, before:
```
recordfail=1
save_env recordfail
set quiet=1
insmod ext2
set root=(hd0,1)
search --no-floppy --fs-uuid --set 904bf39-9234
linux /boot/vmlinuz-2.6.31-9 root=UUID=904bf39-9234 ro quiet splash
initrd /bood/initrd.img-2.6.31-9-generic
```

And after:
```
recordfail=1
save_env recordfail
set quiet=1
insmod ext2
set root=(hd0,1)
search --no-floppy --fs-uuid --set 904bf39-9234
linux /boot/vmlinuz-2.6.31-9 root=UUID=904bf39-9234 ro nomodeset quiet splash
initrd /bood/initrd.img-2.6.31-9-generic
```

and exit to boot.

## Option 2
Otherwise, you can login via Safe Mode, and edit your `/etc/default/grub` with 

```bash
sudo vim /etc/default/grub
```

and add `nomodeset` to `GRUB_CMDLINE_LINUX_DEFAULT`

```bash
GRUB_DEFAULT=0
GRUB_HIDDEN_TIMEOUT=0
GRUB_HIDDEN_TIMEOUT_QUIET=true
GRUB_TIMEOUT=5
GRUB_DISTRIBUTOR=`lsb_release -i -s 2> /dev/null || echo Debian`
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash nomodeset"
GRUB_CMDLINE_LINUX=""
```

Save, and update your Grub with 
```bash
sudo update-grub
```