from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from myapp.models import *


def adminhome(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        return render(request,'admin/homeindex.html')

def logout(request):
    request.session['lid'] = ''
    return redirect('/myapp/login/')


def login_get(request):
    return render(request,'login_index.html')

def login_post(request):
    username = request.POST['textfield']
    password = request.POST['textfield2']
    lg=login.objects.filter(user_name=username,password=password)
    if lg.exists():
        lg1 = login.objects.get(user_name=username, password=password)
        request.session['lid']=lg1.id
        if lg1.type == 'admin':
            obj = user.objects.all()
            point="5"
            obj1 = notification.objects.all()
            obj2 = complaint.objects.all()
            print(obj1)
            # user.objects.filter(LOGIN__id=request.session['lid']).update(point=point)
            return render(request,"admin/homeindex.html",{"data":obj,"data1":obj1,"data2":obj2})
        if lg1.type == 'user':
            return HttpResponse("<script>alert('user login success');window.location='/myapp/userhome/'</script>")
        else:
            return HttpResponse("<script>alert('invalid username or password');window.location='/myapp/login/'</script>")
    else:
        return HttpResponse("<script>alert('not found');window.location='/myapp/login/'</script>")

def view_user(request):
    if request.session['lid']=='':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:


        obj=user.objects.all()
        # return render(request,'Admin/viewusernew.html',{"data":obj})
        return render(request,'Admin/view_user.html',{"data":obj})
def view_user_Post(request):
    search = request.POST['textfield']
    obj=user.objects.filter(name__icontains=search)
    return render(request,'Admin/view_user.html',{"data":obj})


def admin_view_Book(request,userid):
    obj=Book.objects.filter(USER__id=userid)
    request.session['uid']=userid
    return render(request,'Admin/Book.html',{"data":obj})


def Book_post(request):
    search=request.POST['textfield']
    obj = Book.objects.filter(USER__id=request.session['uid'],name__icontains=search)
    return render(request, 'Admin/Book.html', {"data": obj})

def All_Book(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        obj=Book.objects.all()
        return render(request,'Admin/All_Book.html',{'data':obj })


def view_complaint(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        obj=complaint.objects.all()
    return render(request,'Admin/complaint.html',{'data':obj})
def complaint_post(request):
     fdate=request.POST['textfield']
     tdate=request.POST['textfield2']
     obj = complaint.objects.filter(date__range=[fdate,tdate])
     return render(request, 'Admin/complaint.html', {'data': obj})



def Admin_Change_Password(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        return render(request,'Admin/Admin_Change_Password.html')
def Admin_Change_Password_POST(request):
    old_passward = request.POST['textfield']
    print(old_passward)
    new_password = request.POST['textfield2']
    conform_password = request.POST['textfield3']
    res=login.objects.filter(password=old_passward,id=request.session['lid'])
    if res.exists():
        if new_password==conform_password:
            login.objects.filter(password=old_passward, id=request.session['lid']).update(password=conform_password)
            return HttpResponse("<script>alert('changed successfully');window.location='/myapp/login/'</script>")
        else:
            return HttpResponse("<script>alert('password incorrect');window.location='/myapp/Admin_Change_Password/'</script>")
    else:
        return HttpResponse("<script>alert('not fount');window.location='/myapp/Admin_Change_Password/'</script>")


def Send_notification(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        return render(request,'Admin/Send_notification.html')
def Send_notification_POST(request):
    # date = request.POST['date']
    Notification = request.POST['textarea']

    obj=notification()
    obj.notification=Notification
    from datetime import datetime
    obj.date=datetime.now().today()
    obj.save()
    return HttpResponse("<script>alert('send successfully');window.location='/myapp/adminhome/'</script>")


def reply_complaints(request,id):
    obj=complaint.objects.filter(id=id)
    return render(request,'Admin/reply_complaints.html',{'data':obj,"cid":id})


def reply_complaints_POST(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        reply = request.POST['textfield']
        cid=request.POST['cid']
        obj=complaint.objects.filter(id=cid).update(reply=reply,status="replied")

    return HttpResponse("<script>alert('send successfully');window.location='/myapp/view_complaint/'</script>")


def View_notification(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        obj=notification.objects.all()
    return render(request,'Admin/View_notification.html',{"data":obj})
def View_notification_POST(request):
    fdate = request.POST['textfield']
    tdate = request.POST['textfield2']
    obj=notification.objects.filter(date__range=[fdate,tdate])
    return render(request,'Admin/View_notification.html',{"data":obj})

def delete_notification(request,id):
    obj=notification.objects.get(id=id).delete()
    return HttpResponse("<script>alert('delete successfully');window.location='/myapp/View_notification/'</script>")

def view_payments(request):
    obj = payment.objects.all()
    return render(request, 'Admin/view_payments.html',{'data':obj})


#############################################

def userhome(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        return render(request,'User/userindex.html')


def registeration(request):
    return render(request,"registraction_index.html")
def registeration_post(request):
    name=request.POST['textfield']
    DOB=request.POST['textfield2']
    Place=request.POST['textfield3']
    Post=request.POST['textfield4']
    Pin_Code=request.POST['textfield5']
    District=request.POST['textfield6']
    State=request.POST['textfield7']
    Photo=request.FILES['filefield']

    fs=FileSystemStorage()
    from datetime import datetime
    date=datetime.now().strftime("%Y%m%d%H%M%S")+".jpg"
    fs.save(date,Photo)
    path=fs.url(date)

    Gender=request.POST['Gender']
    Phone_number=request.POST['textfield10']
    email=request.POST['textfield11']
    passward=request.POST['textfield12']
    conform_passward=request.POST['textfield13']
    refference=request.POST['textfield14']
    point = 5

    a = user.objects.filter(refference=refference)
    if a.exists():
        ab=user.objects.get(refference=refference)
        ap=ab.point
        ab.point=int(ap)+2
        ab.save()

    else:
        point = 5

    if passward==conform_passward:

        l=login()
        l.user_name=email
        l.password=conform_passward
        l.type='user'
        l.save()


        import random
        u=user()
        u.name=name
        u.date_of_birth=DOB
        u.place=Place
        u.post=Post
        u.pin=Pin_Code
        u.district=District
        u.state=State
        u.photo=path
        u.gender=Gender
        u.phone_number=Phone_number
        u.email=email
        u.LOGIN=l
        # u.refference=refference
        u.point=point
        u.refference=random.randint(00000,99999)
        u.save()
        return HttpResponse("<script>alert('Registered successfully');window.location='/myapp/login/'</script>")
    else:
        return HttpResponse("<script>alert('incorrect passward');window.location='/myapp/registeration/'</script>")



def User_Change_Password(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        return render(request,'User/User_Change_Password.html')
def User_Change_Password_post(request):
    old_passward = request.POST['current_password']
    # old_passward = request.POST['textfield']
    print(old_passward)
    new_password = request.POST['new_password']
    # new_password = request.POST['textfield2']
    conform_password = request.POST['confirm_password']
    # conform_password = request.POST['textfield3']
    res=login.objects.filter(password=old_passward,id=request.session['lid'])
    if res.exists():
        if new_password==conform_password:
            login.objects.filter(password=old_passward, id=request.session['lid']).update(password=conform_password)
            return HttpResponse("<script>alert('changed successfully');window.location='/myapp/login/'</script>")
        else:
            return HttpResponse("<script>alert('password incorrect');window.location='/myapp/User_Change_Password.html/'</script>")
    else:
        return HttpResponse("<script>alert('not fount');window.location='/myapp/User_Change_Password.html/'</script>")


def View_Profile(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        data=user.objects.get(LOGIN=request.session['lid'])
        return render(request,'User/View_Profile.html',{'data':data})


def Update_Profile(request):
    data=user.objects.get(LOGIN=request.session['lid'])

    return render(request,'User/Update_Profile.html',{'data':data})

def Update_Profile_post(request):
    name = request.POST['textfield']
    DOB = request.POST['textfield2']
    Place = request.POST['textfield3']
    Post = request.POST['textfield4']
    Pin_Code = request.POST['textfield5']
    District = request.POST['textfield6']
    State = request.POST['textfield7']
    Gender = request.POST['Gender']
    Phone_number = request.POST['textfield10']
    email = request.POST['textfield11']

    u = user.objects.get(LOGIN_id=request.session['lid'])
    if 'textfield8' in request.FILES:
        Photo = request.FILES['textfield8']
        fs = FileSystemStorage()
        from datetime import datetime
        date = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpj"
        fs.save(date, Photo)
        path = fs.url(date)
        u.photo=path
        u.save()

    u.name = name
    u.date_of_birth = DOB
    u.place = Place
    u.post = Post
    u.pin = Pin_Code
    u.district = District
    u.state = State
    u.gender = Gender
    u.phone_number = Phone_number
    u.email = email
    u.save()

    login.objects.filter(id=request.session['lid']).update(user_name=email)
    return HttpResponse("<script>alert('update successfully');window.location='/myapp/View_Profile/'</script>")


def List_Book(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        return render(request,'User/List_Book.html')
def List_Book_post(request):
    Name=request.POST['textfield']
    Condition=request.POST['textfield2']
    Prize=request.POST['textfield3']
    Author_Name=request.POST['textfield4']
    description=request.POST['textfield5']
    point=request.POST['textfield6']
    photo=request.FILES['photo']

    fs = FileSystemStorage()
    from datetime import datetime
    date = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    fs.save(date, photo)
    path = fs.url(date)

    bobj=Book()
    bobj.name=Name
    bobj.condition=Condition
    bobj.prize=Prize
    bobj.author_name=Author_Name
    bobj.description=description
    bobj.point=point
    bobj.USER=user.objects.get(LOGIN__id=request.session['lid'])
    bobj.photo=path
    bobj.save()
    return HttpResponse("<script>alert('listed successfully');window.location='/myapp/List_Book/'</script>")



def View_Book(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        bobj=Book.objects.filter(USER__LOGIN__id=request.session['lid'])
        return render(request,'User/View_Book.html',{'data':bobj})

def View_Book_post(request):
    search=request.POST['textfield']
    bobj=Book.objects.filter(USER__LOGIN__id=request.session['lid'],name__icontains=search)
    return render(request,'User/View_Book.html',{'data':bobj})


def Update_Book(request,id):
    bobj=Book.objects.get(id=id)
    return render(request,'User/Update_Book.html',{'data':bobj})

def Update_Book_post(request):
    Name=request.POST['textfield']
    Condition=request.POST['textfield2']
    Prize=request.POST['textfield3']
    Author_Name=request.POST['textfield4']
    description=request.POST['textfield5']
    point=request.POST['textfield6']
    id=request.POST['id']
    bobj=Book.objects.get(id=id)

    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        from datetime import datetime
        date = datetime.now().strftime("%Y%m%d%H%M%S") + ".jpj"
        fs.save(date, photo)
        path = fs.url(date)
        bobj.photo = path
        bobj.save()

    bobj.name=Name
    bobj.condition=Condition
    bobj.prize=Prize
    bobj.author_name=Author_Name
    bobj.description=description
    bobj.point=point
    bobj.save()
    return HttpResponse("<script>alert('edit successfully');window.location='/myapp/View_Book/'</script>")

def Delete_Book(request,id):
    bobj=Book.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Delete successfully');window.location='/myapp/View_Book/'</script>")


def View_User_Request(request,bid):
    res=Request.objects.filter(BOOK__id=bid)
    request.session['bid']=bid
    return render(request,'User/View_User_Request.html',{'data':res})

def View_User_Request_post(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        Fdate = request.POST['textfield']
        Tdate = request.POST['textfield2']
        res=Request.objects.filter(BOOK__id=request.session['bid'],date__range=[Fdate,Tdate])
        return render(request,'User/View_User_Request.html',{'data':res})



def Accept_Request(request,id,bid):
    bb=Book.objects.get(id=bid)
    uu=user.objects.get(id=bb.USER.id)
    bpoint=bb.point
    upoint=uu.point
    print(bpoint)
    print(upoint)
    # if

    if upoint>=bpoint:
        Request.objects.filter(id=id).update(status="approved")
        tot=int(upoint)+int(bpoint)
        bb=Book.objects.filter(id=bid).update(status="SOLD")
        user.objects.filter(id=uu.id).update(point=tot)
        return HttpResponse("<script>alert('Request Accepted');window.location='/myapp/View_Book/'</script>")
    else:
        return HttpResponse("<script>alert('Insufficient Point');window.location='/myapp/View_Book/'</script>")


def Reject_Request(request,id):
    Request.objects.filter(id=id).update(status="rejected")
    return HttpResponse("<script>alert('Request Rejected');window.location='/myapp/View_Book/'</script>")



#def Accept_Table(request):
    #return render(request,'User/Accept_Table.html')

def Other_Book(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        bobj=Book.objects.exclude(USER__LOGIN__id=request.session['lid'])
        return render(request,'User/Other_Book.html',{'data':bobj})

def Other_Book_post(request):
    search=request.POST['textfield1']
    bobj = Book.objects.filter(name__icontains=search).exclude(USER__LOGIN__id=request.session['lid'])
    return render(request, 'User/Other_Book.html', {'data': bobj})

def Request_Book(request,bid):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        robj=Request()
        robj.USER=user.objects.get(LOGIN__id=request.session['lid'])
        robj.BOOK_id=bid
        robj.date=datetime.now().date()
        robj.status="pending"
        robj.save()
        return HttpResponse("<script>alert('Request sent');window.location='/myapp/Other_Book/'</script>")



def View_Request_Status(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        res=Request.objects.filter(USER__LOGIN__id=request.session['lid'])
        return render(request,'User/View_Request_Status.html',{'data':res})

def View_Request_Status_post(request):
    search=request.POST['textfield']
    res=Request.objects.filter(BOOK__name__icontains=search)
    return render(request,'User/View_Request_Status.html',{'data':res})


def UserView_notification(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        obj=notification.objects.all()
        return render(request,'User/UserView_notification.html',{'date':obj})
def UserView_notification_post(request):
    Fdate=request.POST['textfield']
    tdate=request.POST['textfield2']
    obj = notification.objects.filter(date__range=[Fdate, tdate])
    return render(request,'User/UserView_notification.html',{'data':obj})


def Review(request,bid):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        return render(request,'User/Review.html',{"bid":bid})
def Review_post(request):
    Rating=request.POST['rating']
    Review=request.POST['textfield2']
    bid=request.POST['bid']

    robj=review()
    robj.USER=user.objects.get(LOGIN__id=request.session['lid'])
    robj.BOOK_id=bid
    robj.date=datetime.now().date()
    robj.rating=Rating
    robj.review=Review
    robj.save()
    return HttpResponse("<script>alert('Review sent');window.location='/myapp/View_Request_Status/'</script>")

def View_Review(request,bid):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        request.session['bkid']=bid
        res=review.objects.filter(BOOK__id=bid)
        return render(request,'User/View_Review.html',{"data":res})

def View_Review_post(request):
    Fdate = request.POST['textfield']
    Tdate = request.POST['textfield2']
    res=review.objects.filter(BOOK__id=request.session['bkid'],date__range=[Fdate,Tdate])
    print(res,"kkkkkkk")
    return render(request, 'User/View_Review.html', {"data": res})


def User_Complaint(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        return render(request,'User/User_Complaint.html')
def User_Complaint_post(request):
    Complaint=request.POST['textfield']
    robj =complaint()
    robj.USER=user.objects.get(LOGIN__id=request.session['lid'])
    robj.date=datetime.now().date()
    robj.complaint=Complaint
    robj.reply="pending"
    robj.status="pending"
    robj.save()

    return HttpResponse("<script>alert('Complaint sent');window.location='/myapp/User_Complaint/'</script>")


def View_reply(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        res=complaint.objects.filter(USER__LOGIN__id=request.session['lid'])
    return render(request,'User/View_Reply.html',{"data":res})
def View_reply_post(request):
    Fdate= request.POST['textfield']
    Tdate= request.POST['textfield2']
    res=complaint.objects.filter(USER__LOGIN__id=request.session['lid'],date__range=[Fdate,Tdate])
    return render(request,'User/View_Reply.html',{"data":res})

def View_Exchange_History(request):
    if request.session['lid'] == '':
        return HttpResponse("<script>alert('Login Required');window.location='/myapp/login/'</script>")
    else:
        res=Request.objects.filter(BOOK__USER__LOGIN__id=request.session['lid'])
        return render(request,'User/View_Exchange_History.html',{'data':res})
def View_Exchange_History_post(request):
    Fdate = request.POST['textfield']
    Tdate = request.POST['textfield2']
    res = Request.objects.filter(BOOK__USER__LOGIN__id=request.session['lid'],date__range=[Fdate,Tdate])
    return render(request,'User/View_Exchange_History.html',{"data":res})

def View_Point(request):

    data=user.objects.get(LOGIN=request.session['lid'])
    return render(request,'User/View_Point.html',{'data':data})
# def View_Point_post(request):
#     return render(request,'User/View_Point.html')

###################################################3

def chat1(request, id):
    request.session["userid"] = id
    cid = str(request.session["userid"])
    request.session["new"] = cid
    qry = user.objects.get(LOGIN__id=cid)
    return render(request, "User/Chat.html", {'photo': qry.photo, 'name': qry.name, 'toid': cid})


def chat_view(request):
    fromid = request.session["lid"]
    toid = request.session["userid"]
    qry = user.objects.get(LOGIN_id=request.session["userid"])
    from django.db.models import Q

    res = chat.objects.filter(Q(FROM_ID_id=fromid, TO_ID_id=toid) | Q(FROM_ID_id=toid, TO_ID_id=fromid))
    l = []

    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.TO_ID_id, "date": i.date, "from": i.FROM_ID_id})

    return JsonResponse({'photo': qry.photo, "data": l, 'name': qry.name, 'toid': request.session["userid"]})


def chat_send(request, msg):
    lid = request.session["lid"]
    toid = request.session["userid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = chat()
    chatobt.message = message
    chatobt.TO_ID_id = toid
    chatobt.FROM_ID_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})

#################### grpchat #############

def grpchat1(request):
    return render(request, "User/Group_Chat.html")


def grpchat_view(request):
    fromid = request.session["lid"]
    qry = user.objects.get(LOGIN_id=request.session["userid"])
    from django.db.models import Q
    res = Group_chat.objects.all()
    l = []
    for i in res:
        l.append({"id": i.id, "message": i.message, "to": i.LOGIN_id, "date": i.date})
        cc=user.objects.get(LOGIN__id=i.LOGIN.id)
    return JsonResponse({'photo': qry.photo, "data": l, 'name': qry.name, 'toid': request.session["userid"]})


def grpchat_send(request, msg):
    lid = request.session["lid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Group_chat()
    chatobt.message = message
    chatobt.LOGIN_id = lid
    chatobt.date = d
    chatobt.save()

    return JsonResponse({"status": "ok"})

################################################


def raz_pay(request):
    import razorpay
    razorpay_api_key = "rzp_test_MJOAVy77oMVaYv"
    razorpay_secret_key = "MvUZ03MPzLq3lkvMneYECQsk"

    razorpay_client = razorpay.Client(auth=(razorpay_api_key, razorpay_secret_key))

    amt = 25
    amount= float(amt)*100

    # Create a Razorpay order (you need to implement this based on your logic)
    order_data = {
        'amount': amount,
        'currency': 'INR',
        'receipt': 'order_rcptid_11',
        'payment_capture': '1',  # Auto-capture payment
    }

    # Create an order
    order = razorpay_client.order.create(data=order_data)

    context = {
        'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],
    }

    obj = payment()
    obj.USER = user.objects.get(LOGIN__id=request.session['lid'])
    obj.date = datetime.now().today()
    obj.payment = 25
    obj.status = 'paid'
    obj.save()

    # D_req_main.objects.filter(id=id).update(p_status='paid')

    return render(request, 'User/payment.html',{ 'razorpay_api_key': razorpay_api_key,
        'amount': order_data['amount'],
        'currency': order_data['currency'],
        'order_id': order['id'],"id":id})