#!/usr/bin/env python3

import os
import subprocess
import readline

EXTRACTION_COMMAND = "jar tf {lib_path} | grep .class | tr / . | sed 's/\\.class$//' | xargs javap -public -cp {lib_path}"
"""
jar: 
    -t => Lists the table of contents for the archive
    -f => File Path 
    
javap:
    -public => Shows only public classes and members.
    -c => Prints disassembled code, for example, the instructions that comprise the Java bytecodes, for each of the methods in the class
    -p => Shows all classes and members.
"""



def get_functions_of_lib(lib_path: str) -> str: 
    print(EXTRACTION_COMMAND.format(lib_path=lib_path))
    result = subprocess.Popen(EXTRACTION_COMMAND.format(lib_path=lib_path), shell=True, stdout=subprocess.PIPE)
    return result.stdout.read().decode('utf-8')
    
    
if __name__ == '__main__':
    old_lib, new_lib = "", ""

    while(not os.path.exists(old_lib)): 
        old_lib = input('[-] Enter Old Lib Location: ')
        if (os.path.exists(old_lib)):
            break;
        print('[!] Unable to find the lib from the provided location!')
    
    while(not os.path.exists(new_lib)): 
        new_lib = input('[-] Enter New Lib Location: ')
        if (os.path.exists(new_lib)):
            break;
        print('[!] Unable to find the lib from the provided location!')


    old_lib_func = get_functions_of_lib(old_lib)
    new_lib_func = get_functions_of_lib(new_lib)
    
    for class_func_iter in old_lib_func.split('Compiled from '):
        class_not_printed = 1
        class_name = class_func_iter.split('\n')[0].strip('"').strip('.java')
        class_old_lib_func = [x.strip() for x in class_func_iter.split('\n')]
        class_old_lib_func.pop(0)
        
        for single_func in class_old_lib_func:
            if single_func not in new_lib_func:
                if (class_not_printed):
                    print('[+] Class ---> ' + class_name)
                    class_not_printed = 0
                    
                print(single_func)



