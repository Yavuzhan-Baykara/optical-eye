class Save_result():
    def make_txt(classId, x1, x2, y1, y2, width, height):
        cx = (x1 + x2)/ 2
        cy = (y1 + y2)/ 2
        cx = cx / width
        cy = cy / height
        xlen = (x2 - x1) / width
        ylen = (y2 - y1) / height
        return f'{classId} {cx} {cy} {xlen} {ylen}' 
