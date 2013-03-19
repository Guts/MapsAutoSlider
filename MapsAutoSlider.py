# -*- coding: UTF-8 -*-
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
from tkFileDialog import askopenfilename

class mapslider(Tk):
    def __init__(self):
        Tk.__init__(self)   # constructeur de la classe parente
##        self.withdraw()
        self.title(u'Choose your maps before and after')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        # labels
        self.labglob = Label(self, text = u' Please paste the path of your before map')
        self.labefore = Label(self, text = u'Map before: ')
        self.labafter = Label(self, text = u'Map after: ')
        # paths to image
        self.pathbefore = Entry(self, width = 35)
        self.pathafter = Entry(self, width = 35)
        # browse buttons
        self.browsebef = Button(self, text = 'Browse', command = self.setpathbef)
        self.browseaft = Button(self, text = 'Browse', command = self.setpathaft)
        # basic buttons
        self.validate = Button(self, text = 'Validate')
        self.cancel = Button(self, text = 'Cancel (quit)', command = self.annuler)

        # placement
        self.labglob.grid(row = 0, column = 0, columnspan = 3)
        self.labefore.grid(row = 1, column = 1, columnspan = 1)
        self.labafter.grid(row = 2, column = 1, columnspan = 1)
        self.pathbefore.grid(row = 1, column = 2, columnspan = 1)
        self.pathafter.grid(row = 2, column = 2, columnspan = 1)
        self.browsebef.grid(row = 1, column = 3, columnspan = 1)
        self.browseaft.grid(row = 2, column = 3, columnspan = 1)
        self.validate.grid(row = 3, column = 0, columnspan = 2)
        self.cancel.grid(row = 3, column = 2, columnspan = 1)

    def setpathbef(self):
            self.filename = askopenfilename(parent = self,
                                            title = 'Select the before image',
                                            filetypes = (("All files", "*.*"),
                                                                        ("Images", "*.jpg;*.jpeg;*.png")))
            if self.filename:
                try:
                    self.pathbefore.insert(0, self.filename)
                except:
                    print 'no file indicated'
            return self.filename

    def setpathaft(self):
            self.filename = askopenfilename(parent = self, filetypes = (("All files", "*.*"),
                                                                        ("Images", "*.jpg;*.jpeg;*.png")))
            if self.filename:
                try:
                    self.pathafter.insert(0, self.filename)
                except:
                    print 'no file indicated'
            return self.filename

    def annuler(self):
        self.destroy()






if __name__ == '__main__':
    app = mapslider()
    app.mainloop()




