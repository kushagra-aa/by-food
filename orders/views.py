import string
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from . import models

# food items
foods=[
        {
            'id':'1',
            'name':'veg Biryani',
            'price':'200',
            'url':'https://i2.wp.com/www.bharatzkitchen.com/wp-content/uploads/2018/07/soyabiryani6.jpg?resize=575%2C262&ssl=1',
        },
        {
            'id':'2',
            'name':'noodles with Chilli paneer',
            'price':'150',
            'url':'https://samosastreet.com/wp-content/uploads/Sweet-Sour-Paneer-3.jpg',
        },
        {
            'id':'3',
            'name':'veg burger',
            'price':'70',
            'url':'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F9%2F2021%2F07%2F13%2FUltimate-Veggie-Burgers-FT-Recipe-0821.jpg',
        },
        {
            'id':'4',
            'name':'Chow Mein',
            'price':'80',
            'url':'https://www.chilitochoc.com/wp-content/uploads/2021/03/Desi-Chow-Mein-2.jpg',
        },
        {
            'id':'5',
            'name':'cheese sandwich',
            'price':'100',
            'url':'https://media.30seconds.com/tip_image/lg/Fancy-Grilled-Cheese-Sandwich-Ideas-9269-d59e3c2cf0-1615604923.jpg',
        },
        {
            'id':'6',
            'name':'Tomato Basil Soup',
            'price':'70',
            'url':'https://www.chilitochoc.com/wp-content/uploads/2022/01/Roasted-Tomato-Basil-Soup-with-cream-swirls.jpg',
        },
        {
            'id':'7',
            'name':'veg thali',
            'price':'220',
            'url':'https://bestinnashik.com/wp-content/uploads/2021/02/best-thali-in-nashik-Best-in-Nashik.jpg',
        },
        {
            'id':'8',
            'name':'choley bhature',
            'price':'120',
            'url':'https://curlytales.com/wp-content/uploads/2017/06/Shiv-Mishthan-Bhandar.jpg',
        },
        {
            'id':'9',
            'name':'veg roll',
            'price':'50',
            'url':'https://spiderimg.amarujala.com/cdn-cgi/image/width=674,height=379.25,fit=cover,f=auto/assets/images/2019/01/21/750x506/roll_1548055223.jpeg',
        },
        {
            'id':'10',
            'name':'dosa',
            'price':'170',
            'url':'https://food.fnr.sndimg.com/content/dam/images/food/fullset/2019/10/9/DV3016_masala-dosa_s4x3.jpg.rend.hgtvcom.826.620.suffix/1570635680579.jpeg',
        },
        {
            'id':'11',
            'name':'kulfi',
            'price':'30',
            'url':'https://www.chilitochoc.com/wp-content/uploads/2021/07/mango-kulfi-2.jpg',
        },
        {
            'id':'12',
            'name':'pasta',
            'price':'130',
            'url':'https://lh3.googleusercontent.com/tkksCBSKT1UvqG1sfWaRZtwq_yL_ZE-AYWoDVs5-na8Fd6IkFoMmV4xbXdtaTQkzAXu92cxIyx2LEb2rzjmYqPviGADw=s320',
        },
        {
            'id':'13',
            'name':'pizza',
            'price':'330',
            'url':'https://img.buzzfeed.com/thumbnailer-prod-us-east-1/video-api/assets/216054.jpg?output-format=auto&output-quantity=auto&resize=600:*',
        },
        {
            'id':'14',
            'name':'aloo paratha',
            'price':'50',
            'url':'https://i0.wp.com/cookingfromheart.com/wp-content/uploads/2020/09/Aloo-Paratha-2.jpg?w=768&ssl=1',
        },
        {
            'id':'15',
            'name':'Cheesy Garlic Bread',
            'price':'150',
            'url':'https://www.chilitochoc.com/wp-content/uploads/2021/10/cheesy-garlic-bread-in-air-fryer-2.jpg',
        },
    ]

# * HELPER FINCTIONS
# check contains
def find(id,list):
    for item in list:
        if(item['id'] == str(id)):
            return item
    return -1

# Create your views here.
# page views
def index(request):
    return render(request,'home.html',{'foods':foods})
def food(request):
    return render(request,'food.html',{'foods':foods})
def loginPage(request):
    return render(request,'login.html')
def register(request):
    form=UserCreationForm()
    return render(request,'register.html',{'form':form})
def orderPage(request,item_id):
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        messages.success(request,'Login First')
        return redirect('byfood:login')
    item=find(item_id,foods)
    return render(request,'order.html',{'item':item})

# handle functions
def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'LoggedIn Successfully')
            return redirect('byfood:home')
        else:
            messages.success(request,'Invalid username or password')
            return redirect('byfood:login')
    else:
        return redirect('byfood:login')

def handleRegister(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,'register success')
            return redirect('byfood:home')
        return redirect('byfood:register')
    else:
        return redirect('byfood:register')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged out")
    return redirect('byfood:home')
    
def handleOrder(request):
    if request.method == 'POST':
        item_name = request.POST['item_name']
        item_id = request.POST['item_id']
        item_rate = request.POST['item_rate']
        quantity = request.POST['quantity']
        f_print = request.POST['f_print']
        order_cost = int(item_rate)*int(quantity)
        newform = models.Order.objects.create()
        newform.user_id = str(request.user.username)
        newform.item_name = item_name 
        newform.item_id = item_id 
        newform.item_rate = item_rate 
        newform.item_quantity = quantity
        newform.order_cost = order_cost
        newform.f_print = str(f_print)
        newform.save()
        messages.success(request,'Order Recived Sucessfully')
        return redirect('byfood:home')
    else:
        return redirect('byfood:home')