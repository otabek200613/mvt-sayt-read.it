from django.shortcuts import render, redirect,get_object_or_404
from .models import Home,Article,About,ContactUs
from .forms import ContactForm,CommentForm
from django.core.paginator import Paginator



def home(request):
    homes = Home.objects.filter(is_active=True)
    articles = Article.objects.filter(is_active=True)
    context = {
        'homes':homes,
        'articles':articles
        }

    return render(request,'index.html',context)











def about(request):
    homes = Home.objects.filter(is_active=True)
    abouts= About.objects.filter(is_active=True)


    context = {
        'abouts':abouts,
        'homes':homes
    }


    return render(request,'about.html',context)







def blog(request):
    homes = Home.objects.filter(is_active=True)
    articles = Article.objects.filter(is_active=True)
    p = Paginator(articles, 5)
    page = request.GET.get('page')
    articles = p.get_page(page)

    context = {'homes': homes,
               'articles':articles}
    return render(request,'blog.html',context)








def blogsingle(request, pk):
    article = get_object_or_404(Article, pk=pk, is_active=True)

    comments = article.comments.filter(is_published=True)

    form = CommentForm(request.POST or None)
    homes = Home.objects.filter(is_active=True)

    if request.method == 'POST' and form.is_valid():
        comment = form.save(commit=False)
        comment.article = article
        comment.save()
        return redirect('blogsingle', pk=article.pk)

    context = {
        'article': article,
        'comments': comments,
        'form': form,
        'homes': homes,
    }
    return render(request, 'blog-single.html', context)













def contact(request):
    homes = Home.objects.filter(is_active=True)
    contac_us= ContactUs.objects.filter(is_active=True)
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('.')
    context={
        'homes':homes,
        'contac_us':contac_us,
        'form':form
    }
    return render(request,'contact.html',context)
# Create your views here.
