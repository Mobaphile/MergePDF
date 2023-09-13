from cx_Freeze import setup, Executable

# Define the script and base options
script = 'merge.py'
base = None  # Set to None for a console-based script

# Create an executable
executables = [Executable(script, base=base)]

# Additional options
options = {
   'build_exe': {
       'packages': [],  # Add any additional packages your script requires
       'include_files': [],  # Add any additional files or folders
   },
}

# Setup
setup(
   name='Your Script Name',
   version='1.0',
   description='Your script description',
   options=options,
   executables=executables
)
