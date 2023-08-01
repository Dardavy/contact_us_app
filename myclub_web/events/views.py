from django.shortcuts import render
from django.core.mail import send_mail
from . models import Myuser
from django.http import FileResponse
import io
from myclub_web.settings import EMAIL_HOST_USER
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

def contact(request):

    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        telephone = request.POST['telephone']
        message = request.POST['message']
        subject = request.POST['subject']
        location = request.POST['location']

        # Create and save a Myuser instance
        contact_create = Myuser.objects.create(fullname=full_name, email=email, phone=telephone,
                                               message=message, location=location, subject=subject)
        contact_create.save()

        # create a bytestream buffer
        pdf_buffer = io.BytesIO()
        # create a canvas
        c = canvas.Canvas(pdf_buffer, pagesize=letter, bottomup=0)
        # create text object
        textob = c.beginText()
        textob.setTextOrigin(inch, inch)
        textob.setFont("Helvetica", 14)

        # Query all Myuser instances from the database
        users = Myuser.objects.all()

        # create blank list 
        lines = []
        for user in users:
            lines.append(user.fullname)
            lines.append(user.email)
            lines.append(user.phone)
            lines.append(user.message)
            lines.append(user.subject)
            lines.append(user.location)
            lines.append("===========================")

        # Loop and add some space between lines
        for line in lines:
            textob.textLine(line)
            textob.moveCursor(0, 15)  # Add 15 units of space between each line

        # Finish Up
        c.drawText(textob)
        c.showPage()
        c.save()
        pdf_buffer.seek(0)

        # Send an email
        send_mail(
            f"Contact Information - {subject}",  # Subject with descriptive text
            f"Name: {full_name}\nEmail: {email}\nTelephone: {telephone}\n\nMessage: {message}",  # Message
            EMAIL_HOST_USER,  # From Email
            [email],  # To Email (Use the 'email' variable instead of the string 'email')
            fail_silently=False,
        )

        return FileResponse(pdf_buffer, email, as_attachment=True, filename="contact.pdf")
    else:
        return render(request, 'contact.html',{})
    


    
        # return render(request, 'contact.html', {'full_name': full_name})
        













# from django.shortcuts import render
# from django.core.mail import send_mail
# from .models import Myuser
# from django.http import FileResponse
# import io
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter
# from myclub_web.settings import EMAIL_HOST_USER

# def create_contact_pdf(users):
#     # Create a bytestream buffer
#     buf = io.BytesIO()
#     # Create a canvas
#     c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
#     # Create text object
#     textob = c.beginText()
#     textob.setTextOrigin(inch, inch)
#     textob.setFont("Helvetica", 14)

#     # Loop through users and add information to the PDF
#     for user in users:
#         textob.textLine(user.fullname)
#         textob.textLine(user.email)
#         textob.textLine(user.phone)
#         textob.textLine(user.message)
#         textob.textLine(user.subject)
#         textob.textLine(user.location)
#         textob.textLine("===========================")
#         textob.moveCursor(0, 15)  # Add 15 units of space between each line

#     # Finish Up
#     c.drawText(textob)
#     c.showPage()
#     c.save()
#     buf.seek(0)

#     return buf

# def contact(request):
#     if request.method == "POST":
#         full_name = request.POST['full_name']
#         email = request.POST['email']
#         telephone = request.POST['telephone']
#         message = request.POST['message']
#         subject = request.POST['subject']
#         location = request.POST['location']

#         # Create and save a Myuser instance
#         contact_create = Myuser.objects.create(fullname=full_name, email=email, phone=telephone,
#                                                message=message, location=location, subject=subject)

#         # Send an email
#         send_mail(
#             f"Contact Information - {subject}",  # Subject with descriptive text
#             f"Name: {full_name}\nEmail: {email}\nTelephone: {telephone}\n\nMessage: {message}",  # Message
#             EMAIL_HOST_USER,  # From Email
#             ['dardavy.26@gmail.com'],  # To Email
#             fail_silently=False,
#         )

#         # Generate the PDF with all Myuser instances and return it as an attachment
#         users = Myuser.objects.all()
#         pdf_buffer = create_contact_pdf(users)
#         return FileResponse(pdf_buffer, as_attachment=True, filename="contact.pdf")
#     else:
#         return render(request, 'contact.html', {})




