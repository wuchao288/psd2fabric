from psd_tools import PSDImage

from psd2fabric.parser.psd_parser import psd_to_fabric
from psd2fabric.render.json_render import dump_json_file

def dump_psd_json(psd,dump_file):
    psd = PSDImage.open(psd)
    fabric = psd_to_fabric(psd)
    dump_json_file(fabric,dump_file)

def dump_psd(psd_file):
    psd = PSDImage.open(psd_file)
    fabric = psd_to_fabric(psd)
    return fabric
    #return  dump_json_string(fabric)

#dump_psd_json("./asserts/猪大叔素材 (2).psd","./asserts/猪大叔素材 (2).json")

# import os
 
# # 设置文件夹路径
# folder_path = 'asserts'
 
# # 获取文件夹下所有文件的文件名
# files = [os.path.join(dirpath, file) for dirpath, dirnames, files in os.walk(folder_path) for file in files]

# import datetime 

# start1 = datetime.datetime.now()
# for filename in files:
#     names=filename.split(".")
#     if os.path.exists(names[0]+".json")==False and names[1]=="psd" :
#         try:
#             dump_psd(filename,filename.split(".")[0]+".json")
#             #_thread.start_new_thread( dump_psd, (filename,names[0]+".json"))
           
#         except Exception as e:
#             # 处理异常的代码块
#             print(filename+"发生了异常:", e)

# end1 = datetime.datetime.now()
# print('程序运行时间为: %s Seconds'%(end1-start1))