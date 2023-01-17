---
layout: article
title: "Confusion Matrix Cheatsheet"
tags:
  - Python
permalink: /synology_conbeeii.html
mathjax: false
---

Let's say that you have two arrays which are telling you the true labels `y_true` and the predicted labels `y_pred`. Additionally, you have a variable `classes`, which contains all of the classes. Then let's first import the necessary libraries: `pandas`, `seaborn` and `sklearn`

```python
from sklearn.metrics import confusion_matrix
import pandas as pd
import seaborn as sns
```

Then create the confusion matrix, put it into a Pandas DataFrame where the index and columns are the classes

```python
cm = confusion_matrix(y_true, y_pred)
df_cm = pd.DataFrame(cm, index=classes, columns=classes)
```

Finally, plot it:

```python
fig, ax = plt.subplots(dpi=200)
sns.heatmap(df_cm, annot=True, fmt="d", ax=ax)
ax.set_xlabel("Estimated Label")
ax.set_ylabel("True Label")
```
