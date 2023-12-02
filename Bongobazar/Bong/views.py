from django.db.models import Count
from django.shortcuts import render
from django.views import View
from . models import Product, Customer
from . forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request,"Bong/index.html") 

def about(request):
    return render(request,"Bong/about.html")

def contact(request):
    return render(request,"Bong/contact.html")  

class CategoryView(View):
    def get(self,request,val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(request,"Bong/category.html",locals())

class CategoryTitle(View):
    def get(self,request,val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,"Bong/category.html",locals())
    
class ProductDetail(View):
        def get(self,request,pk):
            product = Product.objects.get(pk=pk)
            return render(request, "Bong/productdetail.html",locals())
        
class CustomerRegistrationView(View):
        def get(self,request):
            form = CustomerRegistrationForm()
            return render(request, "Bong/customerregistration.html",locals())

        def post(self,request):
             form = CustomerRegistrationForm(request.POST)
             if form.is_valid():
                 form.save()
                 messages.success(request,"Congratulations! Registration Successfully")
             else:
                  messages.warning(request,"Invalid Data")
             return render(request, "Bong/customerregistration.html",locals())
class ProfileView(View):
       def get(self,request):
            form = CustomerProfileForm()
            return render(request, 'Bong/profile.html',locals())
       def post(self,request):
            form =CustomerProfileForm(request.POST)
            if form.is_valid():
                user = request.user
                name  = form.cleaned_data['name']
                locality = form.cleaned_data['locality']
                city = form.cleaned_data['city']
                mobile = form.cleaned_data['mobile']
                zipcode = form.cleaned_data['zipcode']
                state = form.cleaned_data['state']

                reg = Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,zipcode=zipcode,state=state)
                reg.save()
                messages.success(request,"Congratulations! Profile save Sucessfully")
            else:
                messages.warning(request,"Invalid Input Data") 
            return render(request, 'Bong/profile.html',locals())
       
def address(request):
     add = Customer.objects.filter(user=request.user)
     return render(request,'Bong/address.html',locals())
def add_to_cart(request):
     pass
        



