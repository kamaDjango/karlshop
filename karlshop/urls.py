from django.contrib import admin
from django.conf import settings
from django.urls import path

from django.conf.urls.static import static
from mainApp import views as mainApp
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainApp.homePage),
    path('shop/<str:mc>/<str:sc>/<str:br>/',mainApp.shopPage),
    path('price-filter/',mainApp.priceFilterPage),
    path('single-product/<int:num>/',mainApp.singleProductPage),
    path('cart/',mainApp.cartPage),
    path('checkout/',mainApp.checkoutPage),
    path('search/',mainApp.searchPage),
    path('login/',mainApp.loginPage),
    path('logout/',mainApp.logoutPage),
    path('signup/',mainApp.signupPage),
    path('profile/',mainApp.profilePage),
    path('update-profile/',mainApp.updateProfilePage),
    path('add-to-cart/',mainApp.addToCartPage),
    path('delete-cart/<str:num>/',mainApp.deleteFromCartPage),
    path('update-cart/<str:num>/<str:op>/',mainApp.updateCartPage),
    path('placeorder/',mainApp.placeOrderPage),
    path('confirmation/',mainApp.confirmationPage),
    path('add-to-wishlist/<int:num>/',mainApp.addToWishlistPage),
    path('remove-from-wishlist/<int:num>/',mainApp.removeFromWishlistPage),
    path('contact/',mainApp.contactUsPage),
    path('forget-password1/',mainApp.forgetPasswordPage1),
    path('forget-password2/',mainApp.forgetPasswordPage2),
    path('forget-password3/',mainApp.forgetPasswordPage3),
    path('paymentSuccess/<str:rppid>/<str:rpoid>/<str:rpsid>/',mainApp.paymentSuccess),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
