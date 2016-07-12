#-*- coding: utf-8 -*-

__author__ = 'Gustavo Vargas <xgvargas@gmail.com>'
__version_info__ = ('0', '2', '0')
__version__ = '.'.join(__version_info__)

from PySide import QtCore
import os


def setAsApplication(myappid):
    """
    Tells Windows this is an independent application with an unique icon on task bar.

    id is an unique string to identify this application, like: 'mycompany.myproduct.subproduct.version'
    """

    if os.name == 'nt':
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


def getBestTranslation(basedir, lang=None):
    """
    Find inside basedir the best translation available.

    lang, if defined, should be a list of prefered languages.

    It will look for file in the form:
    - en-US.qm
    - en_US.qm
    - en.qm
    """
    if not lang:
        lang = QtCore.QLocale.system().uiLanguages()

    for l in lang:

        l = l.translate({ord('_'): '-'})
        f = os.path.join(basedir, l+'.qm')
        if os.path.isfile(f): break

        l = l.translate({ord('-'): '_'})
        f = os.path.join(basedir, l+'.qm')
        if os.path.isfile(f): break

        l = l.split('_')[0]
        f = os.path.join(basedir, l+'.qm')
        if os.path.isfile(f): break

    else:
        return None

    translator = QtCore.QTranslator()
    translator.load(f)
    return translator
