def measurementsRectangle(list):
    def area(list):
        if len(list) == 2:
            length = list[0]
            width = list[1]
            area = length*width
            return area
        else:
            side = list[0]
            area = side*side
            return area

    def perimeter(list):
        if len(list) == 2:
            length = list[0]
            width = list[1]
            perimeter = length + length + width + width
            return perimeter
        else:
            side = list[0]
            perimeter = side*4
            return perimeter
    return "Perimeter = " + str(perimeter(list)) +  " Area = " +  str(area(list))

if __name__ == '__main__':
    measurementsRectangle(list)