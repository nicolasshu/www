---
layout: article
title: "Tensorflow Cheatsheet"
tags:
  - Machine Learning
  - Python
permalink: /tf_cheatsheet.html
---


## Suppress Tensorflow Warnings

```python
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
```

## Allow for GPU Memory Growth

```python
import tensorflow as tf
physical_devices = tf.config.list_physical_devices('GPU') 
tf.config.experimental.set_memory_growth(physical_devices[0], True)
```