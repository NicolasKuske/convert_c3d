#use convert_c3d to rewrite c3d files making them generally compatible

We are using the Optitrack camera system and there the Motive GUI to export c3d
take files. We had problems importing these files into Vicon.
The convert_c3d.py script uses the Biomechanical Toolkit package BTK to convert
these c3d files, making them readable (and scaling them correctly) by Vicon.
We hope that our script can also solve your c3d compatibility problem.
Feedback is welcome.

To run the converter script we recommend to install Python 2.7 (32 bit) and add the following file adresses (or depending where you installed stuff) to the PATH variable:

C:\Python27\; C:\Python27\Scripts\

Then simply git clone the repository in the folder of your choice (or cumbersomely copy paste everything)
open a console terminal, cd into the cloned repository and write:

python setup.py install

You should now be able to run the converter script from any directory in the terminal by simply writing:

convert_c3d.py

A window will pop up asking you to select one or multiple c3d files to be converted. After you selected the files a new window will pop up asking you for a folder to write the converted files to.

Optionally you can use the commandline options to change the scripts behaviour:

* convert_c3d.py --append APPENDSTRING              Choose a string appended to the original filename which together will be the name for the converted file. Default is APPENDSTRING=_vicon

* convert_c3d.py -i C3D_FILES                  Choose a single file to be converted

* convert_c3d.py -R -i C3D_FOLDER            Choose a folder in which all c3d files will be converted

* convert_c3d.py -o WRITE_FOLDER                    Choose the folder to which the c3d files will be written

* convert_c3d.py -h                                 Open a helptext showing all options

Note that all options are optional and that, except for the default appendstring, in case you do not specify an option, you will be prompted by a window.

Njoy!





