PossibleEnds = [".hC",".HC",".hc","retpahc","retpahC"]

def substring_after(s, delim):
    return s.partition(delim)[2]

def format_title(s):
    title = s[6:]
    title = title[::-1]
    for ends in PossibleEnds:
        temp = title
        temp = substring_after(temp,ends)
        if (temp != "") and (len(temp) < len(title)):
            title = temp
    title = title[1:]
    title = title[::-1]
    return title



