""" This a project is a simple SNS application for end-term course work of University of London World Wide BSc Computer Science, CM3035 Advanced Web Development.<br/> This is Python Django based single-page web application with Ajax. This project use Foundation for a CSS/HTML framework.

# <center> Like and Unlike</center>

## 1. Urls.py

```
 path('like/<int:post_id>/', views.like, name="likes"),
```

## 2. [UnLike_Like(PostId)](blogapp/static/js/like_unlike.js)

```
function UnLike_Like(id) {
  var base_url = window.location.origin;
  var host = window.location.host;
  full_URL = base_url + "/like/" + id + "/";
  fetch(full_URL, {
    method: "POST",
    post_id: id,
  })
    .then((response) => response.json())
    .then((Like_or_Notlike) => {
      x = document.querySelector(".lc-" + id).innerHTML;
      if (Like_or_Notlike == "Liked") {
        y = parseInt(x) + 1;
      } else {
        y = parseInt(x) - 1;
      }
      document.querySelector(".lc-" + id).innerHTML = y;
    });
}

```

> ### Code Analysis
>
> 1.  Sends a POST request BackEnd that triggers like and unlike and realtime update the number of likes
> 2.  **`Click Red Heart to like the post`**

## 3. Views.py

```
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
@csrf_exempt
def like(request, post_id):
    if not request.user.is_authenticated:
        return JsonResponse('Please Log In ..!', safe=False)

    if request.method == 'POST':
        user = request.user

        like = Post.objects.get(postId=post_id)
        if user in like.likers.all():
            like.likers.remove(user)
            return JsonResponse('Unliked', safe=False)
        else:
            like.likers.add(user)
            return JsonResponse('Liked', safe=False)

```

> ### Code Analysis
>
> `csrf_exempt` to ease the workload in liking / unliking of post
>
> `jsonResponse` can be use in many different ways and is very helpful in big projects for convinient page loading and user experience
>
> 1.  Receive a POST from `UnLike_Like(id)` and verify whether user is logged and return json message prompting user to log in. `(id)` is the id of Post that user clicked
> 2.  Verify the request method and obtain the current user
>     - Check Whether the User already is included in Post likers
>     - return in JsonResponse that will be handled by the JavaScript `UnLike_Like(id)`
