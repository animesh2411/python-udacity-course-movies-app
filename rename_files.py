import os
#operating system listdir lists everything in the folder
def rename_files():
    file_list = os.listdir(r"C:\Users\lenovo\Documents\Pyhtonprgms\prank")
    #get files from folder
    #r is for raw path
    #print(file_list)
    saved_path=os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir(r"C:\Users\lenovo\Documents\Pyhtonprgms\prank")
    
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - "+file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
        #renaming files and using the translate func to remove all the numeric entries
    os.chdir(saved_path)
                                                
rename_files()
