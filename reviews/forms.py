from django.forms import ModelForm


from .models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "user_name": "Enter your name : ",
            "review_text": "Enter what do you think about that course : ",
            "rating": "Enter a number between 1 and 5 as a rating to the course: "
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!;)",
                "max_length": "Please enter a message which will satisfy rules!;)"
            }
        }
