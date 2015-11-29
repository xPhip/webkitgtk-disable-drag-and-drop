# Disable Drang-and-Drop

Simple py-webkitGTK disable Drang-and-Drop using Python and Javascript.

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
