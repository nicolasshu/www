---
layout: page
title: "Useful Applications for Ubuntu - Installation Instructions"
categories:
  - Instructions
---

*This is as of 2020-05-14*

Here's a list of applications that are nice for Ubuntu 18.04 
- [4K Video Downloader](https://www.4kdownload.com/products/product-videodownloader)
- [Albert](https://albertlauncher.github.io/)
- [Atom](https://atom.io/)
- [Android Messages]()
- [Blue Jeans / Blue Jeans Events (for GT)](https://www.bluejeans.com/)
- [Cisco AnyConnect](https://www.cisco.com/c/en/us/products/security/anyconnect-secure-mobility-client/index.html)
- [Deluge](https://deluge-torrent.org/)
- [F5 Endpoint / F5 VPN (for Emory University)](https://emory.service-now.com/kb_view.do?sysparm_article=KB00833)
- [EasyTag](https://wiki.gnome.org/Apps/EasyTAG)
- [Etcher](https://www.balena.io/etcher/)
- [Dropbox](https://www.dropbox.com/basic)
- [Discord](https://discord.com/)
- [Frescobaldi](https://frescobaldi.org/)
- [htop](https://hisham.hm/htop/) / [vtop](https://github.com/MrRio/vtop)
- [Kite Coding Assistant](https://kite.com/)
- [MEGASync](https://mega.nz/sync)
- [mkvtoolnix](https://mkvtoolnix.download/)
- [Papirus Icon Theme](https://github.com/PapirusDevelopmentTeam/papirus-icon-theme)
- [Pinta](https://pinta-project.com/pintaproject/pinta/)
- [Solaar](https://pwr-solaar.github.io/Solaar/)
- [Telegram](https://telegram.org/)
- [Tillix](https://gnunn1.github.io/tilix-web/)
- [Timeshift](https://teejeetech.in/timeshift/)
- [Typora](https://typora.io/)
- [VS Code](https://code.visualstudio.com/)
- [Xournal++](https://github.com/xournalpp/xournalpp)
- [Yakuake](https://github.com/KDE/yakuake)
- [Zoom](https://zoom.us/)
- [WhatsDesk](https://snapcraft.io/whatsdesk)


# Albert for Ubuntu 18.04 LTS
## Installation
```bash
$ sudo apt-get update
$ sudo apt-get install albert
```

## Uninstallation
```bash
$ sudo apt remove albert
```


# Android Messages 
## Installation
```bash 
$ npm install nativefier -g
```

## Uninstallation
```bash
$ npm uninstall -g nativefier
```

# Deluge
## Installation
```bash
$ sudo apt install deluge
```

## Uninstallation
```bash
$ sudo apt remove deluge
```

# EasyTag
## Installation
```bash
$ sudo apt update
$ sudo apt install easytag
```

## Uninstallation
```bash
$ sudo apt remove easytag
```

# Frescobaldi 
## Installation
```bash
$ sudo apt install frescobaldi
```

## Uninstallation
```bash
$ sudo apt remove frescobaldi
```

# htop / vtop 
## Installation
```bash
$ sudo apt install htop
$ npm install -g vtop
```

## Uninstallation
```bash
$ sudo apt remove htop
$ npm uninstall -g vtop
```

# MKVToolNix
## Installation

```bash
# (Optional)
$ sudo sh -c 'echo "deb https://mkvtoolnix.download/ubuntu/ $(lsb_release -sc) main" >> /etc/apt/sources.list.d/bunkus.org.list'
$ wget -q -O - https://mkvtoolnix.download/gpg-pub-moritzbunkus.txt | sudo apt-key add -

# Install
$ sudo apt-get update
$ sudo apt-get install mkvtoolnix mkvtoolnix-gui
```

## Uninstallation

Go to `Software & Updates > Other Software` and delete `https://mkvtoolnix.download/ubuntu/ bionic main`

And then run in your terminal
```bash
$ sudo apt-get remove --autoremove mkvtoolnix mkvtoolnix-gui
```

# Papirus
## Installation 
```bash
$ sudo add-apt-repository ppa:papirus/papirus
$ sudo apt update
$ sudo apt install papirus-icon-theme 
```

# Pinta
## Installation
```bash
$ sudo apt install pinta
```


## Uninstallation
```bash
$ sudo apt remove pinta
```


# Solaar 

## Installation
```bash
$ sudo apt update
$ sudo apt install solaar
```

## Uninstallation
```bash
$ sudo apt remove solaar
```


# Tilix

## Installation
```bash
$ sudo apt update 
$ sudo apt install tilix
```

## Uninstallation
```bash
$ sudo apt remove tilix
```

## Additional
You can also make it use as a Quake Terminal with 
```
$ tilix --quake
``` 

And thus, by adding it to a shortcut assigned as a function key (e.g. F12) you might not need [Yakuake](#yakuake)


# Timeshift
## Installation
```bash
$ sudo add-apt-repository ppa:teejee2008/ppa
$ sudo apt-get update
$ sudo apt-get install timeshift
```

## Uninstallation 
In `Software & Updates > Other Software`, remove `ppa:teejee2008/ppa` and then run 

```bash
$ sudo apt remove timeshift
```


# Typora
## Installation
```bash
$ sudo apt update
$ sudo apt install typora
```

## Uninstallation
```bash
$ sudo apt remove typora
```


# Xournal++

## Installation
### Option 1: Sofware Center (Preferred)
In `Ubuntu Software`, search Xournal++ and install it

### Option 2: Terminal
```
$ sudo add-apt-repository ppa:andreasbutti/xournalpp-master
$ sudo apt update
$ sudo apt install xournalpp
```

## Uninstallation
If you used Software Center, simply uninstall it there. If you installed via the terminal, in `Software & Updates > Other Software`, remove `ppa:andreasbutti/xournalpp-master` and then run 

```
$ sudo apt remove xournalpp
```

# Yakuake
## Installation
```bash
$ sudo snap install yakuake --candidate
```
## Uninstallation
```bash
$ sudo snap remove yakuake 
```