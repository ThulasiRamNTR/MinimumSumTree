
#Get the input file path
#read the input file
#inputPS01Q1.txt
import os

def minimumSumTreeFromLeafNodes(leafNodesInorderInput): 
    result = 0
    inorderList = [int(i) for i in leafNodesInorderInput.strip().split()]

    while len(inorderList) > 1:
        min_Index = inorderList.index(min(inorderList)) 
        if 0 < min_Index < len(inorderList) - 1:
            result += min(inorderList[min_Index - 1],inorderList[min_Index + 1]) * inorderList[min_Index]
        else:
            result += inorderList[1 if min_Index == 0 else min_Index - 1] * inorderList[min_Index]
        result += inorderList[min_Index]
        inorderList.pop(min_Index)
    
    result += inorderList[0]
    return result

print("Minimum Sum Tree problem solution")
print("=================================")

#Preparing and getting inputFilePath, inputFile, and inputContent for processing
print("The input file is expected to be in the current directory: ")
print("Simply press enter to continue")
outputFilePath = input().strip()
try:
    inputFilePath = os.path.join(os.getcwd(), "inputPS01Q1.txt")
    inputFile = open(inputFilePath,"r")
    inputlines = inputFile.readlines()
except:
    print("No input file is found or error while reading the input file")
    exit()

#Preparing the output file for processing
print("The output would be written into outputPS01Q1.txt in the current directory: ")
print("Simply press enter to continue")
outputFilePath = input().strip()
if len(outputFilePath) == 0:
    outputFilePath = os.path.join(os.getcwd(), "outputPS01Q1.txt")
if os.path.exists(outputFilePath):
    os.remove(outputFilePath)
outputFile = open(outputFilePath, "w+")

#for each line of input in the file:
#implement the logic for finding the minimum sum

for inputline in inputlines:
    #the logic part
    minSum = minimumSumTreeFromLeafNodes(inputline)

    #for each ouput line, write into the output file
    #outputPS01Q1.txt
    outputFile.write(str(minSum) + "\n")

print("The problem has been executed and the output is written into outputPS01Q1.txt in the current directory/root folder")
inputFile.close()
outputFile.close()


