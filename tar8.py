import sys

src_path = sys.argv[1]
dest_path = sys.argv[2]
input_file = open(src_path,encoding="utf8")
input_file2 = open(dest_path,'w',encoding="utf8")
text = input_file.read()
text1 = text.split(" ")
del text1[0:int(len(text1)/2)]
maya = ' '.join(text1)
input_file2.write(maya)

