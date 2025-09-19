import re

def delem(numarra):
    numarra=numarra.replace("]["," ")
    numarra=numarra.replace("]","")
    numarra=numarra.replace("[","")
    numarra=numarra.split(" ")
    return numarra
    
def stringcalculator(name):
    nums = 0
    negn =[]
    try:
        if name == "":
            return nums
        elif name.startswith("//"):
            na=name.split()
            delm=na[0].replace("/","")
            delimiters=delem(delm)
            pattern = "|".join(re.escape(d) for d in delimiters)
            na1=re.split(pattern,na[1])
            for i in na1:
                try:
                    if int(i) > 0:
                        nums += int(i)
                    else:
                        negn.append(int(i))
                except :
                    continue
        else:
            na = re.split(r'[,\n]', name)
            for i in na:
                try:
                    if int(i) > 0:
                        nums += int(i)
                    else:
                        negn.append(int(i))
                except:
                    continue
        if negn:
            print(f"negative numbers not allowed : {negn}")
    except:
        nums=-1
    return nums


