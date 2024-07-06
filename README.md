# Data Munge
A collection of python scripts for doing data: clean-up, joining, and formatting.

This repository acts as a look up so the "wheel wouldn't need to be read about and assembled twice".

# Using:
- Ensure you have done the [Setup](#Setup) and have the [Dependencies](#Dependencies) installed.
- The script files are located within the `src/` directory.
- You can run any given script by either running `python` command with a relative path to the script file:
  ```sh
    python src/sample.py
  ```
  
  Alternatively, you can launch the script using your code editor's functionality
  _(for example: whilst having script file open in Visual Studio Code, you can click the 'play' triangle
  icon in the top, right corner)_
- Whilst creating new scripts or adding new code you may **introduce** new Pip packages into virtual environment
   _(by doing pip install package_name)_.
  Make sure you update the `requirements.txt` file after you have installed those packages _(otherwise others
  setting up virtual environment for this project will not have the packages available to run your new code)_.

  To update the `requirement.txt` file, run:
  ```sh
    pip freeze > requirements.txt
  ```

# Setup
1. **Ensure** you have all the needed dependencies _(see [Dependencies](#Dependencies) section)_.
2. To avoid interfering with the Python Pip packages installed on your computer, and/or to avoid the need to manage their versions,
   a virtual environment will be used that will wrap around this project and contain the packages this project needs in isolation.
   
   To create a virtual environment for this project, once your terminal window is within the folder directory
   of this project, run:
   ```sh
    python3 -m venv venv
   ```
3. After the virtual environment is created, it needs to be **activated**.
   
   _This step needs to be every time you want to use this project and run its code because the environment
   automatically `deactivate`'s once your terminal window is closed._

   **To active** the environment:
   - Linux / MacOS: Run:
    ```sh
        source venv/bin/activate
    ```
    - Windows: Run:
    `./venv/Scripts/activate.bat` or `./venv/Scripts/activate.ps1` _(whichever works)_.
4. _(Optional)_ If all was successful, your terminal's session should be within the Python's virtual environment.
   You can verify that by running `echo $VIRTUAL_ENV` on Linux, or `echo %VIRTUAL_ENV%` on Windows.
   The output directory path should point to `venv`. Trimmed example: `.../datamunge/venv`.
   
   Additionally, if your virtual environment has been freshly created, it will only have 1 _(pip)_ package installed within it,
   run `pip list` to see the packages installed inside the virtual environment.
5. Lastly, once within the virtual environment, install all of the packages the project needs by running:
   ```sh
    pip install -r requirements.txt
   ```
   _(If you run `pip list` again, you will notice that the list of installed packages within the environmnent has grown.)_
6. _(Conditional)_ **Refer to this if you have already done the virtual environment setup in the past**, and installed the
   packages it needs.
   
   It's possible that since your last setup the project has introduced new packages that you don't have installed **yet**.
   You may notice this by getting missing package import errors whilst attempting to run some of the code within the project.
   
   **To ensure** your previously created environment is **up-to-date**, run: 
   ```sh
    pip install --upgrade -r requirements.txt
   ```
   to upgrade old package versions, and/or to install new missing packages.

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

   Install it using your package manager. For **apt**:
   ```sh
    sudo apt update && sudo apt install package_name
   ```
   For **pacman**
   ```sh
    sudo pacman -Sy package_name
   ```
4. You will need to have/install a text editor. **Visual Studio Code** is recommended.
