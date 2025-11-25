from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [


    path('adminhome/', views.adminhome),

    path('login/', views.login_get),
    path('login_post/', views.login_post),

    path('logout/', views.logout),

    path('view_user/', views.view_user),
    path('view_user_Post/', views.view_user_Post),


    path('admin_view_Book/<userid>', views.admin_view_Book),
    path('Book_post/', views.Book_post),


    path('All_Book/', views.All_Book),


    path('view_complaint/', views.view_complaint),
    path('complaint_post/', views.complaint_post),


    path('Admin_Change_Password/', views.Admin_Change_Password),
    path('Admin_Change_Password_POST/', views.Admin_Change_Password_POST),


    path('Send_notification/', views.Send_notification),
    path('Send_notification_POST/', views.Send_notification_POST),
    path('delete_notification/<id>', views.delete_notification),

    path('reply_complaints/<id>', views.reply_complaints),
    path('reply_complaints_POST/', views.reply_complaints_POST),


    path('View_notification/', views.View_notification),
    path('View_notification_POST/', views.View_notification_POST),

    path('view_payments/',views.view_payments),

    #================User============================

    path('userhome/', views.userhome),


    path('registeration/', views.registeration),
    path('registeration_post/', views.registeration_post),

    path('User_Change_Password/', views.User_Change_Password),
    path('User_Change_Password_post/', views.User_Change_Password_post),

    path('View_Profile/', views.View_Profile),

    path('Update_Profile/', views.Update_Profile),
    path('Update_Profile_post/', views.Update_Profile_post),

    path('List_Book/', views.List_Book),
    path('List_Book_post/', views.List_Book_post),

    path('View_Book/', views.View_Book),
    path('View_Book_post/', views.View_Book_post),

    path('Other_Book/', views.Other_Book),
    path('Other_Book_post/', views.Other_Book_post),

    path('Update_Book/<id>', views.Update_Book),
    path('Update_Book_post/', views.Update_Book_post),

    path('Delete_Book/<id>', views.Delete_Book),

    path('View_User_Request/<bid>', views.View_User_Request),
    path('View_User_Request_post/', views.View_User_Request_post),

    path('Accept_Request/<id>/<bid>', views.Accept_Request),

    path('Reject_Request/<id>', views.Reject_Request),

    path('Request_Book/<bid>', views.Request_Book),

    path('View_Request_Status/', views.View_Request_Status),
    path('View_Request_Status_post/', views.View_Request_Status_post),

    path('Review/<bid>', views.Review),
    path('Review_post/', views.Review_post),

    path('View_Review/<bid>', views.View_Review),
    path('View_Review_post/', views.View_Review_post),

    path('User_Complaint/', views.User_Complaint),
    path('User_Complaint_post/', views.User_Complaint_post),

    path('View_reply/', views.View_reply),
    path('View_reply_post/', views.View_reply_post),

    path('UserView_notification/', views.UserView_notification),
    path('UserView_notification_post/', views.UserView_notification_post),

    path('View_Exchange_History/', views.View_Exchange_History),
    path('View_Exchange_History_post/', views.View_Exchange_History_post),

    path('View_Point/', views.View_Point),
    # path('View_Point_post/', views.View_Point_post),

    path('chat1/<id>', views.chat1),
    path('chat_view/', views.chat_view),
    path('chat_send/<msg>', views.chat_send),




    path('grpchat1/', views.grpchat1),
    path('grpchat_view/', views.grpchat_view),
    path('grpchat_send/<msg>', views.grpchat_send),

    path('raz_pay/', views.raz_pay),
]
