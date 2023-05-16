# -*- coding: utf-8 -*-
"""
Created on Tue May 16 15:25:17 2023

@author: Cielo
"""

def get_todo(filepath='todos.txt'):
    with open(filepath, 'r') as f:
        todos = f.readlines()
    return todos

def write_todo(todos_arg, filepath='todos.txt'):
    with open(filepath, 'w') as f:
        f.writelines(todos_arg)
        
        
if __name__ == '__main__':
    print('This function works!')
