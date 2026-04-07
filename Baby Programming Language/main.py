import lexer

srcCode = "3+43+100"
tokSeq = lexer.tokenize(srcCode)

for item in tokSeq:
    print(item)