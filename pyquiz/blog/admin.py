from django.contrib import admin
from .models import Post, Comment, PostImage

# display these models on the admin page
admin.site.register(Post)
admin.site.register(Comment)
admin.stie.register(PostImage)