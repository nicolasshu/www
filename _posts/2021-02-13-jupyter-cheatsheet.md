---
layout: article
title: "Jupyter Cheatsheet"
tags:
  - Python
permalink: /jupyter_cheatsheet.html
---

## Autoreload

```python
%load_ext autoreload
%autoreload 2
```


## IPython

### Display Audio

```python
import IPython.display as ipd

audio, fs = librosa.load("path/to/audio")
ipd.Audio(data=audio, rate=fs)
```