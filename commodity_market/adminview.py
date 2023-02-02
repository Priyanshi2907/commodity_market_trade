from django.shortcuts import render
from .import Pool
from. import  PoolDict


def adminlogin(request):
    emailaddress = request.POST.get('your_email')
    password = request.POST.get('your_pass')

    try:

        db,cmd = PoolDict.ConnectionPool()

        q="select * from admin where email='{}' and password='{}'".format(emailaddress,password)
        print(q)
        cmd.execute(q)
        result=cmd.fetchone()
        print(result)

        if(result):
            return render(request,'adminhome.html',{'msg':'Login Succesfully'})

        else:
            return render(request, 'adminlogin.html', {'msg': 'Invalid Email or password'})
    except Exception as e:
     print("error:",e)
     return render(request, 'adminlogin.html', {'result': {},'msg':'Server Error'})



def admininterface(request):
    return render(request,'adminlogin.html')



def displayall(request):
    try:
        db,cmd=Pool.ConnectionPool()
        q="select * from user"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,'displayadmin.html',{'rows':rows})
    except Exception as e:
       print(e)
       return render(request,'displayadmin.html',{'rows':[]})