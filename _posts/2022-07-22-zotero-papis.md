---
layout: article
title: "Zotero and papis"
permalink: /zotero_and_papis.html
tags:
  - Linux
---

So Zotero can be very helpful for citation management. There's a [guide](nicolasshu.com/zotero_setup.html) I previously wrote to setup Zotero. That setup allows you to set Zotero to be easily backed up. However, the way that Zotfile operates is that it only moves the PDF file to your synced folder. That setup is written so that it creates a flat directory for your synced folder. 

Recently, I also found a new repository called [papis](https://github.com/papis/papis). It provides a pretty nice TUI interface for your citation management, but it also is nicely maintained, it has a [variety of different repositories](https://github.com/papis) which go with it, along with a [rofi](https://github.com/papis/python-rofi), a [dmenu](https://github.com/papis/papis-dmenu), and an [emacs](https://github.com/papis/papis.el) package for it! It's pretty great!

It also has a [Zotero interface](https://github.com/papis/papis-zotero) which allows you to pull information from your Zotero and create your own papis library. But the way that it currently operates is that it creates a new library by using the key that the SQLite uses. In other words, it would have the structure of 

```
library/
  ├── 9Q2KKMZL
  |   ├── publication_A.pdf
  |   └── info.yaml
  └── EINISJX9
      ├── publication_B.pdf
      └── info.yaml
```

Although, papis is able to pick it up, but it's hard to look over it if you wanted to use a regular file manager to look into it. The current `papis-zotero` has a few bugs and documentation that could be improved, but I wanted to do something that would create a nice workflow to work with both. 

# Proposed Workflow

The proposed workflow is meant to use the Zotero connector or the Zotero application. 

```
PDFs & Files -> Zotero -> papers -> papis
```


This will require a few pieces of software to be used:

- [SyncThing](https://syncthing.net/) (or any other syncing software)
- [Zotero](https://www.zotero.org/)
- [papis](https://github.com/papis/papis)

It is meant so that the sychronizing software takes care of the backing up of the data, Zotero provides a database which you can use a GUI with, and we copy the relevant information to a desired directory which has the PDF files organized, any other file we attached to Zotero, along with the `info.yaml` needed for papis. 

# Prerequisites

## Zotero
In order to install Zotero, you can use 

```bash
pacman -S zotero-bin
```

## Papis

For papis, you can use use AUR's `aur/papis`, but, at the time of this writing, it is a bit out of date. So it's best if you use `pip`

```bash
pip3 install papis
# or
sudo pip3 install papis
```

## SyncThing

For SyncThing, you can use either `community/syncthing` or use a Docker container for it. For the Docker container, you may either use [linuxserver's syncthing](https://hub.docker.com/r/linuxserver/syncthing/#!) which has the Docker compose file:

```yaml
---
version: "2.1"
services:
  syncthing:
    image: lscr.io/linuxserver/syncthing:latest
    container_name: syncthing
    hostname: syncthing #optional
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/London
    volumes:
      - /path/to/appdata/config:/config
      - /path/to/data1:/data1
      - /path/to/data2:/data2
    ports:
      - 8384:8384
      - 22000:22000/tcp
      - 22000:22000/udp
      - 21027:21027/udp
    restart: unless-stopped
```

or [Syncthing's Syncthing](https://hub.docker.com/r/syncthing/syncthing/#!), which I think it is more often updated, and has the following Docker compose file below, which is taken from [here](https://github.com/syncthing/syncthing/blob/main/README-Docker.md)

```yaml
---
version: "3"
services:
  syncthing:
    image: syncthing/syncthing
    container_name: syncthing
    hostname: my-syncthing
    environment:
      - PUID=1000
      - PGID=1000
    volumes:
      - /wherever/st-sync:/var/syncthing
    ports:
      - 8384:8384 # Web UI
      - 22000:22000/tcp # TCP file transfers
      - 22000:22000/udp # QUIC file transfers
      - 21027:21027/udp # Receive local discovery broadcasts
    restart: unless-stopped
```

Read through this entire guide to know where to put the volumes first. 

# Setup

## Goal

The goal is to have the following:

```
~/sync/
  ├── papers/
  │   ├── publication_A/
  │   │   ├── publication_A.pdf
  │   │   └── info.yaml
  │   └── publication_B/
  │       ├── publication_B.pdf
  │       ├── code.py
  │       └── info.yaml
  └── zotero/
      ├── locate/
      ├── pipes/
      ├── storage/
      │   ├── GSFPIRZY/
      │   │   └── (used to have publication_A.pdf)
      │   └── RSERDEPY/
      │       ├── (used to have publication_A.pdf)
      │       └── code.py
      ├── styles/
      ├── translators/
      └── zotero.sqlite
```

## Directories

Now, how will we set this up. Let us say I have two computers. I will create folder structures as follows:

```
~/sync/
  ├── papers/
  └── zotero/
```

You may wish to keep those folders synced individually or together. Individually might be best if in one of the computers is to store the directories in different relative paths to each other. 

## Zotero

Now, follow the setup steps for preperly installing Zotero. 

1. Install Zotero
1. Install the [Zotfile](http://zotfile.com/) plugin
1. Under Zotfile Preferences, leave `General Settings` > `Source Folder for Attaching New Files` blank
1. Under Zotfile Preferences, go to `General Settings` > `Location of Files` > `Custom Location` and set it as `~/sync/papers`. Additionally, check the `Use subfolder defined by` and use a model for storing your files. You may use:
   - `{% raw %}/{%y_}{%t}{% endraw %}` for `~/sync/papers/2016_Name of the Paper/`
   - `/{%t}` for `~/sync/papers/Name of the Paper/`


Now, every time you add a new file via the Zotero connector, you it will automatically send the new files to the `~/sync/papers/{name_of_paper}/{name_of_paper}.pdf`

Next, go to `Edit` > `Preferences` > `Advanced` > `Data Directory Location` and set a custom location to `~/sync/zotero`. It will ask you:

> The directory you selected is empty. To move an existing Zotero data directory, you will need to manually move files from the existing data directory to the new location after Zotero has closed. 
> 
> Use new directory?

Click on "Yes", close Zotero, and move the files from `~/Zotero` into that new folder. 

At this point, you should start to have the following: 


```
~/sync/
  ├── papers/
  └── zotero/
      ├── locate/
      ├── pipes/
      ├── storage/
      ├── styles/
      ├── translators/
      └── zotero.sqlite
```

Then once you start to add your files via the Zotero connector and via the GUI, you will get the following:

```
~/sync/
  ├── papers/
  │   ├── publication_A/
  │   │   └── publication_A.pdf
  │   └── publication_B/
  │       └── publication_B.pdf
  └── zotero/
      ├── locate/
      ├── pipes/
      ├── storage/
      │   ├── GSFPIRZY/
      │   │   └── (used to have publication_A.pdf)
      │   └── RSERDEPY/
      │       ├── (used to have publication_A.pdf)
      │       └── code.py
      ├── styles/
      ├── translators/
      └── zotero.sqlite
```

As you can see, the PDF files will be automatically moved to the correct location. However, as you may also notice, the other attachments are not moved to the correct location, nor is the `~/sync/papers` compatible with papis yet. 

## Transfer Information from Zotero to Papis

Here, I wrote a script which allows you to gather the data from your local Zotero's SQLite database and parse it to an output directory where it can be used by papis. This can be found in the [zotero2papis's repository)[https://github.com/nicolasshu/zotero2papis). In order to use it, take look through the documentation or follow this. 

Install it by first cloning the repository

```bash
git clone https://github.com/nicolasshu/zotero2papis
```

Then install it via
```bash
pip install -e . 
# or 
pip install .
# or 
python3 setup.py install
```

Once that is done, you may use the tool on your terminal by running:

```bash
zotero2papis -z {zotero_directory} -o {output_directory}
```

where `-z` / `--zotdir` will be the parent directory where the Zotero SQLite database is located (e.g. `~/Zotero` or `~/sync/zotero`) and `-o` / `--outdir` is a destination directory where your library will be formed. If the destination directory does not exist, it will be created for you. 

Once you do that, you will have the following structure:


```
~/sync/
  ├── papers/
  │   ├── publication_A/
  │   │   ├── publication_A.pdf
  │   │   └── info.yaml
  │   └── publication_B/
  │       ├── publication_B.pdf
  │       ├── code.py
  │       └── info.yaml
  └── zotero/
      ├── locate/
      ├── pipes/
      ├── storage/
      │   ├── GSFPIRZY/
      │   │   └── (used to have publication_A.pdf)
      │   └── RSERDEPY/
      │       ├── (used to have publication_A.pdf)
      │       └── code.py
      ├── styles/
      ├── translators/
      └── zotero.sqlite
```

Once done, you can ensure that the papis configuration file, which is found in `~/.config/papis/config` has a library set to `dir = ~/sync/papers`, and you can start ot use papis. 
