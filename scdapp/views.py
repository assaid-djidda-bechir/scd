from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .models import Client,Comment


def home(request):
    comments = Comment.objects.all()
    # qtySelect = 10
    context = {
        # 'qtySelect' :qtySelect,
        'comments' :comments,
    }
    return render(request,'home.html',context)


def order(request):
    if request.method == "POST":
        client = Client() 
        client.prenom = request.POST["prenom"]
        client.nom = request.POST["nom"]
        client.email = request.POST["email"]
        client.ville = request.POST["ville"]
        client.code_postal = request.POST["code_postal"]
        client.telephone = request.POST["telephone"]
        client.pays = request.POST["pays"]
        client.quantite = request.POST["quantite"]
        qty = int(client.quantite)
        amount = 120*qty
        
        send_mail(
            'Facture de la commande',
            # 'Vous avez commandé ' + client.quantite +' de produits qui coute '+ amount+' $',
            f"Vous avez commandé {client.quantite} de produits qui coute(nt) {amount} $",
            'succedn@gmail.com',
            [client.email],
            fail_silently=False 
        ) 
        context={
            'amount':amount,
            'qty':qty
        }
        
        client.save()
    # return redirect("home")
    return render(request,'order.html',context)

def comment(request):
    if request.method == "POST":
        comment = Comment()
        comment.nom = request.POST["nom"]
        comment.email = request.POST["email"]
        comment.avis = request.POST["avis"]
        
        
        
        comment.save()
        
    return redirect("home")