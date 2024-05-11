import json

from psd2fabric.fabric import FabricLayer, Fabric


def custom_default(obj):
    if isinstance(obj, (FabricLayer, Fabric)):
        return obj.__dict__
    return str(obj)


def render_json(obj: Fabric):
  
    if isinstance(obj.id, (tuple)):
        obj.id=obj.id[0]
    if isinstance(obj.width, (tuple)):
        obj.width=obj.width[0]
    if isinstance(obj.height, (tuple)):
        obj.height=obj.height[0]
    if isinstance(obj.zoom, (tuple)):
        obj.zoom=obj.zoom[0]
    

    return json.dumps(obj, default=custom_default, ensure_ascii=False)


def dump_json_file(obj, file):
    content = render_json(obj)
    with open(file, 'w',encoding='utf-8') as file:
        # 将字符串写入文件
        file.write(content)

def dump_json_string(obj, file):
    return render_json(obj)

