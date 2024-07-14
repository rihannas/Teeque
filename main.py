from teequeapp.models import *
buyer1 = CustomUser.objects.create(email='buyer1@e.com', username='buyer1', phonenumber='+12345678900', country='Maldives')
buyer = Buyer.objects.create(user=buyer1)
buyer.save()

seller2 = CustomUser.objects.create(email='seller2@e.com', username='seller2', phonenumber='+12345678900', country='Portugal')
seller = Seller.objects.create(user=seller2)
seller.save()
