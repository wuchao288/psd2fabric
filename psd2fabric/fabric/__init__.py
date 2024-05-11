import uuid


class FabricLayer:
    def __init__(self, name, type, left, top, width, height):
     
        self.type = type
        self.originX = "left"
        self.originY = "top"
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.scaleX = 1
        self.scaleY = 1
        self.angle = 0
        self.flipX = False
        self.flipY = False
        self.opacity = 1
        self.visible = True
        self.backgroundColor = ""
        self.skewX = 0
        self.skewY = 0
        self.selectable = True
        self.hasControls = True
        self.id = str(uuid.uuid4())
        self.name = name

    def set_stroke(self, color, size):
        self.stroke = color
        self.strokeWidth = size


class Fabric:
    def __init__(self, objs, left, top, width, height):
     
        self.id:str=str(uuid.uuid4()),
        self.width:int= width,
        self.height:int= height,
        self.zoom:int=1,
        self.objects = [
            {
                "id": "WorkSpaceDrawType",
                "name": "rect",
                "fill": "",
                "selectable": False,
                "evented": False,
                "lockMovementX": False,
                "lockMovementY": False,
                "objectCaching": True,
                "transparentCorners": False,
                "hasBorders": True,
                "type": "Rect",
                "originX": "left",
                "originY": "top",
                "left": 0,
                "top": 0,
                "width": width,
                "height": height
                }
        ]
        self.clipPath = {
            "type": "rect",
            "originX": "left",
            "originY": "top",
            "left": left,
            "top": top,
            "width": width,
            "height": height
        }

        self.workSpace = {
            "fillType": 0,
            "left": 0,
            "top": 0,
            "angle": 0,
            "scaleX": 1,
            "scaleY": 1
        }

        #self.objects.append(workspace)
        for obj in objs:
            # print(obj)
            self.objects.append(obj)
