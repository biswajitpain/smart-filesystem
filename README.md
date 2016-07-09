##SMART file System

###Deconstruct

```python deconstruct.py  <filename> <block-size>```

###Dry Run

```(pyenv)bp:smrt-filesystem:-python deconstruct.py test_file_plain 6```

*Required bytes to store (dedup) 36*.

*dedup file written in dedup_deconstruct*.

*meta data written in dedup_meta_data.json*.

###Reconstruct

```python reconstruct.py  <meta_data_file>```


###Dry Run

``` (pyenv)bp:smrt-filesystem:-python reconstruct.py dedup_meta_data.json```

*file written in output_file_reconstructrd*
