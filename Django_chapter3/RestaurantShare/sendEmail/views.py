from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from shareRes.models import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Create your views here.
def sendEmail(request):
    checked_res_list = request.POST.getlist('checks')
    inputReceiver = request.POST['inputReceiver']
    inputTitle = request.POST['inputTitle']
    inputContent = request.POST['inputContent']

    mail_html = "<html><body>"
    mail_html += "<h1> 맛집 공유 </h1>"
    mail_html += "<p>" + inputContent + "<br>"
    mail_html += "발신자가 공유한 맛집입니다.</p>"

    for checked_res_id in checked_res_list:
        restaurant = Restaurant.objects.get(id=checked_res_id)
        mail_html += "<h2>" + restaurant.restaurant_name + "</h2>"
        mail_html += "<h4>* 관련 링크</h4>" + "<p>" + restaurant.restaurant_link + "</p><br>"
        mail_html += "<h4>* 관련 키워드</h4>" + "<p>" + restaurant.restaurant_keyword + "</p><br>"
        mail_html += "<br>"
        mail_html += "</body></html>"

    print(mail_html)
    # print(checked_res_list, inputReceiver, inputTitle, inputContent, sep=" / ")
    return HttpResponseRedirect(reverse('index'))
