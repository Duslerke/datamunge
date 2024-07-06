# Data Munge
A collection of python scripts for doing data: clean-up, joining, and formatting.

This repository acts as a look up so the "wheel wouldn't need to be read about and assembled twice".

# Using:
- Ensure you have done the [Setup](#Setup) and prepared the [Dependencies](#Dependencies).
- The script files are located within the `src/` directory.
- You can run any given script by either running `python` command with a relative path to the script file:
  ```sh
    python src/sample.py
  ```
  or you can run using your code editor _(example: whilst having script file open in Visual Studio Code,
  you can click the 'play' triangle icon in the top, right corner)_
- Whilst creating new scripts or adding new code you may **introduce** new Pip packages into virtual environment.
  Make sure you update the `requirements.txt` file after you have installed those packages _(otherwise anyone else
  using this environment will not have the packages available to run your new code)_.

  To update the `requirement.txt` file, run:
  ```sh
    pip freeze > requirements.txt
  ```

# Setup
1. **Ensure** you have all the needed dependencies _(see [Dependencies](#Dependencies) section)_.
2. In order to avoid interfering with the Python package versions installed on your computer globally,
   a virtual environment will be used that will contain the packages and their versions this project needs in isolation.
   
   To create a virtual environment for this project, once your terminal window is within the folder directory
   of this project, run:
   ```sh
    python3 -m venv venv
   ```
3. After the virtual environment is created, it needs to be **activated**.
   
   _This step needs to be every time you want to use this project as the environment automatically `deactivate`'s once
   your terminal window is closed._

   **To active** the environment:
   - Linux / MacOS: Run:
    ```sh
        source venv/bin/activate
    ```
    - Windows: Run:
    `./venv/Scripts/activate.bat` or `./venv/Scripts/activate.ps1` _(whichever works)_.
4. _(Optional)_ If all was successful, you should be within the Python's virtual environment.
   You can verify that by running `echo $VIRTUAL_ENV` on Linux, or Windows: `echo %VIRTUAL_ENV%`.
   The output directory path should point to `venv`: `.../datamunge/venv`.
   
   Additionally, if your
   virtual environment has been freshly created, it will only have 1 _(pip)_ package installed within it
5. Lastly, once within the virtual environment, install all of the packages the project needs by running:
   ```sh
    pip install -r requirements.txt
   ```
6. _(Conditional)_ If you have already done the virtual environment setup in the past, and installed the packages it needs
   it is possible that since then the project has started requiring a few extra packages that you don't have installed. You
   may notice this by getting missing package import errors whilst attempting to run some of the code here.
   
   **To ensure** your previously created environment is **up-to-date**, run: 
   ```sh
    pip install --upgrade -r requirements.txt
   ```
   to upgrade old package versions, or to install new missing packages.

# Dependencies
_Note! In between the installs of any packages specified here, if the package you've installed
is still shown as missing after installation, you may need to close down & re-open your terminal window._

1. Ensure you have a [recent](https://www.python.org/downloads/) version of **Python 3**.
   Check your computer's **Python** version by running:
   ```sh
    python --version
   ```
   _(If you have 2 Python versions installed on your system (v2 and v3), the Python 3 command
   will be `python3` instead of `python`)_
2. Check whether **Pip** package manager for Python installed. Run:
   ```sh
    python -m pip --version
   ```
   to see if you have it installed. Otherwise, run:
   ```sh
    python -m ensurepip
   ```
   to install it.
3. Check whether **virtualenv** package is installed by running:
   ```sh
    python -m virtualenv --version
   ```
   If the module is missing, install it via [Pip](https://pypi.org/project/virtualenv/):
   ```sh
    pip install virtualenv
   ```
   **However!** You may be on the system that prevents global package installs directly onto
   your system. In cases such as this, you may beed to rely on your system's package manager.
   Try search for `\-virtualenv` or `virtualenv` within your package manager. Using **apt**:
   ```sh
    apt search '\-virtualenv'
   ```
   Or using **pacman**:
   ```sh
    pacman -Ss '\-virtualenv'
   ```
   The package needed may either be named something like: `python-virtualenv` or `python3-virtualenv`.
   Install it using your package manager, so for **apt**:
   ```sh
    sudo apt update && sudo apt install package_name
   ```
   For **pacman**
   ```sh
    sudo pacman -Sy package_name
   ```
4. You will need to have/install a text editor. **Visual Studio Code** is recommended.
