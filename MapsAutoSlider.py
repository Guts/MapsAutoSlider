﻿# -*- coding: UTF-8 -*-
#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        MapsAutoSlider
# Purpose:
#
# Author:      Julien M.
#
# Created:     15/03/2013
# Copyright:   (c) Utilisateur 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from Tkinter import *
from tkFileDialog import askopenfile

class mapslider(Tk):
    def __init__(self):
        Tk.__init__(self)   # constructeur de la classe parente
        self.withdraw()
        self.title(u'Choose your maps before and after')
        # labels
        self.labglob = Label(self, text = u' Please paste the path of your before map')
        self.labefore = Label(self, text = u'Map before: ')
        self.labafter = Label(self, text = u'Map after: ')
        # paths to image
        self.pathbefore = Entry(self)
        self.pathafter = Entry(self)
        # browse buttons
        self.browsebef = Button(self, text = 'Browse', command = self.browsepath(bef))
        self.browseaft = Button(self, text = 'Browse', command = self.browsepath(aft))
        # basic buttons
        self.validate = Button(self, text = 'Browse')
        self.cancel = Button(self, text = 'Browse', command = self.annuler)

    def browsepath(self, entree):
            filename = askopenfile(parent = self, filetypes = (("Images", "*.jpg;*.jpeg;*.png"),
                                                ("All files", "*.*")))
            if filename:
                try:
                    self.settings["template"].set(filename)
                except:
                    tkMessageBox.showerror("Open Source File", "Failed to read file \n'%s'"%filename)
                    return

    def annuler(self):
        self.destroy()






if __name__ == '__main__':
    app = mapslider()
    app.mainloop()



