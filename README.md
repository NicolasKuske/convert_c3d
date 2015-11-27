## use convert_c3d to rewrite c3d files so other programs can read them!

### Why did we make it?

We are using the Optitrack camera system's program, Motive, to export c3d take files, but we had problems importing these files into Vicon IQ for use in their marker labeling postprocessing pipeline.

The convert_c3d.py script uses the Biomechanical Toolkit package BTK to convert
these c3d files, making them readable (and scaling them correctly) by Vicon.
We hope that our script can also solve your c3d compatibility problem.
Feedback is welcome.

### How do I install it?


#### Installing Python

To run the converter script we recommend to install Python 2.7 (32 bit) and make sure it runs in the windows console (i.e. open the Command Window and type *python*. If python starts, then it's installed!  If it is installed but not working, try and add the following file adresses (or depending where you installed stuff) to the PATH variable::
  ```
  C:\Python27\; C:\Python27\Scripts\
  ```
#### Downloading convert_c3d

There are many options for installing this script! While we included a simple Windows Installer in the dist/ folder, the best way would be to clone the repository using *git* (you may need to install git as well: https://git-scm.com/downloads) and download it from the command window into the folder of your choice using the command::

  ```
  git clone https://github.com/NicolasKuske/convert_c3d.git
  ```

#### Installing convert_c3d

To install, simply run the setup.py file by navigating into the convert_c3d directory via the command window (*cd convert_c3d*) and running the install option on the setup.py script::

  ```
  cd convert_c3d
  python setup.py install
  ```

That's it!

#### Using convert_c3d

You should now be able to run the converter script from any directory in the terminal by simply writing::

  ```
  convert_c3d
  ```

##### From the GUI

A window will pop up asking you to select one or multiple c3d files to be converted. After you selected the files a new window will pop up asking you for a folder to write the converted files to.

##### As a Console Script

Optionally, you can use the commandline options to change the scripts behaviour:

* convert_c3d.py --append APPENDSTRING              Choose a string appended to the original filename which together will be the name for the converted file. Default is APPENDSTRING=_vicon

* convert_c3d.py -i C3D_FILES                  Choose a single file to be converted

* convert_c3d.py -R -i C3D_FOLDER            Choose a folder in which all c3d files will be converted

* convert_c3d.py -o WRITE_FOLDER                    Choose the folder to which the c3d files will be written

* convert_c3d.py -h                                 Open a helptext showing all options

Note that all options are optional and that, except for the default appendstring, in case you do not specify an option, you will be prompted by a window.

Njoy!





