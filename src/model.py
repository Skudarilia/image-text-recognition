import easyocr


def init():
    reader = easyocr.Reader(['ru','en'], gpu=False)
    return reader


def get_result(reader, pic_path):
    result = reader.readtext(pic_path, detail=0)
    return result
