from django.shortcuts import HttpResponse, redirect
from django.shortcuts import render
from .models import Product, Review
import telebot
import os

BOT_TOKEN = os.getnv('BOT_TOKEN')
CHAT_ID = os.getnv('CHAT_ID')

bot = telebot.TeleBot(BOT_TOKEN)

def home(request):
    search = request.GET.get('search')

    if search:
        products = Product.objects.filter(name__contains=search).all()
    else:
        products = Product.objects.all()

    return render(request, "index.html", {
        'products': products,
        'products_found': len(products) > 0,
        'search': search if search else '',
    })

def view_product(request, id):
    product = Product.objects.filter(id=id).first()

    if request.method == "POST":
        author = request.POST.get('author')
        rating = request.POST.get('rating')
        usage_duration = request.POST.get('duration')
        text = request.POST.get('review')

        review = Review(
            product=product,
            author=author,
            rating=rating,
            usage_duration=usage_duration,
            text=text,
        )
        review.save()

    reviews = product.review_set.all()

    return render(request, 'product.html', {
        'product': product,
        'reviews': reviews,
    })

def payment(request, id):
    product = Product.objects.filter(id=id).first()

    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        # Send message to Telegram
        bot.send_message(CHAT_ID, f'''🏷️Новый заказ: {product.name}
💳Цена: {product.price} рублей

ФИО покупателя: {name}
Адрес доставки: {address}
''')
        return redirect('/success')

    return render(request, "payment.html", {
        'product': product
    })

def success(request):
    return render(request, 'success.html')