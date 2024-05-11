import json
import uuid
from flask import Flask,request,Response
 
from werkzeug.utils import secure_filename
import os

from psd2fabric.render.json_render import custom_default
from psd_fabric import dump_psd


def getResponse(code,msg,data):
     convert = dict()
     convert["data"]=data
     convert["msg"] = msg
     convert["code"]=code

     return Response(json.dumps(convert, default=custom_default, ensure_ascii=False), mimetype='application/json') 

app = Flask(__name__)


@app.route('/api/parse/file', methods=['POST'])
def upload_file():

    print(request.host)
    # 检查是否有文件在请求中
    if 'file' not in request.files:
        return  getResponse(code=500,msg="No file part")
    file = request.files['file']
    # 如果用户没有选择文件，浏览器也会提交一个没有文件名的空部分
    if file.filename == '':
         return  getResponse(code=500,msg="No selected file")
    if file.filename.endswith('.psd')==False:
         return  getResponse(code=500,msg="No .psd file")
    # 如果文件名是空的，那么也不进行保存
    if file:
        # 保存文件到服务器的uploads文件夹，文件名使用secure_filename保证安全
        filename='uploads/' +str(uuid.uuid4())+"_"+ secure_filename(file.filename)

        file.save(filename)
       
        obj=dump_psd(filename)

        if os.path.exists(filename):
             os.remove(filename)

        if isinstance(obj.id, (tuple)):
               obj.id=obj.id[0]
        if isinstance(obj.width, (tuple)):
               obj.width=obj.width[0]
        if isinstance(obj.height, (tuple)):
               obj.height=obj.height[0]
        if isinstance(obj.zoom, (tuple)):
               obj.zoom=obj.zoom[0]

        return getResponse(200,"success",obj)

if __name__ == '__main__':
    app.run(debug=False)