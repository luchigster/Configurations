'''生成cscope.files并生成out文件
'''
__revision__ = '0.1'
__author__ = 'lxd'

PATH= r'C:\GitHub\django'
FILE_TYPE_LIST= ['py']

if __name__ == '__main__':
    import os
    f = open('cscope.files','w')
    for root,dirs,files in os.walk(PATH):
        for file in files:
            for file_type in FILE_TYPE_LIST:
                if file.split('.')[-1] == file_type:
                    f.write('%s\n' %os.path.join(root,file))
    f.close()
    cmd = 'cscope -bk'
    os.system(cmd)
