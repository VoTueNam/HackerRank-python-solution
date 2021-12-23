def timeConversion(s):
    if(s[8]=="P"):
        if s[0:2]=="12":
            return s[0:8]
        return str(int(s[0:2])+12)+s[2:8]
    elif s[0:2]=="12":
        return "00"+s[2:8]
    else:
    	return s[0:8]

print(timeConversion("12:45:54PM"))