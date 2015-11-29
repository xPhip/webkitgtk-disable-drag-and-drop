# Disable Drang-and-Drop

Simple py-webkitGTK disable Drang-and-Drop using Python and Javascript.

See more in [Example.py](https://github.com/xPhip/py-webkitgtk-disable-drag-and-drop/blob/master/README.md)

#### Py
```python
def nulled(one=None, two=None, tree=None, four=None):
  return 1
```
```python
webkit.WebView().connect("script-confirm", nulled)
```

#### Js
```javascript
window.onbeforeunload = function(){ return false; };
```
