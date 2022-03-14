import os
import shutil
#os.system("date")
#os.mkdir("test_folder")
print(os.getcwd())
path = "C:/Users/r_aha/OneDrive/Amu - WhiteHat JR/c99/test_folder/test.txt"
exist= os.path.exists(path)
print(exist)
root_ext=os.path.splitext(path)
print("rootpart",root_ext[0])
print("extpart",root_ext[1])
print(os.listdir())
src_path = "C:/Users/r_aha/OneDrive/Amu - WhiteHat JR/c99/test_folder/test.txt"
dest_path = "C:/Users/r_aha/OneDrive/Amu - WhiteHat JR/c99/test.txt"
#dest=shutil.copy(src_path,dest_path)
dest=shutil.move(src_path,dest_path)
