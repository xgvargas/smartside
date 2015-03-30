#-*- coding: utf-8 -*-

from PySide.QtGui import QPlainTextEdit, QTextCursor
from PySide.QtCore import Qt
from code import InteractiveInterpreter
import sys


__all__ = ['ConsoleWidget']


class ConsoleWidget(QPlainTextEdit):
    """
    """

    def __init__(self, *args, **kwargs):
        """
        """
        super(ConsoleWidget, self).__init__(*args, **kwargs)
        self.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.setMaximumBlockCount(50)
        self.setTabChangesFocus(True)
        # self.setReadOnly(True)
        self.setPlainText('>>>')
        self.moveCursor(QTextCursor.End)
        self.cmd = ''
        self.fullcmd = ''
        self.setLocals(None)
        sys.stdout = self
        sys.stderr = self

    def setLocals(self, local):
        """
        """
        self.ii = InteractiveInterpreter(local)

    def keyPressEvent(self, event):
        key = event.key()

        if key in (Qt.Key_Enter, Qt.Key_Return):
            self.textCursor().insertText('\n')
            r = self.ii.runsource(self.fullcmd+self.cmd)
            if r == True:
                self.fullcmd += '\n'+self.cmd
                self.cmd = '    '
                self.textCursor().insertText('...    ')

            if r == False:
                self.cmd = ''
                self.fullcmd = ''
                self.textCursor().insertText('>>>')

            return True

        elif key == Qt.Key_Backspace:
            if self.cmd:
                self.cmd = self.cmd[:-1]
            else:
                return True
        else:
            self.cmd += event.text()

        self.moveCursor(QTextCursor.End)
        self.ensureCursorVisible()

        QPlainTextEdit.keyPressEvent(self, event)

    def write(self, ln):
        # self.textCursor().insertText(ln.strip('\n\r'))
        self.textCursor().insertText(ln)
        self.moveCursor(QTextCursor.End)
        self.ensureCursorVisible()
