# Getting-Started-with-Python
Some notes to take when I got started with Python on my Mac

## Setting up Python on your new Mac for development is pretty straightforward. Here’s the best way to do it:

### 1. Install Homebrew (If You Haven’t Already)

Homebrew is a package manager that makes installing and managing software easier.

Open Terminal (Cmd + Space, type "Terminal").

Run this command to install Homebrew:

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

After installation, add Homebrew to your path (if prompted) by running:

`echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile`

`eval "$(/opt/homebrew/bin/brew shellenv)"`

### 2. Install Python Using Homebrew

Now that Homebrew is installed, install Python:

`brew install python`

To verify the installation:

`python3 --version`

It should show something like Python 3.x.x.

### 3. Install a Virtual Environment Manager 
### Recommended: please use a virtual environment whenever using python on your MAC to avoid mixing installed packages!
### Anything related to `pip install` should be done from a virtual environment. Best Practice!

For managing Python projects efficiently, you should use virtual environments.

Option 1: Using venv (Built-in)

Create a virtual environment in your project folder:

`python3 -m venv venv`

Activate it:

`source venv/bin/activate`

To deactivate:

`deactivate`

Option 2: Using pyenv (For Managing Multiple Python Versions)

If you need to switch between Python versions easily, install pyenv:

`brew install pyenv`

Then, add this to your ~/.zshrc file (if using zsh, the default shell on macOS):

`echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc`

`echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc`

`echo 'eval "$(pyenv init --path)"' >> ~/.zshrc`

`source ~/.zshrc`

Now you can install different Python versions:

`pyenv install 3.x.x`

`pyenv global 3.x.x`

### 4. Install Essential Python Packages

Once Python is installed, get the must-have development tools:

`pip install --upgrade pip setuptools wheel`

`pip install numpy pandas matplotlib jupyter flask django`

### 5. Install an IDE or Code Editor

VS Code (Recommended): Install from VS Code and add the Python extension.

PyCharm (For more structured Python projects).
