# CSE-6324-ADV-TOPS-SOFTWARE-ENGINEERING

1) For Issue 1 the dependant files are condition.py, function.py, node.py, operation.py, slither.py, temp.py, temporary.py
2) For Issue 2 the dependant files are call_graph.py
3) The first issue that we are addressing here is the IR (Intermediate Representation) disorder in the nested ternary operation.
4) The second issue that we are addressing here is the functional overloading in call graph printer

Steps to run the program:

1) Install the slither analyzer using the command pip3 install slither-analyzer
2) Next clone the repository into your local machine using the command git clone https://github.com/Akansha9812/CSE-6324-ADV-TOPS-SOFTWARE-ENGINEERING.git
3) Then run the _main_.py file using the command python3 _main_.py 
4) Next run the Code_issue.sol Solidity file with the slither Code_issue.sol command 
5) To generate or to see the IR slither Code_issue.sol $slither --print slithir Code_issue.sol
6) Run the add.sol file to generate the issue 2 using the command slither add.sol
