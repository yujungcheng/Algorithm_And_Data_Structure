### tree/b_tree
- some bugs still exist.
- need to improve display of tree.

```
ycheng@nuc:/mnt/sdb/Data/learn/github/Algorithm_And_Data_Structure/tree$ ./b_tree.py

[ Display Tree ]
------------------------------------------------------------
7,12
3,5 10 14
0,1,2 4 8,9 13 15,16,17

[ Node info ]
------------------------------------------------------------
Tree Node: 2 values, 3 children
  values: [7, 12]
  children: ['3 to 5', '10 to 10', '14 to 14']

Tree Node: 2 values, 2 children
  values: [3, 5]
  children: ['0 to 2', '4 to 4']

Tree Node: 1 values, 1 children
  values: [10]
  children: ['8 to 9']

Tree Node: 1 values, 2 children
  values: [14]
  children: ['13 to 13', '15 to 17']


[ Display Tree ]
------------------------------------------------------------
7
3 11
1 9 13,15,17
0 8 12 14 16 18,19

[ Node info ]
------------------------------------------------------------
Tree Node: 1 values, 2 children
  values: [7]
  children: ['3 to 3', '11 to 11']

Tree Node: 1 values, 1 children
  values: [3]
  children: ['1 to 1']

Tree Node: 1 values, 2 children
  values: [11]
  children: ['9 to 9', '13 to 17']
```