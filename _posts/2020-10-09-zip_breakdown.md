---
layout: article
title: "Breaking Zip files into Multiple Parts"
tags:
  - Linux
permalink: /zip_multipart.html
mathjax: true
---


Sometimes zip files may be too big, so you could break them for easier transfer. Assuming you have a large zip file called `dataset.zip` and you wish to split it into 300MB parts. You can do so with 

```bash
zip dataset.zip --out dataparts -s 300m
```

This will then create a bunch of files called

```
dataparts.zip
dataparts.z01
dataparts.z02
dataparts.z03
...
```

In order to collect them back together, you can use 

```bash
zip -F dataparts.zip --out new_dataset.zip
# or 
zip --fix dataparts.zip --out new_dataset.zip
```

Then you can unzip them with `unzip`


## Resources
[1] [Daniel Beck's Answer](https://superuser.com/questions/336219/how-do-i-split-a-zip-file-into-multiple-segments)