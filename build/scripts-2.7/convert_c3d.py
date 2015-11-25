__author__ = 'Nico'

import btk
import Tkinter, tkFileDialog
import os
import argparse

# TODO: This function is doing too many things.  Why not break it into 3 functions: read, convert, and write?
def convert_and_write(c3d_file):

    reader = btk.btkAcquisitionFileReader()
    reader.SetFilename(c3d_file)
    reader.Update()
    acq=reader.GetOutput()
    points=acq.GetPoints()
    n_points=points.GetItemNumber()

    for f in xrange(acq.GetPointFrameNumber()):
        for i in xrange(n_points):
            point=acq.GetPoint(i)
            data=point.GetValues()[f,:]
            point.SetDataSlice(f, *[1000*x for x in data])

    directory, extension = os.path.splitext(c3d_file)
    converted_c3d_file= ''.join([directory, '_vicon', extension])
    writer = btk.btkAcquisitionFileWriter()
    writer.SetInput(acq)
    writer.SetFilename(converted_c3d_file)
    writer.Update()


# TODO: Make an "if __name__ == '__main__'" section for seperating your script control logic from your functions. This is messy!

parser = argparse.ArgumentParser(description="This script converts a c3d file as exported by motive to a vicon readable c3d file.",
                                 epilog="If no arguments are given, the script first opens a window to let you choose a c3d file or a directory of c3d files to convert. \n")

parser.add_argument('-f', action='store', dest='c3d_file', default='', help='Name of the c3d file to convert.')

parser.add_argument('-F', action='store', dest='c3d_folder', default='', help='Name of the folder which contains c3d files to convert.')

parser.add_argument('-s', action='store', dest='write_c3d_folder', default='jifoew', help='Folder where converted c3d files will be written to.')

args = parser.parse_args()

# TODO: This series of 'if' statements is too complex.  Please simplify: Get Filenames-->Check Directories-->Read-->Convert-->Write

if args.c3d_file and not args.c3d_folder:
    convert_and_write(args.c3d_file)

elif args.c3d_folder and not args.c3d_file:
    for c3d_file in os.listdir(args.c3d_folder):
        if c3d_file.endswith(".c3d"):
            convert_and_write(''.join([args.c3d_folder,"\\"+c3d_file]))

elif args.c3d_folder and args.c3d_file:
    raise Exception("Convert a file OR a folder")

else:

#first try to create without app class. then use tkinter instead from tkinter

    root = Tkinter.Tk()

    def write_slogan():
        root.withdraw()
        c3d_folder=tkFileDialog.askdirectory(title='Choose a folder with c3d files to convert').encode("ascii")
        for c3d_file in os.listdir(c3d_folder):
            if c3d_file.endswith(".c3d"):
             convert_and_write(''.join([c3d_folder,"\\"+c3d_file]))
        root.quit()

    def write_slogan2():
        root.withdraw()
        file_u=tkFileDialog.askopenfilename(title='Choose a c3d file to convert: ', filetypes=[('motive c3d tracking files', '*.c3d')])
        convert_and_write(file_u.encode("ascii"))
        root.quit()

    frame=Tkinter.Frame(root)
    frame.pack()
    button=Tkinter.Button(frame, text="QUIT", fg="red", command=frame.quit)
    button.pack(side=Tkinter.LEFT)
    slogan = Tkinter.Button(frame, text="Folder", command=write_slogan)
    slogan.pack(side=Tkinter.LEFT)
    slogan2 = Tkinter.Button(frame, text="File", command=write_slogan2)
    slogan2.pack(side=Tkinter.LEFT)

    Tkinter.mainloop()





