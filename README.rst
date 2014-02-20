SmartSide is one of many available ways to have PySide signals connected in a easy way.

Example of what it can do for you
=================================

Suppose you have designed a GUI using *Qt Designer*

Compile it with:

.. sourcecode:: bash

    pyside-uic.exe myform.ui -o myform_ui.py

    #if you have resources included compile them too
    pyside-rcc.exe myresources.qrc -o myresources_rc.py


Then use a code like this to show your form and bind some signals:

.. sourcecode:: python

    from PySide.QtGui import *
    from PySide.QtCore import *
    import sys
    from myform_ui import *
    from smartside import *

    class MyApplication(QtGui.QMainWindow, Ui_MainWindow, SmartSide):
        def __init__(self, parent=None):
            super(MyApplication, self).__init__(parent)
            self.setupUi(self)
            self.auto_connect()

        #will respond to stateChanged signal from checkBox widget
        #notice the double underline between widget name and signal name
        def _on_checkBox__stateChanged(self):
            print 'check', self.sender().isChecked()

        #will respond to pressed signal of btn_add widget
        def _on_btn_add__pressed(self):
            print 'btn_add was pressed'

        #list some widgets and can also use regex `regex`, to select multiples
        #starting with underline is mandatory
        _myfuncs = 'btn_base, btn_format, `btn_.+log.+`, btn_sqr'
        #will respond to clicked signal of all widget listed above
        def _when_myfuncs__clicked(self):
            print 'multiples', self.sender()

    if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        window = MyApplication()
        window.show()
        #uncomment line below to print a list of ALL signals available on your form
        #window.print_all_signals()
        sys.exit(app.exec_())

Your form is supposed to be called *Ui_MainWindow* in this example.

First we use ``setupUi`` as usual to create the interface.

Then ``auto_connect`` will connect member functions to signals when they match.

The last case use a multiple connection, so more then one widgets will call the same
callback function. You can also use regex to select related widgets. In the example above
we have selected a few widgets by its explicit name and also all widget whose name starts with ``'btn\_'``
and have ``'log'`` in some part of its name. All of them are going to be connected to
``_when_myfuncs__clicked``.

More to come
------------

A few other functions are planed for future versions.

----------------------------------

Development:
    https://github.com/xgvargas/smartside - please use this space if you found a problem or think any other task on PySide can be simplified.
