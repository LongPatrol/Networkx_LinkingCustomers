# Networkx_LinkingCustomers
**The problem:**
Your company tracks business primarily by account number, but they would like to understand more about their customers (individuals/enterprises). Customers can have multiple account numbers. 
For one account, any related accounts are supposed to be written in a general comment field. This is not done consistenly, and sometimes account A links to B but Account B says nothing about Account A. 

How can we link related accounts together into Customer Groups?

**Answer:**
We can use the python package *networkx* to create a network of Customers using the account numbers as nodes and the comment reference as the edge. 


*Notes:*
For the purposes of this exercise, I created 13 accounts for 4 customers.

**Sources**

Printing the connected components:
https://stackoverflow.com/questions/26317775/print-connected-components-of-a-graph-in-python

Enumerating lists:
https://www.geeksforgeeks.org/enumerate-in-python/

Debugging blank lines:
https://stackoverflow.com/questions/11652806/csv-write-skipping-lines-when-writing-to-csv
