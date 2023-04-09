from django import template
register = template.Library()

@register.filter(name='paymentMode')
def paymentMode(Request, num):
    if(num==0):
        return "COD"
    else:
        return "Net Banking"


@register.filter(name='paymentStatus')
def paymentStatus(Request, num):
    if(num==0):
        return "Pending"
    else:
        return "Done"

@register.filter(name='orderStatus')
def orderStatus(Request, num):
    if(num==0):
        return "Order Placed"
    elif(num==1):
        return "Ready To Pack"
    elif(num==2):
        return "Packed"
    elif(num==3):
        return "Ready to Ship"
    elif(num==4):
        return "Shippied"
    elif(num==5):
        return "Order in Transit"
    elif(num==6):
        return "Product Reached at Final Delivery Station"
    elif(num==7):
        return "Out for Delivery"
    else:
        return "Delivered"