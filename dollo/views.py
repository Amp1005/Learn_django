from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    peoples =[
        {'name' : 'arjun', 'age' : 12 },
        {'name' :'dallwe', 'age' :21 },
        {'name' : 'raju', 'age' : 24 },
    ]
    text = """ Lorem ipsum dolor sit amet consectetur adipisicing elit. Inventore officiis repellendus nesciunt, ad adipisci, nulla facilis laboriosam magnam aut voluptate magni quod ratione minus asperiores maxime sed rerum reprehenderit impedit sit? Iure iusto ullam molestias? Sapiente reprehenderit voluptatibus sit blanditiis nemo temporibus qui inventore, impedit tempore eius fugit fuga sunt unde culpa quaerat autem quibusdam animi officia earum ex optio placeat. Eaque esse iure ducimus, fuga debitis laboriosam placeat rem nemo quia delectus eveniet natus nostrum animi molestias! Ipsum ullam error voluptas sint ad, reiciendis animi quaerat consequatur explicabo necessitatibus earum dolorum unde perspiciatis exercitationem beatae quo hic qui repellendus."""
    context = {
        'peoples': peoples,
        'text': text,
        'page' : 'Home'
    }
    return render(request, "dollo/index.html", context )

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1> Hey this is a success page</h1>")

def contact(request):
    context = {
        'page': 'Contact'
    }
    return render(request, "dollo/contact.html", context )

def about(request):
    context = {
        'page': 'About'
    }
    return render(request, "dollo/about.html", context )
