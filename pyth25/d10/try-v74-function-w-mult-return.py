def format_name(fname, lname):
    if fname =="" or lname =="":
        return "There is no input in either fname or lname"
    print("Your title name is: " + fname.title() + " " + lname.title())
    return f"{fname.title()} {lname.title()}"

"""
This function formats the first name and last name into Title name
:param: a string that is first name ,and a string is the last name
:return: this function returns the title first name and title last name 
"""


def repeat(txt1):
    return txt1 + " " + txt1


def catch(txt2):
    return txt2.title()

firstname=input("input your first name:  ").lower()
print("last name you entered was ", firstname)

lastname=input("input your last name:  ").lower()
print("last name you entered was ", lastname)


formatted_string_from_function=format_name(firstname,lastname)
print("Returned string from fuction was:  "+formatted_string_from_function)



print("now this two function demo the use of return to a second fuction")
output_from_repeat= repeat("hello")
print("output from the repeat function:  "+output_from_repeat)
titled_output=catch(output_from_repeat)
print("now the titled repeated output is:  "+titled_output)