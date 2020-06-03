from django.urls import path

from . import views

app_name = "invoicemanager"
urlpatterns = [

	# # # DEFAULT

	path('', views.invoices.index, name='index'),

    # # # INVOICES

    path('invoice/new/', views.invoices.new_invoice, name='new_invoice'),
    path('invoice/all/', views.invoices.all_invoices, name='all_invoices'),
    path('invoice/draft/', views.invoices.draft_invoices, name='draft_invoices'),
    path('invoice/paid/', views.invoices.paid_invoices, name='paid_invoices'),
    path('invoice/unpaid/', views.invoices.unpaid_invoices, name='unpaid_invoices'),
    path('invoice/<int:invoice_id>/', views.invoices.invoice, name='invoice'),
    path('invoice/search/', views.invoices.search_invoice, name='search_invoice'),
    path('invoice/<int:invoice_id>/update/', views.invoices.update_invoice, name='update_invoice'),
    path('invoice/<int:invoice_id>/print/', views.invoices.print_invoice, name='print_invoice'),
    path('invoice/<int:invoice_id>/delete/', views.invoices.delete_invoice, name='delete_invoice'),

    # # # ITEMS

    path('invoice/<int:invoice_id>/item/add/', views.items.add_item, name='add_item'),
    path('invoice/<int:invoice_id>/item/<int:invoiceitem_id>/delete/', views.items.delete_item, name='delete_item'),

    # # # REPORTS

    path('accounting/', views.reports.accounting, name='accounting'),

    # # # CUSTOMERS

    path('customers/', views.customers.customer_list, name='customer_list'),
    path('customer/<int:customer_id>/', views.customers.customer, name='customer'),
	path('customer/<int:customer_id>/update/', views.customers.update_customer, name='update_customer'),
    path('customer/<int:customer_id>/delete/', views.customers.delete_customer, name='delete_customer'),
    path('customer/new/', views.customers.new_customer, name='new_customer'),

    # # # USER AUTHENTICATION

    path('login/', views.userauth.login_view, name='login'),
    path('logout/', views.userauth.logout_view, name='logout'),

    # # # ADMIN

    path('users/', views.admin.users, name='users'),
    path('settings/', views.admin.settings, name='settings'),
]
