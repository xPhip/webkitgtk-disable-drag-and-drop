#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk
import webkit

HTML = """
<html>
<head>
<script type="text/javascript">
window.onbeforeunload = function(){ return false; };
</script>
</head>
<body>
Hello World!
</body>
"""

# Cancel javascript dialog
def js_script_confirm(sef, view, dialog, data):
	return 1

win = gtk.Window()
win.connect("destroy", lambda w: gtk.main_quit())
win.set_title("Disable Drag-and-Drop")
win.set_size_request(250,250)

scroller = gtk.ScrolledWindow()
win.add(scroller)
web = webkit.WebView()

web.load_string(HTML, "text/html", "UTF-8","/")
web.connect("script-confirm", js_script_confirm)

scroller.add(web)
win.show_all()
gtk.main()
