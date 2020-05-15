def newemail(email,old,new):
    if "@" + old in email:
        index= email.index("@"+old)
        replace=email[:index]+"@"+new
        print(replace)
print("enter the emailid ,old domain ,newdomain")
newemail(email=(input()),old=(input()),new=(input()))
