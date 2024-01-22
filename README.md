# binvox_rw
Python module to read and write .binvox files, Contributions come from [`dimatura/binvox-rw-py`](https://github.com/dimatura/binvox-rw-py).
Fixed some bugs and packaged them into installable Python packages。

## Install
```
git clone git@github.com:wangqiang9/binvox_rw.git
cd binvox_rw
pip install .
```

## Example
![example](https://github.com/wangqiang9/binvox_rw/blob/main/example.gif)
```
>>> import binvox_rw
>>> with open('chair.binvox', 'rb') as f:
...     model = binvox_rw.read_as_3d_array(f)
>>> model.dims
[32, 32, 32]
>>> model.scale
41.133000000000003
>>> model.translate
[0.0, 0.0, 0.0]
>>> model.data
```

## Convert to video
```
pip install matplotlib
pip install moviepy
```

```
python convert_to_video.py
```

## Datasets Download
```
https://shapenet.org/
```
