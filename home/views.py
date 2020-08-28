from django.shortcuts import render,reverse
from django.core import mail
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    if request.method == 'POST':
        full_name = request.POST.get('ContactFullName')
        to_ = request.POST.get('ContactEmail')
        number = request.POST.get('ContactNumber')
        company = request.POST.get('ContactCompanyName')
        desc = request.POST.get('ContactDescription')
        body = f"<table width='600' border='0' cellpadding='3' cellspacing='3'>\
    				  <tr>\
    					<td colspan='2' align='left'><font face='Arial, Helvetica, sans-serif' size='4'><strong>Appointment request from  {full_name}</strong></font></td>\
    				  </tr>\
    				  <tr>\
    					<td colspan='2' align='center'><table width='600' cellpadding='3' cellspacing='3' border='0'>\
    						<tr>\
    						  <td><table width='100%' cellspacing='0' cellpadding='12' border='1' bordercolor='#919191'>\
    							  <tr>\
    								<td width='32%' align='right'><font face='Arial, Helvetica, sans-serif' size='4'>Name :</font></td>\
    								<td width='68%' align='left'><font face='Arial, Helvetica, sans-serif' size='4'>{full_name}</font></td>\
    							  </tr>\
    							  <tr>\
    								<td align='right'><font face='Arial, Helvetica, sans-serif' size='4'>Email :</font></td>\
    								<td align='left'><font face='Arial, Helvetica, sans-serif' size='4'>{to_}</font></td>\
    							  </tr>\
    							  <tr>\
    								<td align='right'><font face='Arial, Helvetica, sans-serif' size='4'>Contact  :</font></td>\
    								<td align='left'><font face='Arial, Helvetica, sans-serif' size='4'>{number}</font></td>\
    							  </tr>\
    							  <tr>\
    								<td align='right'><font face='Arial, Helvetica, sans-serif' size='4'>Company Name  :</font></td>\
    								<td align='right'><font face='Arial, Helvetica, sans-serif' size='4'>{company}</font></td>\
    							  </tr>\
    							  <tr>\
    								<td align='right' valign='top'><font face='Arial, Helvetica, sans-serif' size='4'>Description :</font></td>\
    								<td align='left'><font face='Arial, Helvetica, sans-serif' size='4'>{desc}</font></td>\
    								</tr>\
    							  </table></td>\
    						</tr>\
    					  </table></td>\
    				  </tr>\
    				</table>"
        try:
            mail.send_mail(f'Contact From {full_name}', strip_tags(body), settings.DEFAULT_FROM_EMAIL , [to_], html_message=body)
            messages.success(request, 'Success! Your message has been sent to us.')
            return HttpResponseRedirect(f'{reverse("home")}#ContactSuccessMessage')
        except:
            messages.error(request, 'Error! There was an error sending your message.')
            return HttpResponseRedirect(f'{reverse("home")}#ContactErrorMessage')


    return render(request, 'home.html')

def book_app(request):
    if request.method == 'POST':
        AppointmentFullName = request.POST.get('AppointmentFullName')
        AppointmentEmail = request.POST.get('AppointmentEmail')
        AppointmentContactNumber = request.POST.get('AppointmentContactNumber')
        AppointmentDate = request.POST.get('AppointmentDate')
        AppointmentMobileDate = request.POST.get('AppointmentMobileDate')
        AppointmentTime = request.POST.get('AppointmentTime')
        AppointmentMessage = request.POST.get('AppointmentMessage')
        if AppointmentDate =='':
            AppointmentDate = AppointmentMobileDate
        table = f"<table width='600' border='0' cellpadding='3' cellspacing='3'>\
    				  <tr>\
    					<td colspan='2' align='left'><font face='Arial, Helvetica, sans-serif' size='4'><strong>Appointment request from  {AppointmentFullName}</strong></font></td>\
    				  </tr>\
    				  <tr>\
    					<td colspan='2' align='center'><table width='600' cellpadding='3' cellspacing='3' border='0'>\
    						<tr>\
    						  <td><table width='100%' cellspacing='0' cellpadding='12' border='1' bordercolor='#919191'>\
    							  <tr>\
    								<td width='32%' align='right'><font face='Arial, Helvetica, sans-serif' size='4'>Name :</font></td>\
    								<td width='68%' align='left'><font face='Arial, Helvetica, sans-serif' size='4'>{AppointmentFullName}</font></td>\
    							  </tr>\
    							  <tr>\
    								<td align='right'><font face='Arial, Helvetica, sans-serif' size='4'>Email :</font></td>\
    								<td align='left'><font face='Arial, Helvetica, sans-serif' size='4'>{AppointmentEmail}</font></td>\
    							  </tr>\
    							  <tr>\
    								<td align='right'><font face='Arial, Helvetica, sans-serif' size='4'>Contact  :</font></td>\
    								<td align='left'><font face='Arial, Helvetica, sans-serif' size='4'>{AppointmentContactNumber}</font></td>\
    							  </tr>\
    							  <tr>\
    								<td align='right'><font face='Arial, Helvetica, sans-serif' size='4'>Appointment Date  :</font></td>\
    								<td align='left'><font face='Arial, Helvetica, sans-serif' size='4'>{AppointmentDate}</font></td>\
    							  </tr>\
    							  <tr>\
    								<td align='right' valign='top'><font face='Arial, Helvetica, sans-serif' size='4'>Appointment Time :</font></td>\
    								<td align='left'><font face='Arial, Helvetica, sans-serif' size='4'>{AppointmentTime}</font></td>\
    							  </tr>\
    							  <tr>\
    								<td align='right' valign='top'><font face='Arial, Helvetica, sans-serif' size='4'>Message:</font></td>\
    								<td align='left'><font face='Arial, Helvetica, sans-serif' size='4'>{AppointmentMessage}</font></td>\
    							</tr>\
    							  </table></td>\
    						</tr>\
    					  </table></td>\
    				  </tr>\
    				</table>"
        try:
            mail.send_mail(f'Contact From {AppointmentFullName}', strip_tags(table), settings.DEFAULT_FROM_EMAIL , [to_], html_message=table)
            messages.success(request, 'Success! Your message has been sent to us.')
            return HttpResponseRedirect(f'{reverse("home")}#SuccessMessage')
        except:
            messages.error(request, 'Error! There was an error sending your message.')
            return HttpResponseRedirect(f'{reverse("home")}#ErrorMessage')
