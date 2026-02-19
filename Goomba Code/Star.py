class Star:
    def __init__(self, posX):
        self.__posX = posX
        self.__starSprite = [None] * 6
        self.__set_sprite() #for setting star image to starSprite


    def __set_sprite(self):
        self.__starSprite[0] = "          "
        self.__starSprite[1] = "  ___/\\___"
        self.__starSprite[2] = "  \\  ||  / "
        self.__starSprite[3] = "  /__  __\\"
        self.__starSprite[4] = "     \\/   "
        self.__starSprite[5] = "          "

    def draw_sprite(self):
        spaces = " " * self.__posX
        for line in self.__starSprite:
            print(spaces + line)
