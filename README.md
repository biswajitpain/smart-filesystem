##SMART file System

###Deconstruct

```python test-file.py  <filename> <block-size>```

###Dry Run

```python test-file.py testfile 5```

#####Required bytes to store (dedup) 10


###Reconstruct

```python test_file_reconstruct.py  <filename> <block-size>```

1. This will breaks the input file into the block-size and store into file_ddup
2. It creats a meta data in jason format in file named meta_data.json(its contains the block
position as key and hash of block data as value.
3.The simple hash function takes blocks as input and return the sum of ASCII value.(Not efficiant hash)
4. While doing reconstruction ,parsing the meta data file to get the position of the block .

###Dry Run
```
python test_file_reconstruct.py testfile 5
['Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', 'Hello', '\n']
set(['\n', 'Hello'])


Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello
Hello

```
