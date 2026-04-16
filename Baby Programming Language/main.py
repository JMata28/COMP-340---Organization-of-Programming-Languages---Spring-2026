import lexer
import parserr

#To test what we did for the lexer in class
# srcCode = "3+43+100"
# tokSeq = lexer.tokenize(srcCode)

# for item in tokSeq:
#     print(item)

#To test what we did for the parser in class
srcCode = "1 + 2 * 4 * 5" #Remember that this will only work if your lexer can process multiplications (Project 4 part 1)
tokSeq = lexer.tokenize(srcCode)
rootNode = parserr.parse(tokSeq)
parserr.printTree(rootNode)
print()

