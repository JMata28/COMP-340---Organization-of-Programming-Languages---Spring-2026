class token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return (f"Type: {self.type}, Value: {self.value} \n")

def tokenize(srcCode):
    tokSeq = []
    while srcCode != "":
        char = srcCode[0]
        if char == "+":
            newToken = token("PLUS",char)		
            tokSeq.append(newToken)
            srcCode = srcCode[1:]
        elif char == " ":
            srcCode = srcCode[1:]
        elif char.isdigit():
            numbStr = ""
            while char.isdigit():
                numbStr += char
                srcCode = srcCode[1:]
                if srcCode == "":
                    char = srcCode
                else:
                    char = srcCode[0]
            newToken = token("NUMBER",numbStr)
            tokSeq.append(newToken)
    return tokSeq
