from psd2fabric.fabric import FabricLayer


class TextFabricLayer(FabricLayer):
    def __init__(self, name, left, top, width, height):
     
        # 调用父类的构造方法
        super().__init__("textbox", "IText", left, top, width, height)
        self.pathAlign = None
        self.pathSide = None
        self.pathStartOffset = None
        self.direction = None
        self.styles = None
        self.charSpacing = None
        self.textBackgroundColor = None
        self.fontStyle = None
        self.textAlign = None
        self.linethrough = None
        self.overline = None
        self.underline = None
        self.fontWeight = None
        self.fontSize = None
        self.fontFamily = None
        self.layer=name

    def set_text(self, font_family, font_size, font_color, text_bold, text_align, text,lineHeight,charSpacing):
        self.fill = font_color
        self.fontFamily = font_family
        self.fontSize = font_size
        self.paintFirst = "stroke" # "fill"内边框
        self.text = text
        self.fontWeight = "normal"
        if text_bold:
            self.fontWeight = "bold"

        self.underline = False
        self.overline = False
        self.linethrough = False
        self.textAlign = text_align
        self.fontStyle = "normal"
        self.lineHeight = lineHeight
        self.textBackgroundColor = ""
        self.charSpacing = charSpacing
        self.styles = []
        self.direction = "ltr"
        self.pathStartOffset = 0
        self.pathSide = "left"
        self.pathAlign = "baseline"
