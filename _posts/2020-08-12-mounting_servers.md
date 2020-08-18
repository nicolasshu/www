---
layout: page
title: "Mounting Server"
categories:
  - Instructions
---

```
# ~/.bash_aliases
function mount_brainiac(){
        sudo mount -t cifs //brainiac.local/$1 /media/Brainiac/$1 -o user=nicolas.s.shu,domain=WORKGROUP,sec=ntlm,vers=1.0
}

function umount_brainiac(){
        sudo umount /media/Brainiac/$1
}
```
