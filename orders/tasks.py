from celery import shared_task  # функция декоратор
from django.core.mail import send_mail  # функция для отправки сообщений
from .models import Order  # импортируем класс для работы
from io import BytesIO
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings




# @shared_task
# def order_created(order_id):
#     """
#     Задание по отправке уведомления по электронной почте при
#     успешном заказе
#     :param order_id: номер заказа
#     :return: письмо для рассылки
#     """
#
#     order = Order.objects.get(id=order_id)  # получаем номер заказа
#     subject = f'Order nr. {order_id}'
#     message = f'Dear {order.first_name},\n\n' \
#               f'You have successfully placed an order.' \
#               f'Your order ID is {order_id}.'
#     mail_sent = send_mail(subject,  # что отсылаем
#                           message,
#                           'admin@myshop.com',  # c какой почты
#                           [order.email])  # на какую почту
#
#     return mail_sent
#

@shared_task
def payment_completed(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully paid.
    """
    order = Order.objects.get(id=order_id)
    # create invoice e-mail
    subject = f'My Shop - Invoice no. {order.id}'
    message = 'Please, find attached the invoice for your recent purchase.'
    email = EmailMessage(subject,
                         message,
                         'admin@myshop.com',
                         [order.email])
    # generate PDF
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets=[weasyprint.CSS(settings.STATIC_ROOT / 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out,
                                          stylesheets=stylesheets)
    # attach PDF file
    email.attach(f'order_{order.id}.pdf',
                 out.getvalue(),
                 'application/pdf')
    # send e-mail
    email.send()