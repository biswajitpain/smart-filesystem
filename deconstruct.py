#!/usr/bin/python
import os ,sys ,json,hashlib
from collections import OrderedDict

list_of_bytes=[]
set_of_byte=[]

def hash_func(block_value):
	m = hashlib.md5()
	m.update(block_value)
	return m.hexdigest()


def deconstruct(file_name,block_size):
	
	with open(file_name, 'rb') as f, open ('dedup_deconstruct','w') as df:
	    while True:
	        data=f.read(int(block_size))   
	        if data == '':
	        	break
	        list_of_bytes.append(data)
	    d = OrderedDict()
	    for x in list_of_bytes:
	    	d[x] = True
	    for x in d:
	    	set_of_byte.append(x)
	    df.writelines(["%s" % item  for item in set_of_byte])

	total_file_size_in_bytes =len(list_of_bytes) * int(block_size)
	total_file_size_in_bytes_dedup = len(set_of_byte) * int(block_size)
	print "Required bytes to store (dedup)",total_file_size_in_bytes_dedup
	print "dedup file written in dedup_deconstruct"

def create_meta(file_name,block_size):
    file_meta={}
    block_hash={}

    for  idx ,val in enumerate(list_of_bytes):
		block_hash[idx]=hash_func(val)

    file_meta['FILE_NAME']=file_name
    file_meta['BLOCK_SIZE']=block_size
    file_meta['META_DATA']=block_hash
    file_meta['DEDUP_FILE_NAME']='dedup_deconstruct'

    with open('dedup_meta_data.json','w') as fp:
		json.dump(file_meta, fp)


    print "meta data written in dedup_meta_data.json"


if __name__=='__main__':
	file_name = sys.argv[1]
	block_size = sys.argv[2]


	deconstruct(file_name,block_size)
	create_meta(file_name,block_size)

