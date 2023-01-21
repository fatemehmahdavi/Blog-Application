from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
#from django.shortcuts import redirect
#from django.urls import reverse


# Create your views here.

posts_list = [
    {"id": 1, "post_name":"first_post", "test":" machine", "post_comment" : ["This post is great", "fantastic"]},
    {"id": 2, "post_name":"second_post", "post_comment" : ["I like this post", "great"]},
    {"id": 3, "post_name":"third_post", "post_comment" : ["I don't agree", "boring"]},


]



#shows recent posts and a welcome message in the index page
def starrting_page(request):
    return render(request, "blog/index.html")
    # all_posts = [(i["post_name"], i["post_comment"]) for i in posts_list]
#     recent_posts = posts_list[:2]
#     return render(request, "blog/index.html", context = {
#     "recent_posts": recent_posts
# })

#shows the list of all posts
def posts(request):
    return render(request, "blog/all-posts.html")
    # return render(request, "blog/posts.html", context= {
    #     "posts": posts_list
    # })

#shows details of a single post
def post_detail(request, slug):
    return render (request, "blog/post-detail.html")
    # post = posts_list[number-1]
    # return render(request, "blog/post.html", context = {
    #     "post_detail": post
    # })

# def post_detail_by_name(request, name:str):
#     message = 'undefined'
#     for post in posts_list:
#         if post['post_name'] == name:
#             message = post['id']
#             redirect_path = reverse("month-challenge-str", args = [redirect_month])
#             return HttpResponseRedirect(redirect_path)
    
    # return HttpResponse(message)1



