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


def gui_load_c3d_filenames():
        root = Tkinter.Tk()
        root.withdraw()
        c3d_filenames = tkFileDialog.askopenfilename(title='Choose a c3d file to convert: ',
                                                filetypes=[('motive c3d tracking files', '*.c3d')],
                                                multiple=True).encode("ascii")
        root.quit()
        return c3d_filenames


def gui_save_c3d_directory():
        root = Tkinter.Tk()
        root.withdraw()
        save_dir = tkFileDialog.askdirectory(title='Choose a directory to save to: ')
        root.quit()
        return save_dir


if __name__ == '__main__':

    # Parse Command-Line Arguments
    parser = argparse.ArgumentParser(description="This script converts a c3d file as exported by motive to a vicon readable c3d file.",
                                 epilog="If no arguments are given, the script first opens a window to let you choose a c3d file or a directory of c3d files to convert. \n")

    parser.add_argument('-f', action='store', dest='c3d_file', default='',
                        help='Name of the c3d file to convert.')

    #parser.add_argument('-F', action='store', dest='c3d_folder', default='', help='Name of the folder which contains c3d files to convert.')

    parser.add_argument('-s', action='store', dest='write_c3d_folder', default='',
                        help='Folder where converted c3d files will be written to.')

    parser.add_argment('--append', action='store', dest='save_filename_append', default='_vicon',
                       help='string to append to new files')

    args = parser.parse_args()

    # Make sure only a file or folder (not both) is specified)
    if args.c3d_folder and args.c3d_file:
        raise Exception("Convert a file OR a folder")

    # Get Filenames
    filenames = [args.c3d_file] if args.c3d_file  else gui_load_c3d_filenames()

    # Get Destination Directory (Save Directory)
    if args.write_c3d_folder:
        # Check to make sure it exists, and if not, make one.
        save_dir = args.write_c3d_folder
    else:
        save_dir = gui_save_c3d_directory()

    # Convert and Write to Each File
    for name in filenames:
        load_dir, base_name = os.path.split(name)
        _, ext = os.path.splitext(name)
        convert_and_write(name, os.path.join(save_dir, base_name+args.save_filename_append+ext))






