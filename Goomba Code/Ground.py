class Ground:
    def __init__(self, length: int):
        self.__length = length
        self.__ground_sprite = ["", ""]
        self.__set_sprite()

    def __set_sprite(self):
        ground_one_layer = "/" * self.__length
        self.__ground_sprite[0] = ground_one_layer
        self.__ground_sprite[1] = ground_one_layer

    def draw_sprite(self):
        for each_line in self.__ground_sprite:
            print(each_line)