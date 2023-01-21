from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from datetime import date
#from django.shortcuts import redirect
#from django.urls import reverse

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Maximilian",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]
# Create your views here.

# posts_list = [
#     {"id": 1, "post_name":"first_post", "test":" machine", "post_comment" : ["This post is great", "fantastic"]},
#     {"id": 2, "post_name":"second_post", "post_comment" : ["I like this post", "great"]},
#     {"id": 3, "post_name":"third_post", "post_comment" : ["I don't agree", "boring"]},


# ]

def get_date(post):
    return post['date']

#shows recent posts and a welcome message in the index page
def starrting_page(request):
   sorted_posts = sorted(all_posts, key=get_date) #sort the posts by their date. we don't execute get_date and python executes get_date for us for every post when it sorts that posts list so it goes through the posts list calls get_date for every post in that list to get that date and compares the dates with eachother to sort the overall arrray
   latest_posts = sorted_posts[-3:]
   return render (request, "blog/index.html", context = {
    "latest_posts": latest_posts
   })


#shows the list of all posts
def posts(request):
    return render(request, "blog/all-posts.html", context = {
        "all_posts":all_posts
    })
    # return render(request, "blog/posts.html", context= {
    #     "posts": posts_list
    # })

#shows details of a single post
def post_detail(request, slug):
    ientified_post = next(post for post in all_posts if post['slug'] == slug)
    return render (request, "blog/post-detail.html", context={
        "post":ientified_post
    })
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



