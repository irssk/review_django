from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm

# Create your views here.


def home(req):
    if req.method == "POST":
        form = ReviewForm(req.POST)

        # .isValid(<ur_value>)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect("https://google.com")

    else:
        form = ReviewForm()

    return render(req, "reviews/reviews.html", {
        "form": form
    })
