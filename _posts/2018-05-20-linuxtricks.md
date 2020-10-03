---
layout: article
title: "Linux Terminal Cheatsheet"
tags:
  - Instructions
  - Linux
permalink: terminal_cheatsheet.html
---

This page is basically just some Linux commands that I think it's good for me to keep as reference


## Find Text in All Files
In order to look for the files that contain a certain text:  
`grep -r 'text_to_be_found' /path/to/files`

Alternatively, you can use, from [rakib_](https://stackoverflow.com/questions/16956810/how-do-i-find-all-files-containing-specific-text-on-linux)  
`grep -rnw '/path/to/somewhere/' -e 'pattern'`
* `-r` or -R is recursive,
* `-n` is line number, and
* `-w` stands for match the whole word.
* `-l` (lower-case L) can be added to just give the file name of matching files.
Along with these, --exclude, --include, --exclude-dir flags could be used for efficient searching:

This will only search through those files which have .c or .h extensions:
`grep --include=\*.{c,h} -rnw '/path/to/somewhere/' -e "pattern"`  

This will exclude searching all the files ending with .o extension:
`grep --exclude=*.o -rnw '/path/to/somewhere/' -e "pattern"`

For directories it's possible to exclude a particular directory(ies) through --exclude-dir parameter. For example, this will exclude the dirs dir1/, dir2/ and all of them matching *.dst/:

` grep --exclude-dir={dir1,dir2,*.dst} -rnw '/path/to/somewhere/' -e "pattern" `





## Set the Monitor Resolution

Get the Modeline with the following command. 60 is the monitor refresh rate in Hz. You have to know your monitor refresh rate!!!
`cvt 1360 768 60`  

The output looks like this. Copy the modeline after `Modeline` to use it in the next command.:
```
# 1360x768 59.80 Hz (CVT) hsync: 47.72 kHz; pclk: 84.75 MHz`
Modeline "1360x768_60.00"   84.75  1360 1432 1568 1776  768 771 781 798 -hsync +vsync
```  
Create a new mode with the copied modeline and xrandr.:
`xrandr --newmode "1360x768_60.00"   84.75  1360 1432 1568 1776  768 771 781 798 -hsync +vsync`

With the following command, you get the connected port.  
`xrandr --query | grep connected`  

The output looks like this. As you can see, in my case the connected port is DVI-0.:
```
HDMI-0 disconnected (normal left inverted right x axis y axis)
DVI-0 connected 1920x1080+0+0 (normal left inverted right x axis y axis) 521mm x 293mm
VGA-0 disconnected (normal left inverted right x axis y axis)
```
Add the new mode using your connected port.:
`xrandr --addmode DVI-0 "1360x768_60.00"`

Change the monitor resolution.:
`xrandr --output DVI-0 --mode "1360x768_60.00"`





## Colored Bash
Open `~/.bashrc` in text editor  
`sudo gedit ~/.bashrc`

Uncomment line:  
`#force_color_prompt=yes` $$\rightarrow$$ `force_color_prompt=yes`

Save and Source the file  
`source ~/.bashrc`
