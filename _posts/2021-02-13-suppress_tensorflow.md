---
layout: article
title: "Suppress Tensorflow Warnings"
tags:
  - Machine Learning
permalink: /tf_suppress.html
---

```python
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
```

```python
%load_ext autoreload
%autoreload 2
```
