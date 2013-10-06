from django.contrib import admin
from grumblr.models import *

admin.site.register(Grumblr)
admin.site.register(Follow)
admin.site.register(Comment)
admin.site.register(Block)
admin.site.register(Dislike)
admin.site.register(DislikeCount)
