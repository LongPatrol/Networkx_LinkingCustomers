# Networkx_LinkingCustomers
**The problem:**
Your company tracks business primarily by account number, but they would like to understand more about their customers (individuals/enterprises). Customers can have multiple account numbers. 
For one account, any related accounts are supposed to be written in a general comment field. This is not done consistenly, and sometimes account A links to B but Account B says nothing about Account A. 

How can we link related accounts together into Customer Groups?

**Answer:**
We can use the python package *networkx* to create a network of Customers using the account numbers as nodes and the comment reference as the edge. 
