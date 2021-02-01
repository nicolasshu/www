---
layout: article
title: "Appending to Dataset in HDF5 (h5py)"
tags:
  - Python
permalink: /appending_to_dataset_h5py.html
mathjax: false
---

## Simple Example 

This is a reminder of how to add data to a dataset in `h5py`. Let's first import some packages, and declare a path for a file

```python
import h5py
import numpy as np

path = "test.h5"

# Optional 
import os
os.remove(path)
```

We can create 

```python
# Create the file
hdf = h5py.File(path, "a")

# Create an empty dataset with features shaped (40,200)
dset = hdf.create_dataset(
    name  = "my_data",
    shape = (0,40,200),
    maxshape = (None, 40, 200), # None means that this dimension can be extended
    dtype = "f16"
    )
print(dset.shape)   # (0,40,200)
print(type(dset))   # <class 'h5py._hl.dataset.Dataset'>
```

Here we set the shape as `(0,?,?)` to mean that it is an empty dataset. We make the `maxshape` to have the shape `(None,?,?)`, which means that axis 0 can be expanded to whatever we wish. Next, we can start to expand our dataset:

```python
for k in range(3):
    N = 2
    dset.resize(dset.shape[0]+N, axis=0)
    new_data = np.random.random([N,40,200])
    dset[-N:] = new_data
    print(dset.shape)
    # (2, 40, 200)
    # (4, 40, 200)
    # (6, 40, 200)
hdf.close()
```

And this is how you iteratively append to a dataset. In order to check for the data in the file

```python
with h5py.File(path,"r") as hdf:
    data = hdf["my_data"][:]
print(data.shape) # (6, 40, 200)
print(type(data)) # <class 'numpy.ndarray'>
```

### Full Code

```python
import h5py
import numpy as np
path = "test.h5"

# Optional 
import os
os.remove(path)

# Create the file
with h5py.File(path, "a") as hdf:

    # Create an empty dataset with features shaped (40,200)
    dset = hdf.create_dataset(
        name  = "my_data",
        shape = (0,40,200),
        maxshape = (None, 40, 200), # None means that this dimension can be extended
        dtype = "f16"
        )
    print(dset.shape)   # (0,40,200)
    print(type(dset))   # <class 'h5py._hl.dataset.Dataset'>

    for k in range(3):
        N = 2
        dset.resize(dset.shape[0]+N, axis=0)
        new_data = np.random.random([N,40,200])
        dset[-N:] = new_data
        print(dset.shape)
        # (2, 40, 200)
        # (4, 40, 200)
        # (6, 40, 200)

with h5py.File(path,"r") as hdf:
    data = hdf["my_data"][:]
print(data.shape) # (6, 40, 200)
print(type(data)) # <class 'numpy.ndarray'>
```

## Example for a Dataset for ML

First import the packages, and establish a destination path

```python
import h5py
import numpy as np 
import random
path = "test.h5"

# Optional
os.remove(path)
```

Next open up a HDF5 file in appending mode

```python
hdf = h5py.File(path, "a")
```

Now we will add groups, where we will keep labels and data. Let's say we have two different types of features: A and B. We will keep them in separate groups: "features_A" and "features_B". Here we will create two groups, but we will only work with one.

```python
group_A = hdf.create_group("features_A")
group_B = hdf.create_group("features_B")
```

And then we will create the datasets. Per group, one dataset will be for features, and another will be for labels. It is important to say that, if you wish to set data in datasets as strings (`str`), you need to create a special type of data type. We'll use `h5py.special_dtype` to do so [[Source](https://stackoverflow.com/a/43935389/4962905)]


```python
dt = h5py.special_dtype(vlen=str)
feats_A = group_A.create_dataset("features",(0,40,200), maxshape=(None,40,200))
labels_A = group_A.create_dataset("gender", (0,), maxshape=(None,), dtype=dt)
```

Now, let's set up a few attributes to describe this dataset

```python
group_A.attrs["fs"] = 16000
group_A.attrs["win_dur"] = 0.025
group_A.attrs["hop_dur"] = 0.01
```

And then we can start to populate the dataset and the labels

```python
gender = ["m", "f"]
for k in range(3):
    feats_A.resize(feats_A.shape[0]+1, axis=0)
    labels_A.resize(labels_A.shape[0]+1, axis=0)

    feats_A[-1] = np.random.random([1,40,200])
    labels_A[-1]= random.sample(gender,1)[0]

hdf.close()
```


Now we can check the results:

```python
with h5py.File(path,"r") as hdf:
    feats = hdf["features_A/features"][:]
    labels= hdf["features_A/gender"][:]
    g1 = hdf["features_A"]
    params = dict(g1.attrs)

print(params)
print(feats)
print(type(feats))
print(labels)
print(type(labels))
```


```python
import h5py
import numpy as np
import random
path = "test.h5"

# Optional 
import os
os.remove(path)

with h5py.File(path, "a") as hdf:
    group_A = hdf.create_group("features_A")
    group_B = hdf.create_group("features_B")
    dt = h5py.special_dtype(vlen=str)
    feats_A = group_A.create_dataset("features",(0,40,200), maxshape=(None,40,200))
    labels_A = group_A.create_dataset("gender", (0,), maxshape=(None,), dtype=dt)
    group_A.attrs["fs"] = 16000
    group_A.attrs["win_dur"] = 0.025
    group_A.attrs["hop_dur"] = 0.01
    gender = ["m", "f"]
    for k in range(3):
        feats_A.resize(feats_A.shape[0]+1, axis=0)
        labels_A.resize(labels_A.shape[0]+1, axis=0)

        feats_A[-1] = np.random.random([1,40,200])
        labels_A[-1]= random.sample(gender,1)[0]

with h5py.File(path,"r") as hdf:
    feats = hdf["features_A/features"][:]
    labels= hdf["features_A/gender"][:]
    g1 = hdf["features_A"]
    params = dict(g1.attrs)

print(params)
# {'fs': 16000, 'hop_dur': 0.01, 'win_dur': 0.025}

print(feats)
# (3, 40, 200)

print(type(feats))
# <class 'numpy.ndarray'>

print(labels)
# ['f', 'm', 'm']

print(type(labels))
# <class 'numpy.ndarray'>

print(type(labels[0]))
# <class 'str'>
```

