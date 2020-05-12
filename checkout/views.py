from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from django.contrib.auth.models import User
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings 
from django.utils import timezone 
from products.models import Product
from to_do.models import Feature

from to_do.forms import FeatureForm

import stripe 

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    """ Checkout function for buying a new feature ticket """

    user = request.user

    product = Product.objects.get(name="Request a new feature")

    quantity = 1

    total = quantity * product.price

    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        feature_form = FeatureForm(request.POST)

        if order_form.is_valid and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.user = user
            feature_form.save()
            order.save()

            # Save the product details to the order 
            total += quantity * product.price
            order_line_item = OrderLineItem(
                order = order,
                product = product,
                quantity = quantity
            )
            order_line_item.save()
            
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card has been declined")

            if customer.paid:
                request.session['cart'] = {}
                return redirect(reverse('invoice'))
            else:
                messages.error(request, "Sorry, we have not been able to take your payment")

        else:
            print(payment_form.errors)
            messages.error(request, "Sorry, we were unable to process your payment with that card")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
        feature_form = FeatureForm()

    return render(request, "checkout.html", {"order_form": order_form, 
                                              "payment_form": payment_form, 
                                              "publishable": settings.STRIPE_PUBLISHABLE,
                                             "feature_form": feature_form,
                                             "product": product,
                                             "total": total,
                                             "quantity": quantity})


@login_required()
def upvote_checkout(request, id):
    """ Checkout function for liking a feature.
    Once the payment has gone through then the like count 
    will increase """

    user = request.user

    # Pass through specific feature 
    if Feature.objects.filter(pk=id).exists():
        feature = get_object_or_404(Feature, pk=id)

    # If the user has already liked that specific feature they won't be able to pay for it again, 
    # they will be sent back to the home page with a message
    if user in feature.likes.all():
        messages.success(request, "You've already liked and paid for this feature")
        return redirect('home')
    
    # If they haven't already liked and paid for that feature 
    # they will be sent to the checkout form
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

        product = Product.objects.get(name="Upvote ticket")

        upvote_quantity = 1

        total = product.price * upvote_quantity

        # Posting the checkout form and saving the order 
        if request.method == "POST":
            order_form = OrderForm(request.POST)
            payment_form = MakePaymentForm(request.POST)

            if order_form.is_valid and payment_form.is_valid():
                order = order_form.save(commit=False)
                order.date = timezone.now()
                order.user = user
                order.save()
                
                # Saving the product details to the order
                total += upvote_quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=upvote_quantity
                )
                order_line_item.save()
            
                try:
                    customer = stripe.Charge.create(
                        amount=int(total * 100),
                        currency="EUR",
                        description=request.user.email,
                        card=payment_form.cleaned_data['stripe_id'],
                    )
                except stripe.error.CardError:
                    messages.error(request, "Your card has been declined")

                if customer.paid:

                    # Will increase the like count for that feature once payment has
                    # been completed 
                    if user not in feature.likes.all():
                        feature.likes.add(user)
                        

                    return redirect(reverse('invoice'))
                else:
                    messages.error(request, "Sorry, we have not been able to take your payment")

            else:
                print(payment_form.errors)
                messages.error(request, "Sorry, we were unable to process your payment with that card")
        else:
            payment_form = MakePaymentForm()
            order_form = OrderForm()

    return render(request, "upvote_checkout.html", 
                {"order_form": order_form, 
                "payment_form": payment_form, 
                "publishable": settings.STRIPE_PUBLISHABLE, 
                "product": product, 
                "total": total,
                "upvote_quantity": upvote_quantity,
                "feature": feature})

def invoice(request):
    """ Renders the invoice page """
    return render(request, 'invoice.html')
