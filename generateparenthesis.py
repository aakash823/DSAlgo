def generateparenthesis(left,right,stringsofar,result,count):
    if left == 0 and right == 0:
        result.append(stringsofar)
        count[0]+=1
        return

    if left > 0:
        generateparenthesis(left-1,right,stringsofar+"(",result,count)
    if right>left:
        generateparenthesis(left,right-1,stringsofar+")",result,count)

result = []
count = [0]
generateparenthesis(12,12,"",result,count)
print(result)
print(count)
