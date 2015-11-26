__author__ = 'Nico'

## FOR DEBUGGING
#import pdb
#pdb.set_trace()

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
    print to_c3d_filename
    print to_c3d_filename
    print to_c3d_filename
    print to_c3d_filename
    writer.SetFilename(to_c3d_filename)
    writer.Update()


def gui_load_c3d_filenames():
        root = Tkinter.Tk()
        root.withdraw()
        c3d_filenames_u=tkFileDialog.askopenfilename(title='Choose a c3d file to convert: ',
                                                    filetypes=[('motive c3d tracking files', '*.c3d')],
                                                    multiple=True)
        c3d_filenames=[f.encode('ascii') for f in c3d_filenames_u]
        root.quit()
        return c3d_filenames


def gui_save_c3d_directory():
        root = Tkinter.Tk()
        root.withdraw()
        save_dir = (tkFileDialog.askdirectory(title='Choose a directory to save to: ')).encode('ascii')
        root.quit()
        return save_dir


if __name__ == '__main__':

    # Parse Command-Line Arguments
    parser = argparse.ArgumentParser(description="This script converts a c3d file as exported by motive to a vicon readable c3d file.",
                                 epilog="If no arguments are given, the script first opens a window to let you choose a c3d file or a directory of c3d files to convert. \n")

    parser.add_argument('-f', action='store', dest='c3d_file', default='',
                        help='Name of the c3d file to convert.')

    parser.add_argument('-F', action='store', dest='c3d_folder', default='', help='Name of the folder which contains c3d files to convert.')

    parser.add_argument('-s', action='store', dest='write_c3d_folder', default='',
                        help='Folder where converted c3d files will be written to.')

    parser.add_argument('--append', action='store', dest='save_filename_append', default='_vicon',
                       help='string to append to new files')

    args = parser.parse_args()

    # Make sure only a file or folder (not both) is specified)
    if args.c3d_folder and args.c3d_file:
        raise Exception("Convert a file OR a folder")

    # Get Filenames
    filenames = [args.c3d_file] if args.c3d_file  else gui_load_c3d_filenames()

    # Get Destination Directory (Save Directory)
    if args.write_c3d_folder:
        # TODO: Check to make sure it exists, and if not, make one.
        save_dir = args.write_c3d_folder
    else:
        save_dir = gui_save_c3d_directory()

    # Convert and Write to Each File
    for name in filenames:
        load_dir, base_name = os.path.split(name)
        base, ext = os.path.splitext(base_name)
        save_filename=os.path.join(save_dir, base+args.save_filename_append+ext)
        #save_filename=''.join([save_dir,'\\'+ base+args.save_filename_append+ext])
        #os.path.join uses backward slashes, while tkFileDialog.askdirectory returns forward slashes
        #convert_and_write(name,save_filename.replace('/','\\'))
        convert_and_write(name,save_filename)
        

# import btk
# import Tkinter, tkFileDialog
# import os
# import argparse
#
# # TODO: This function is doing too many things.  Why not break it into 3 functions: read, convert, and write?
# def convert_and_write(c3d_file):
#
#     reader = btk.btkAcquisitionFileReader()
#     reader.SetFilename(c3d_file)
#     reader.Update()
#     acq=reader.GetOutput()
#     points=acq.GetPoints()
#     n_points=points.GetItemNumber()
#
#     for f in xrange(acq.GetPointFrameNumber()):
#         for i in xrange(n_points):
#             point=acq.GetPoint(i)
#             data=point.GetValues()[f,:]
#             point.SetDataSlice(f, *[1000*x for x in data])
#
#     directory, extension = os.path.splitext(c3d_file)
#     converted_c3d_file= ''.join([directory, '_vicon', extension])
#     writer = btk.btkAcquisitionFileWriter()
#     writer.SetInput(acq)
#     writer.SetFilename(converted_c3d_file)
#     writer.Update()
#
#
# # TODO: Make an "if __name__ == '__main__'" section for seperating your script control logic from your functions. This is messy!
#
# parser = argparse.ArgumentParser(description="This script converts a c3d file as exported by motive to a vicon readable c3d file.",
#                                  epilog="If no arguments are given, the script first opens a window to let you choose a c3d file or a directory of c3d files to convert. \n")
#
# parser.add_argument('-f', action='store', dest='c3d_file', default='', help='Name of the c3d file to convert.')
#
# parser.add_argument('-F', action='store', dest='c3d_folder', default='', help='Name of the folder which contains c3d files to convert.')
#
# parser.add_argument('-s', action='store', dest='write_c3d_folder', default='jifoew', help='Folder where converted c3d files will be written to.')
#
# args = parser.parse_args()
#
#
# # TODO: This series of 'if' statements is too complex.  Please simplify: Get Filenames-->Check Directories-->Read-->Convert-->Write
#
# if args.c3d_file and not args.c3d_folder:
#     convert_and_write(args.c3d_file)
#
# elif args.c3d_folder and not args.c3d_file:
#     for c3d_file in os.listdir(args.c3d_folder):
#         if c3d_file.endswith(".c3d"):
#             convert_and_write(''.join([args.c3d_folder,"\\"+c3d_file]))
#
# elif args.c3d_folder and args.c3d_file:
#     raise Exception("Convert a file OR a folder")
#
# else:
#     root = Tkinter.Tk()
#
#     def write_c3d_file():
#         root.withdraw()
#         file_u=tkFileDialog.askopenfilename(title='Choose a c3d file to convert: ', filetypes=[('motive c3d tracking files', '*.c3d')])
#         convert_and_write(file_u.encode("ascii"))
#         root.quit()
#
#     def write_c3d_folder():
#         root.withdraw()
#         c3d_folder=tkFileDialog.askdirectory(title='Choose a folder with c3d files to convert:').encode("ascii")
#         for c3d_file in os.listdir(c3d_folder):
#             if c3d_file.endswith(".c3d"):
#              convert_and_write(''.join([c3d_folder,"\\"+c3d_file]))
#         root.quit()
#
#     frame=Tkinter.Frame(root)
#     frame.pack()
#
#     quit_button=Tkinter.Button(frame, text="QUIT", fg="red", command=frame.quit)
#     quit_button.pack(side=Tkinter.LEFT)
#
#     c3d_file_button = Tkinter.Button(frame, text="c3d file to convert", command=write_c3d_file)
#     c3d_file_button.pack(side=Tkinter.LEFT)
#
#     c3d_folder_button = Tkinter.Button(frame, text="folder with c3d files to convert", command=write_c3d_folder)
#     c3d_folder_button.pack(side=Tkinter.LEFT)
#
#
#     Tkinter.mainloop()




