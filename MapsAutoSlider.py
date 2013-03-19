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
from tkFileDialog import askopenfilename, askdirectory

class mapslider(Tk):
    """ Main class """
    def __init__(self):
        Tk.__init__(self)   # constructeur de la classe parente
##        self.withdraw()
        self.title(u'Choose your maps before and after')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        # labels
        self.labglob = Label(self, text = u' Please paste or browse the path of your maps')
        self.labefore = Label(self, text = u'Map before: ')
        self.labafter = Label(self, text = u'Map after: ')
        # paths to image
        self.pathbefore = Entry(self, width = 35)
        self.pathafter = Entry(self, width = 35)
        # browse buttons
        self.browsebef = Button(self, text = 'Browse',
                                      command = self.setpathbef)
        self.browseaft = Button(self, text = 'Browse',
                                      command = self.setpathaft)

        # target folder
        self.labtarg = Label(self, text = u'Destination folder: ')
        self.target = Entry(self, width = 35)
        self.browsetarg = Button(self, text = 'Browse',
                              command = self.setpathtarg)
        # basic buttons
        self.validate = Button(self, text = 'Validate',
                                     relief= 'raised',
                                     command = self.templhtml(self.pathbefore.get(), self.pathafter.get()))
        self.cancel = Button(self, text = 'Cancel (quit)',
                                   relief= 'groove',
                                   command = self.destroy)

        # placement
        self.labglob.grid(row = 0, column = 0, columnspan = 3)
        self.labefore.grid(row = 1, column = 1, columnspan = 1)
        self.labafter.grid(row = 2, column = 1, columnspan = 1)
        self.labtarg.grid(row = 3, column = 1, columnspan = 1)
        self.pathbefore.grid(row = 1, column = 2, columnspan = 1)
        self.pathafter.grid(row = 2, column = 2, columnspan = 1)
        self.target.grid(row = 3, column = 2, columnspan = 1)
        self.browsebef.grid(row = 1, column = 3, columnspan = 1)
        self.browseaft.grid(row = 2, column = 3, columnspan = 1)
        self.browsetarg.grid(row = 3, column = 3, columnspan = 1)
        self.validate.grid(row = 4, column = 1, columnspan = 2)
        self.cancel.grid(row = 4, column = 3, columnspan = 1, sticky = "W")

    def setpathbef(self):
        """ ...browse and insert the path of FIRST image  """
        self.filename = askopenfilename(parent = self,
                                            title = 'Select the "before" image',
                                            filetypes = (("All files", "*.*"),
                                                         ("Images", "*.jpg;*.jpeg;*.png")))
        if self.filename:
            try:
                self.pathbefore.insert(0, self.filename)
            except:
                print 'no file indicated'
        # end of function
        return self.filename

    def setpathaft(self):
        """ ...browse and insert the path of SECOND image """
        self.filename = askopenfilename(parent = self,
                                        title = 'Select the "after" image',
                                        filetypes = (("All files", "*.*"),
                                                     ("Images", "*.jpg;*.jpeg;*.png")))
        if self.filename:
            try:
                self.pathafter.insert(0, self.filename)
            except:
                print 'no file indicated'
        # end of function
        return self.filename

    def setpathtarg(self):
        """ ...browse and insert the path of destination folder """
        self.foldername = askdirectory(parent = self,
                                     title = 'Select the destination folder')
        if self.foldername:
            try:
                self.target.insert(0, self.foldername)
            except:
                print 'no folder indicated'
        # end of function
        return self.foldername


    def targetready(self, folder):
        print folder

    def templhtml(self, img1, img2):
        self.tpl = open(r'template.html', mode = 'r').readlines()
        self.out = open(r'result.html', mode = 'a')
        self.out.write('\n<div id="container"><div><img alt="before" src="IMAGEBEFORE" width="500" /></div><div><img alt="after" src="IMAGEAFTER" width="500" /></div></div></body></html>')

        self.out.close()

        # closing GUI
        self.destroy
        #end of function
        return self.tpl, self.out




if __name__ == '__main__':
    app = mapslider()
    app.mainloop()




