from django.contrib import admin
from .models import Client, Comment


class ClientAdmin(admin.ModelAdmin):
    list_display = ("prenom","nom","email","ville","code_postal","telephone","pays","quantite",)
    list_filter =  ("nom","telephone","pays","quantite",)
    
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ("nom","email","avis",)
    list_filter =  ("nom","email","avis",) 
    


admin.site.register(Client,ClientAdmin)
admin.site.register(Comment,CommentAdmin)
