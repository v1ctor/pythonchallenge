




s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def awful_decode(s):
    result = ""
    for ch in s:
        if ch is not " ":
            result += chr((ord(ch) - 97 + 2) % 26 + 97)
        else:
            result += " "
    return result


print(awful_decode(s))
print(awful_decode("map"))

