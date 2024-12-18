stud_info= {"grno":1111,
                       "stnm":"ABCDE",
                        "class":"BCA-5",
                       "City":"Rajkot",
                       "BDT":"01-01-90",
                       "Result":"PASS"}
print("Dictionary Data are:")
print(stud_info)
print("Specific value: ",stud_info["stnm"])
for v in stud_info:
    print("Dictionary Key is: ",v,"Value is :",stud_info[v])
stud_info["stnm"]="XYZ"
print("Dictionary Data are:")
print(stud_info)
