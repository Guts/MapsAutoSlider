# -*- coding: UTF-8 -*-
#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        MapsAutoSlider
# Purpose:     GUI to create easily a html page with a javascript slider to
#          compare 2 images or maps. The js script is authored by atchmyfame.com
#          See http://www.catchmyfame.com/catchmyfame-jquery-plugins/jquery-beforeafter-plugin/
# Author:      Julien M.
# Created:     19/03/2013
# Licence:     CC Attribution-NonCommercial-ShareAlike 3.0 Unported
#          CC BY-NC-SA 3.0)-http://creativecommons.org/licenses/by-nc-sa/3.0/
#-------------------------------------------------------------------------------

###################################
##### Libraries importation #######
###################################

# standard library
from Tkinter import Tk, Label, Button, W, Entry
from tkFileDialog import askopenfilename, askdirectory
from tkMessageBox import showerror
from os import mkdir, path
from shutil import copytree, copy2
from webbrowser import open as webview
# third party
from modules import EXIF # by https://github.com/ianare/exif-py

###################################
####### Classes definition ########
###################################

class mapslider(Tk):
    """ Main class """
    def __init__(self):
        # basics
        Tk.__init__(self)   # constructor of parent graphic class
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
                                     command = self.processhtml)
        self.cancel = Button(self, text = 'Cancel (quit)',
                                   relief= 'groove',
                                   command = self.destroy)

        # widgets placement
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
                                            filetypes = (("Images", "*.jpg;*.jpeg;*.png;*.tiff"),
                                                         ("All files", "*.*")))
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
                                        filetypes = (("Images", "*.jpg;*.jpeg;*.png;*.tiff"),
                                                     ("All files", "*.*")))
        if self.filename:
            try:
                self.pathafter.insert(0, self.filename)
            except:
                print 'no file indicated'
        # end of function
        return self.filename

    def setpathtarg(self):
        """ ...browse and insert the path of DESTINATION FOLDER """
        self.foldername = askdirectory(parent = self,
                                     title = 'Select the destination folder')
        if self.foldername:
            try:
                self.target.insert(0, self.foldername)
            except:
                print 'no folder indicated'
        # end of function
        return self.foldername

    def processhtml(self):
        """ export the html output file adding the div needed """
        # if jpeg or tiff images => test images dimensions
        extimg = (path.splitext(self.pathbefore.get())[1],
                  path.splitext(self.pathafter.get())[1])
        print extimg
        extok = ('.jpeg', '.jpg', '.JPG', '.JPEG', '.tiff', '.TIFF')
        if extimg[0] in extok and extimg[1] in extok:
            self.testdim(self.pathbefore.get(), self.pathafter.get())
        else:
            print "Images format couldn't be tested."
        # variables
        img1 = 'img/' + path.basename(self.pathbefore.get())
        img2 = 'img/' + path.basename(self.pathafter.get())
        dest = self.target.get()
        pathimg = path.join(dest, 'img')
        pathjs = path.join(dest, 'js')
        # Preparation of destination folder
        mkdir(pathimg, 0644)
        copy2(self.pathbefore.get(), pathimg)
        copy2(self.pathafter.get(), pathimg)
        copytree('js', pathjs)
        # creating the html output
        with open(r'template.html', 'r') as tpl, open(path.join(dest, 'MapsComparison_slider.html'), 'a') as self.out:
            for line in tpl.read():
                self.out.write(line)
            self.out.write('\n<div id="container">\
        \n\t<div>\
        \n\t\t<img alt="before" src="' + img1 + '" width="" />\
        \n\t</div>\
        \n\t<div>\
        \n\t\t<img alt="after" src="' + img2 + '" width="" />\
        \n\t</div>\
        \n\t</div>\
        \n</body>\
        \n</html>')

        # closing GUI
        self.destroy()
        # opening the output file
        webview(self.out.name)
        #end of function
        return self.out

    def testdim(self, pathimg1, pathimg2):
        """ test dimensions if jpeg and tiff images selected """
        # reading EXIF tags inside images files
        with open(pathimg1, 'rb') as mag1, open(pathimg2, 'rb') as mag2:
            tag1 = EXIF.process_file(mag1,
                                     details = False,
                                     stop_tag='ExifImageLength')
            tag2 = EXIF.process_file(mag2,
                                     details = False,
                                     stop_tag='ExifImageLength')
        # getting dimensions tags keys
        self.w1 = int(str(tag1.get('EXIF ExifImageWidth')))
        self.w2 = int(str(tag2.get('EXIF ExifImageWidth')))
        self.l1 = int(str(tag1.get('EXIF ExifImageLength')))
        self.l2 = int(str(tag2.get('EXIF ExifImageLength')))
        # comparing
        if not self.w1 == self.w2 and not self.l1 == self.l2:
            showerror(title='Dimensions error',
                      message = 'Both images may have the same dimensions')
            self.destroy()
        else:
            'everything ok'
        # end of function
        return self.w1, self.w2, self.l1, self.l2




###################################
### Main program initialization ###
###################################

if __name__ == '__main__':
    app = mapslider()
    app.mainloop()