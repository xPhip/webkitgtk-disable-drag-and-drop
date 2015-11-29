# Disable Drang-and-Drop

Simple py-webkitGTK disable Drang-and-Drop using Python and Javascript.

See more in [Example.py](https://github.com/xPhip/py-webkitgtk-disable-drag-and-drop/blob/master/Example.py)

#### Py
```python
def nulled(self, view, frame, message, isConfirmed):
  return 1
```
```python
webkit.WebView().connect("script-confirm", nulled)
```

#### Js
```javascript
window.onbeforeunload = function(){ return false; };
```
