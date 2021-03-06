def cloze(data):
    '''
    should be called if data[1]=="cloze"
    accepts a list of lists (full card data) and returns the formatted card data
    '''
    ret = ""
    #look for numbers if number is found check if it's immediately preceded by "c". Should not be double digit clozes lol wtf
    for n in range(0, len(data[0])):
        # Check if  start of cloze statement
        if data[0][n].isnumeric() and data[0][n-1].lower()=="c":
            # First cloze
            if ret == "":
                ret = data[0][0:n-1] + cloze_it(data[2][0]) # Calls the cloze formatter
                data[2]=data[2][1:] # Slice used cloze arguements
                # Future: pass the index of data[cloze] to get c2 and stuff
            # Subsequent clozes
            else:
                ret = ret[0:-1] + cloze_it(data[2][0])
        # Normal chars
        else:
            ret += data[0][n]
    ret = [ret, "cloze", ""] + data[3:]
    return ret

def cloze_it(string, rep="..."):
    '''
    Formats cloze statements
    Always with cloze number 1
    Default replacement is ..., can be changed with an indicator in string.

    "cloze statement|replacement" -> "cN::cloze statement::replacement"
    '''
    # Check for replacement
    if "|" in string:
        rep, string = string.split("|")[1], string.split("|")[0]
        if rep[0] == " ": # Remove unnecessary extra space
            rep = rep[1:]
    # Format cloze
    ret = "{"+f'{{c1::{string}::{rep}}}'+"}"
    return ret

def check_cloze(row):
    if "cloze" in row[1].lower():
        return True
    return False

d=['c1 this is patrick', 'Cloze', 'no', 'From spongggebob', 'physiology', 'planes, respiration', '']
print(cloze(d))