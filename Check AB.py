def checkAB(str):
  
    if len(str)==0:
        return "true"

    if (len(str)>=3) and ((str[0]=="a") and (str[1]=="b") and (str[2]=="b")):
        print(str)
        print("Entering first condition")
        return checkAB(str[3:])
    elif str[0]=="a":
        print(str)
        return checkAB(str[1:])
    else:
        return "false"

str=input()
print(checkAB(str))