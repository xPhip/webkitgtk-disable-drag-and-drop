# Disable Drang-and-Drop

Simple WebkitGTK Disable Drang-and-Drop using Python and Javascript.

See more in [Example.py](https://github.com/xPhip/py-webkitgtk-disable-drag-and-drop/blob/master/Example.py)

#### Py
```python
def js_script_confirm(view, dialog, data, arg):
  return 1
```
```python
webkit.WebView().connect("script-confirm", js_script_confirm)
```

#### Js
```javascript
window.onbeforeunload = function(){ return false; };
```
