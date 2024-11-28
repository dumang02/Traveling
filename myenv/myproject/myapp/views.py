from django.shortcuts import redirect, render
from .models import*
# from .models import YourModel  # replace with your model
# from .forms import SearchForm  # type: ignore # replace with your model


# Create your views here.



# def login(request):
#     if 'email' in request.session:
#         return render(request,"myapp/Home.html")
#     else:
#         if request.POST:
#             email=request.POST['email']
#             password=request.POST['password']
#             uid=login.objects.get(email=email)
#             request.session['email']=uid.email
#             if uid.password==password:
#                 contaxt={
#                  'uid':uid,
#                 }
#                 return render(request,"myapp/Home.html",contaxt)
            
#             else:
#                 return render(request,"myapp/ad_login.html")
           
#         else:
#            return render (request,'myapp/ad_login.html')



def login1(request):
    if 'email' in request.session:
        return render(request,"myapp/ad_Home.html")
    else:
        if request.POST:
            email=request.POST['email']
            password=request.POST['password']
            uid=login.objects.get(email=email)
            request.session['email']=uid.email
            if uid.password==password:
                contaxt={
                 'uid':uid,
                }
                return render(request,"myapp/ad_Home.html",contaxt)
            
            else:
                return render(request,"myapp/ad_login.html")
           
        else:
           return render (request,'myapp/ad_login.html')

def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return render(request,'myapp/Home.html')
    else:
        return render(request,'myapp/Home.html')

def Home(request):
    return render(request,"myapp/Home.html")

def about(request):
    return render(request,"myapp/about.html")

def blog(request):
    return render(request,"myapp/blog.html")

def contact(request):
    return render(request,"myapp/contact.html")

def destination(request):
    return render(request,"myapp/destination.html")

def guide(request):
    return render(request,"myapp/guide.html")


def packageing(request):
    uid=package.objects.all()
    context={
        'uid': uid
        
    }
    return render(request,"myapp/package.html",context)

def service(request):
    return render(request,"myapp/service.html")

def signal(request):
    return render(request,"myapp/signal.html")

def testimonial(request):
    return render(request,"myapp/testimonial.html")


# def search_view(request):
#     query = request.GET.get('query')
#     results = []
#     if query:
#         results = YourModel.objects.filter(field_name__icontains=query)  # replace field_name with the actual field you want to search
#     return render(request, 'search_results.html', {'results': results, 'query': query})


def ad_home(request):
    return render(request,"myapp/ad_home.html")

# def ad_package(request):
    # if request.POST:
    #         pic=request.FILES['pic1']
    #         place=request.POST['place1']
    #         days=request.post['days1']
    #         person=request.POST['person1']
    #         explor=request.POST['explor1']
    #         price=request.POST['price1']
            
    #         package.objects.create(pic=pic,
    #                                    place=place,
    #                                    days=days,
    #                                    person=person,
    #                                    explor=explor,
    #                                    price=price)
    # return render(request,"myapp/add_package.html")
    
def package1(request):
    if request.POST:
        pic=request.FILES['pic1']
        place=request.POST['place1']
        days=request.post['days1']
        person=request.POST['person1']
        explor=request.POST['explor1']
        price=request.POST['price1']
        
        package.object.create(pic=pic,
                              place=place,
                              days=days,
                              person=person,
                              explor=explor,
                              price=price)
    return render(request,"myapp/add_package.html")


