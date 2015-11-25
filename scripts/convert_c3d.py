__author__ = 'Nico'

import btk
import Tkinter, tkFileDialog
import os
import argparse



def convert_and_write(from_c3d_filename, to_c3d_filename):

    # Makes reader from filename
    reader = btk.btkAcquisitionFileReader()
    reader.SetFilename(from_c3d_filename)
    reader.Update()
    acq=reader.GetOutput()
    points=acq.GetPoints()
    n_points=points.GetItemNumber()

    for f in xrange(acq.GetPointFrameNumber()):
        for i in xrange(n_points):
            point=acq.GetPoint(i)
            data=point.GetValues()[f,:]
            point.SetDataSlice(f, *[1000*x for x in data])

    writer = btk.btkAcquisitionFileWriter()
    writer.SetInput(acq)
    writer.SetFilename(to_c3d_filename)
    writer.Update()


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
    root = Tkinter.Tk()

    def write_c3d_file():
        root.withdraw()
        file_u=tkFileDialog.askopenfilename(title='Choose a c3d file to convert: ', filetypes=[('motive c3d tracking files', '*.c3d')])
        convert_and_write(file_u.encode("ascii"))
        root.quit()

    def write_c3d_folder():
        root.withdraw()
        c3d_folder=tkFileDialog.askdirectory(title='Choose a folder with c3d files to convert:').encode("ascii")
        for c3d_file in os.listdir(c3d_folder):
            if c3d_file.endswith(".c3d"):
             convert_and_write(''.join([c3d_folder,"\\"+c3d_file]))
        root.quit()

    frame=Tkinter.Frame(root)
    frame.pack()

    quit_button=Tkinter.Button(frame, text="QUIT", fg="red", command=frame.quit)
    quit_button.pack(side=Tkinter.LEFT)

    c3d_file_button = Tkinter.Button(frame, text="c3d file to convert", command=write_c3d_file)
    c3d_file_button.pack(side=Tkinter.LEFT)

    c3d_folder_button = Tkinter.Button(frame, text="folder with c3d files to convert", command=write_c3d_folder)
    c3d_folder_button.pack(side=Tkinter.LEFT)


    Tkinter.mainloop()



#
if __name__ == '__main__':

    # Parse Command-Line Arguments
    parser = argparse.ArgumentParser(description="This script converts a c3d file as exported by motive to a vicon readable c3d file.",
                                 epilog="If no arguments are given, the script first opens a window to let you choose a c3d file or a directory of c3d files to convert. \n")

    parser.add_argument('-f', action='store', dest='c3d_file', default='', help='Name of the c3d file to convert.')

    parser.add_argument('-F', action='store', dest='c3d_folder', default='', help='Name of the folder which contains c3d files to convert.')

    parser.add_argument('-s', action='store', dest='write_c3d_folder', default='jifoew', help='Folder where converted c3d files will be written to.')

    args = parser.parse_args()

    #



