class DimensionConverter:
    def __init__(self, dimension_mm, resolution_pixels):
        self.dimension_mm = dimension_mm
        self.resolution_pixels = resolution_pixels

    def convert(self, pixel_value):
        pixel_size = self.dimension_mm / self.resolution_pixels
        physical_value = pixel_value * pixel_size
        return physical_value

class WidthConverter(DimensionConverter):
    pass

class HeightConverter(DimensionConverter):
    pass


def ext(num):
    a = num - 330
    b = num + 330
    return a, b


width_converter = WidthConverter(1100, 4096)
print(width_converter.convert(6107))

a, b = ext(6107)

liste = [a, b]

print()
print()
print()
print("-----------------------------")

for i in range(len(liste)):
    width_converter = WidthConverter(1100, 4096)
    print(f'{liste[i]} için:' + str(width_converter.convert(liste[i])))


    width_converter = WidthConverter(960, 4096)
    print(f'{liste[i]} için:' + str(width_converter.convert(liste[i])))


    width_converter = WidthConverter(1000, 4096)
    print(f'{liste[i]} için:' + str(width_converter.convert(liste[i])))


    width_converter = WidthConverter(1035, 4096)
    print(f'{liste[i]} için:' + str(width_converter.convert(liste[i])))


    width_converter = WidthConverter(1050, 4096)
    print(f'{liste[i]} için:' + str(width_converter.convert(liste[i])))
    
    print("-----------------------------")


# width_mm = 975
# height_mm = 100
# resolution_pixels_width = 4096
# resolution_pixels_height = 256

# width_converter = WidthConverter(width_mm, resolution_pixels_width)
# physical_width = width_converter.convert(15)
# physical_width = round(physical_width, 2)
# print("Physical Width: ", physical_width, "mm")

# # height_converter = HeightConverter(height_mm, resolution_pixels_height)
# # physical_height = height_converter.convert(100)
# # physical_height = round(physical_height, 2)
# # print("Physical Height: ", physical_height, "mm")
