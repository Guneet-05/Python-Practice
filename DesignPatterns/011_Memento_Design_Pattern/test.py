# Originator (Main Class)
# Memento Class
# Memento saves the state of Originator

# Care taker me stack me mementos maintained hote hai

from Editor import *
from CareTaker import *
from EditorMemento import *

ct = CareTaker()
e = Editor()

e.text = 'Hello'
e.cursorX = 10
e.cursorY = 20
e.ff = 'Times New Roman'
e.fs = 20

e.print()

em1 = e.getSnapshot()
ct.save(em1)

e.text = 'Hello World'
e.cursorX = 30

e.print()

em2 = e.getSnapshot()
ct.save(em2)

e.fs = 25
e.ff = 'Arial'

e.print()

em3 = e.getSnapshot()
ct.save(em3)

e.restore(ct.undo())
e.print()
e.restore(ct.undo())
e.print()

e.restore(ct.undo())
e.print()

