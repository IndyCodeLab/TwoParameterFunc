def calc_area(w = 1, h = 1):
    if w != 1 and h == 1:
        area = w * w
        print area
    else:
        area = w * h
        print area
        
calc_area()
calc_area(5)
calc_area(3, 10)
