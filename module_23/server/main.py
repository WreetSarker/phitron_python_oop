""" object processor """

import glob
import shutil
import os
from zipfile import ZipFile


source_path = "../source/*"
destination_path = "../destination"
postfix = [1, 2, 3]
# os.mkdir('temp')
while True:

    source_object = glob.glob(source_path)

    if len(source_object) > 0: 

        object_path = source_object[0]
        


        object_name = object_path.split('\\')[-1].split('.')
        
        prefix = object_name[0]
        postfix2 = object_name[1]
        
        # create zip
        zip_filename = 'some_txt.zip'
        zipObj = ZipFile(zip_filename, 'w')

        for item in postfix:
            filename = prefix + "_" + str(item) + '.' + postfix2
            if postfix2.endswith('.txt'):
                shutil.copy(object_path, f'{destination_path}/{filename}')
                shutil.copy(object_path, f'./{filename}')
            elif postfix2.endswith('.py'):
                exec(filename)

            lines = []
            try:
                with open(f'{destination_path}/{filename}', 'r') as file:
                    lines = file.readlines()
                file.close()
                with open(f'{destination_path}/{filename}', 'w') as file:
                    for idx, line in enumerate(lines):
                        if (idx+1) <= item*10:
                            file.write(line) 
                file.close()
            except:
                print("Error")
        directory = '.'
        for fname in os.listdir(directory):
            f = os.path.join(directory, fname)
            if os.path.isfile(f):
                if f.endswith('.txt'):
                    zipObj.write(f)
                
        shutil.copy(zip_filename, f'{destination_path}/{zip_filename}')
        
        with ZipFile(f'{destination_path}/{zip_filename}', 'r') as zip_ref:
            zip_ref.extractall(f'{destination_path}')

        
        # shutil.copy(object_path, f'demo_folder/{filename}')
        # os.remove(object_path)
        # os.remove(object_path.split('\\')[-1])

