---
layout: page
title: "How to Remove Metadata from Video Files "
categories:
  - Instructions
---



## Installation

```bash
# (Optional)
$ sudo sh -c 'echo "deb https://mkvtoolnix.download/ubuntu/ $(lsb_release -sc) main" >> /etc/apt/sources.list.d/bunkus.org.list'
$ wget -q -O - https://mkvtoolnix.download/gpg-pub-moritzbunkus.txt | sudo apt-key add -

# Install
$ sudo apt-get update
$ sudo apt-get install mkvtoolnix mkvtoolnix-gui
```

## Usage

If you wish to remove the title metadata from a file, you use

```bash 
$ mkvpropedit name_of_file.mkv -d title
```

If you wish to do so for a batch of files

```bash
for x in **/*mp4; do mkvpropedit "${x}" -d title; done
```
