import cx_Freeze
import sys
base = None
if sys.platform == "win32":
    base = "Win32GUI"
shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory_
     "Speed Up Shanti Motors",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]\main.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     "TARGETDIR",  # WkDir
     )
]
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}

executables = [cx_Freeze.Executable(script="main.py",icon='speed_up_logo.ico',base=base)]

cx_Freeze.setup(
    version="2.0",
    description="Speed Up Shanti Motors Software is made by Soham Mahesh Tamhane",
    author="Soham Mahesh Tamhane",
    name="Speed Up Shanti Motors",
    options={"build_exe": {"packages":["tkinter", "tkinter.ttk", "tkinter.messagebox", "pandas", "random", "datetime", "shutil", "tkcalendar", "subprocess", "os"],
                           "include_files":['login_logo.png','speed_up_logo.png', 'speed_up_logo.ico']},
             "bdist_msi": bdist_msi_options,
             },
    executables = executables

    )
