#-*- coding: utf-8 -*-

__author__ = 'Gustavo Vargas <xgvargas@gmail.com>'
__version_info__ = ('0', '1', '5')
__version__ = '.'.join(__version_info__)


def setAsApplication(myappid):
    """
    Tells Windows this is an independent application with an unique icon on task bar.

    id is an unique string to identify this application, like: 'mycompany.myproduct.subproduct.version'
    """
    import os

    if os.name == 'nt':
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
