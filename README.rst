SmartSide is one of many available ways to have PySide signals connected in a easy way.

Example of what it can do for you
---------------------------------

Suppose you have designed a GUI using *Qt Designer*

Compile it with:

.. sourcecode:: bash

    $ pyside-uic.exe myform.ui -o myform_ui.py

    #if you have resources included compile them too
    $ pyside-rcc.exe myresources.qrc -o myresources_rc.py


Then use a code like this to show your form and bind some signals:

.. sourcecode:: python

    import sys
    from myform_ui import *   # this will also include `QtCore` and `QtGui`
    import smartside.signal as smartsignal

    class MyApplication(QtGui.QMainWindow, Ui_MainWindow, smartsignal.SmartSignal):
        def __init__(self, parent=None):
            super(MyApplication, self).__init__(parent)
            self.setupUi(self)

            # create any local UI object here, so they signal are
            # going to be auto-connected too

            self.auto_connect()

        # will respond to stateChanged signal from checkBox widget
        # notice the double underline between widget name and signal name
        def _on_checkBox__stateChanged(self):
            print 'check', self.sender().isChecked()

        # will respond to `pressed` signal of btn_add widget
        def _on_btn_add__pressed(self):
            print 'btn_add was pressed'

        # list some widgets and use regex `regex`, to select multiples.
        # starting with underline is mandatory
        _myfuncs = 'btn_base, btn_format, `btn_.+log.+`, btn_sqr'
        # will respond to clicked signal of all widget listed above
        def _when_myfuncs__clicked(self):
            print 'multiples', self.sender()

    if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        window = MyApplication()
        window.show()
        # uncomment line below to print a list of ALL signals available on your form
        #window.print_all_signals()
        sys.exit(app.exec_())

Your form is supposed to be called *Ui_MainWindow* in this example.

First we use ``setupUi`` as usual to create the interface.

Then ``auto_connect`` will connect member functions to signals when they match.

The last case use a multiple connection, so more then one widgets will call the same callback function. You can also use regex to select related widgets. In the example above we have selected a few widgets by its explicit name and also all widget whose name starts with ``'btn\_'`` and have ``'log'`` in some part of its name. All of them are going to be connected to ``_when_myfuncs__clicked``.

Yes, it works with actions too. Like ``def _on_actionTest__triggered(self):``. This is usefull when you create context menu by code. Just remember to call ``auto_connect`` *after* menu creation.

Show icon on Windows taskbar
----------------------------

Usually Windows 7+ executes Python scripts as a group and put every icon you define to your GUI as a child of Python's taskbar icon, since python actually hosts your code. This happens even if you give ``.pyw`` as extension for your python script.

To solve this you have to tell Windows your script is an application by calling ``smartside.setAsApplication()`` and pass to this function an unique identifier for your script, like: 'company.product.version'.

.. sourcecode:: python

    # ....

    if __name__ == "__main__":

        from smartside import setAsApplication
        setAsApplication('example_co.exampleProd.'+__version__)

        app = QtGui.QApplication(sys.argv)
        window = MyApplication()
        window.show()
        sys.exit(app.exec_())


Console Widget
--------------

Using Qt Designer promote a QPlainTextEdit to ``ConsoleWidget``, and use ``smartside.console`` as header (source).

Then, inside ``__init__`` of this form use: ``self.name_of_widget.setLocals({'name': object, 'me': self})``.

This will make the promoted QPlainTextEdit to become a python console with access to two objects: ``name`` and ``me``.

Change History
--------------

:0.1.6: Fixed setup typo.
:0.1.5: Added support to python 3.
:0.1.4: Added ``ConsoleWidget class``.
:0.1.3: Added ``setAsApplication``.
:0.1.2: Added QAction support; For every QAction created before calling auto_connect() you can use ``def _on_action_name__clicked(self):`` like you do with signals.
:0.1.1: Small fix.

------------------

Development:
    https://github.com/xgvargas/smartside - please use this space if you found a problem or think any other task on PySide can be simplified.
