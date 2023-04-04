# CSE-6324-ADV-TOPS-SOFTWARE-ENGINEERING

Requirements

For Mac:

Install Homebrew (if not already installed) by running the following command in the terminal:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Install Python 3 by running the following command in the terminal:
brew install python

Install Slither by running the following command in the terminal:
pip3 install slither-analyzer


For Windows:

Install Python 3 from the official website: https://www.python.org/downloads/windows/

Add Python to the system's PATH variable by following the instructions in this tutorial: https://geek-university.com/python/add-python-to-the-windows-path/

Install Slither by running the following command in the Command Prompt:
pip install slither-analyzer


After Installing slither-analyzer:

Check the solidity version using the command solc --version, chnage the version of your solidity based on the smart contract code that you are running using the command pip3 install solc-select.

solc-select install <version number>

Then you can change the solc version using the command solc-select use 0.4.24.

Then run the smart contract code on your local machine using the command slither --print slithir <file_name>.sol
