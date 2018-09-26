# harmonicintervalprofile

Python library for computing (shared) harmonic interval profiles from chord labels

## Example use:

Compute a Harmonic Interval Profile (HIP) from a chord label:

```python 
import harmonicintervalprofile as hip 
```

```python 
>>> label_hip = hip.label_to_hip('Eb:maj/3')
```

```python 
>>> label_hip
```

```python 
array([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
       1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
       0, 0])
```

Compute a Shared Harmonic Interval Profile (SHIP) from multiple chord labels:

```python 
>>> chord_labels = ['G:min', 'Eb:maj/3', 'G:min', 'Eb:maj/3', 'Eb:maj'] 
```

```python 
>>> hips = np.array([hip.label_to_hip(c) for c in chord_labels]) 
```

```python 
>>> hips 
array([[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0,
        1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
        1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
        0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0,
        1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
        1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
        0, 0],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
        1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0]]) 
```

A SHIP is the average of multiple HIPs:

```python 
>>> ship(hips) 
    array([0. , 0. , 0. , 0.6, 0. , 0. , 0. , 0.4, 0. , 0. , 0. , 0. , 0. ,
       0. , 0. , 0. , 1. , 0.6, 0.4, 0. , 0. , 0. , 1. , 1. , 0. , 0. ,
       0. , 0. , 1. , 0. , 0. , 0. , 1. , 0.6, 0. , 0. , 0. , 0.4, 0. ,
       0. , 0. , 0. , 0. , 0. , 0. , 0. ])
```

## Dependencies:

* `mir_eval`
* `numpy`
* `re`

If you use harmonicintervalprofile in a research project, please cite the following paper:

Koops, H.V., de Haas, W.B., Bransen, J. et al. "Automatic chord label personalization through deep learning of shared harmonic interval profiles" Neural Computing & Applications Springer 2018 https://doi.org/10.1007/s00521-018-3703-y 

```
@Article{Koops2018,
author="Koops, Hendrik Vincent and de Haas, W. Bas and Bransen, Jeroen and Volk, Anja",
title="Automatic chord label personalization through deep learning of shared harmonic interval profiles",
journal="Neural Computing and Applications",
year="2018",
month="Sep",
day="21",
issn="1433-3058",
doi="10.1007/s00521-018-3703-y",
url="https://doi.org/10.1007/s00521-018-3703-y"
}
```
