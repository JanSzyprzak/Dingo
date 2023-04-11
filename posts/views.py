from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Post, Author
from .forms import PostForm, AuthorForm


# Create your views here.

def posts_list(request):
    if request.method == "POST":
        form = PostForm(data=request.POST)
        author_from_form = Author.objects.get(id=request.POST['author'])
        new_post = Post(title=request.POST['title'], content=request.POST['content'], author = author_from_form)
        new_post.save()
        messages.add_message(
            request,
            messages.SUCCESS,
            "Dodano nowy post!!!!!!!!!!!!!!!!!!!!!!"
        )
     
       
    posts_list = Post.objects.all()
    form = PostForm()
    paginator = Paginator(posts_list, 7)
    page_number = request.GET.get('page')
    posts_list = paginator.get_page(page_number)
    return render(
       request=request,
       template_name="posts/posts_list.html",
       context={"posts_list": posts_list,
                'form':form
                }
   )


def post_details(request, id):
    post_details = Post.objects.get(id=id)
    return render(
        request=request,
        template_name="posts/post_details.html",
        context = {'post_details': post_details}
    )



def authors_list(request):
    authors_list = Author.objects.all()
    if request.method == 'POST':
        new_author = Author(nick=request.POST['nick'], email=request.POST['email'], bio = request.POST['bio'])
        new_author.save()
        messages.add_message(
            request,
            messages.SUCCESS,
            "Dodano nowego autora!!!!!!!!!!!!!!!!!!!!!!"
        )
    form = AuthorForm()
    return render(
        request = request,
        template_name="posts/authors_list.html",
        context = {'authors_list': authors_list,
                   'form': form
                   }
    ) 

def author_details(request, id):
    author_details = Author.objects.get(id=id)
    return render(
        request=request,
        template_name='posts/author_details.html',
        context = {'author_details': author_details}
    ) 




       
            
