#!/usr/bin/python
import os ,sys ,json,hashlib
from deconstruct import hash_func


file_name=""
block_size=""

file_meta={}
list_of_bytes=[]
set_of_byte=[]
de_dup_meta={}

def read_meta_file(meta_file_name):
    global file_name , set_of_byte  ,de_dup_meta
    global block_size , file_meta

    with open(meta_file_name, 'r') as fp : 
		file_meta_data= json.load(fp)
		file_name=file_meta_data['DEDUP_FILE_NAME']
		block_size=int(file_meta_data['BLOCK_SIZE'])
		file_meta = file_meta_data['META_DATA']
		


def reconstruct_dedup_file():
	with open(file_name, 'rb') as f:
	    while True:
	        data=f.read(int(block_size))   
	        if data == '':
	        	break
	        list_of_bytes.append(data)
	   


def meta_dict():
	for i in list_of_bytes:
		de_dup_meta[hash_func(i)]=i





def helpp():
	with open('output_file_reconstructrd', 'w') as op:
		for i in range(len(file_meta.keys())):
			if file_meta[str(i)] in de_dup_meta.keys():
				#print de_dup_meta[file_meta[i]]
				op.write(de_dup_meta[file_meta[str(i)]])
	print "file written in output_file_reconstructrd "			


if __name__=='__main__':
	
	meta_file_name = sys.argv[1]

	read_meta_file(meta_file_name)
	reconstruct_dedup_file()
	meta_dict()
	helpp()

	



