# color_dict={'red':'#FF0000',
#            'green':'#008000',
#            'black':'#000000',
#            'white':'#FFFFFF'}
# d=list(color_dict)
# print(d)

d={1:10,2:20,3:30,4:40,5:50,6:60}
i=eval(input("enter your number:"))
if i in d.keys():
    print("already exist")
else:
    print("ok")
