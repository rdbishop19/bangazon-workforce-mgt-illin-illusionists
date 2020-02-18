from django.urls import path
from django.conf.urls import include
# from hrapp import views
from .views import *

app_name = 'hrapp'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employee_list'),
    path('employees/<int:employee_id>/form', employee_edit_form, name='employee_edit_form'),
    path('computers/', computer_list, name='computer_list'),
    path('trainingprograms/', training_program_list, name='training_list'),
    path('trainingprograms/<int:program_id>', training_details, name='training'),
    path('trainingprograms/form', training_program_form, name='training_form'),
    path('computers/<int:computer_id>', computer_details, name="computer"),
    path('computer/form', computer_form, name = "computer_form"),
    path('employees/<int:employee_id>', employee_details, name="employee"),
    path('employees/form', employee_form, name="employee_form"),
    path('departments/', department_list, name='department_list'), 
    path('departments/<int:department_id>/', department_details, name='department'),
    path('departments/form', department_form, name="department_form")
]
