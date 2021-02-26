---
layout: article
title: "PyTorch Reminders to Self"
tags:
  - Machine Learning
permalink: /pytorch_reminders.html
mathjax: false
---

### Using 
Let's say that 


```python
# %%
drop = nn.Dropout()
x = torch.ones(1,10)
# %%
drop.train()
drop(x)

# %%
drop.eval()
drop(x)

```