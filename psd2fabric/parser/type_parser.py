
from psd_tools.api.layers import TypeLayer

from psd2fabric.fabric.text import TextFabricLayer

import math

def parse(layer: TypeLayer, relate_x, relate_y):
   

    text = layer.engine_dict['Editor']['Text'].value


    fontset = layer.resource_dict['FontSet']
    styleSheetSet = layer.resource_dict['StyleSheetSet']
    engineDict = layer.engine_dict
    runlength = engineDict["StyleRun"]["RunLengthArray"]
    rundata = engineDict["StyleRun"]["RunArray"]
    paragraph_rundata = engineDict['ParagraphRun']['RunArray']
    writingDirection = engineDict["Rendered"]["Shapes"]["WritingDirection"]
    index = 0
    lineHeight=0.86
    charSpacing=0
    for length, style, paragraph in zip(runlength, rundata, paragraph_rundata):
        # just use the first one
        # substring = text[index:index + length]
       
        stylesheet = style['StyleSheet']['StyleSheetData']

        paragraphsheet = paragraph['ParagraphSheet']['Properties']
        if 'Font' in stylesheet:
            fontType = stylesheet['Font']
        else:
            fontType = styleSheetSet[index]['StyleSheetData']['Font']

        if 'FontSize' in stylesheet:
            font_size = stylesheet['FontSize']
        else:
            font_size = styleSheetSet[index]['StyleSheetData']['FontSize']

        font_size = get_size(font_size, layer.transform)
       
        if "Leading" in stylesheet and stylesheet["Leading"]>0 and font_size>0:
             lineHeight=stylesheet["Leading"]
             lineHeight=(lineHeight/font_size)
             lineHeight=get_lineHeight(lineHeight,layer.transform)


        if "Tracking" in stylesheet and stylesheet["Tracking"]>0 and font_size>0:
            charSpacing=stylesheet["Tracking"]
            #charSpacing=get_charSpacing(charSpacing,layer.transform)

        if 'Name' in fontset[fontType]:
            font_name = fontset[fontType]['Name']
        else:
            font_name = "Microsoft YaHei"
        
        font_name=get_name(str(font_name))

        if 'FillColor' in stylesheet:
            font_color = get_color(stylesheet['FillColor']['Values'])
        else:
          
            font_color =get_color(styleSheetSet[index]['StyleSheetData']["FillColor"]["Values"])
        break
    
    
    tlayer = TextFabricLayer(layer.name, layer.left - relate_x, layer.top - relate_y, layer.width, layer.height)
    text = get_text(text)

    tlayer.set_text(
        font_name,
        font_size,
        font_color,
        get_bold(stylesheet),
        get_align(paragraphsheet),
        # writingDirection = 2 表明是竖版字，使用换行符实现竖版字
        text if writingDirection != 2 else "\n".join(list(text.replace("\n", ""))),
        lineHeight,
        charSpacing
    )
    return tlayer


def get_color(color):
    rgba_values = [round(c * 255, 0) for c in color]
    return f"rgba({','.join(map(str, rgba_values[1:]))},{rgba_values[0]})"


def get_size(font_size, transform):
    return font_size*transform[0]

def get_lineHeight(line_height, transform):
    print(transform)
    return round(line_height*transform[0]*0.9,2)

def get_charSpacing(char_pacing, transform):
    return char_pacing*transform[0]

def get_text(text):
    return text.replace('\r', '\n').replace("\t","    ")

def get_name(text):
    return text.replace("'", "")

def get_align(paragraphsheet):

    
    if not 'Justification' in paragraphsheet:
        return 'justify-left'

    if paragraphsheet['Justification'] == 1:
        return 'justify-right'
    elif paragraphsheet['Justification'] == 2:
        return 'justify-center'

    return 'justify-left'

def get_bold(stylesheet):
    if 'FauxBold' in stylesheet:
        return stylesheet['FauxBold']
    return False