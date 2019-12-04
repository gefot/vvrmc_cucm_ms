import datetime
import time
import os

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


###########################################################################################################################################
def timestamp_to_date(my_timestamp):
    return datetime.datetime.fromtimestamp(my_timestamp)


###########################################################################################################################################
def date_to_timestamp(my_date):
    return time.mktime(datetime.datetime.strptime(my_date, "%Y%m%d%H%M%S").timetuple())


###########################################################################################################################################
def weekday_from_timestamp(my_timestamp):
    return datetime.datetime.fromtimestamp(my_timestamp).strftime('%a')


###########################################################################################################################################
def hour_from_timestamp(my_timestamp):
    return datetime.datetime.fromtimestamp(my_timestamp).strftime('%H')


###########################################################################################################################################
def day_timestamp_range_from_date(my_date):
    dt = datetime.datetime.strptime(my_date, '%Y%m%d%H%M%S')

    my_start = dt.replace(hour=0, minute=0, second=1).strftime('%Y%m%d%H%M%S')
    my_end = dt.replace(hour=23, minute=59, second=59).strftime('%Y%m%d%H%M%S')
    print("inside day_timestamp_range_from_date: ", my_start, my_end)
    day_range = [date_to_timestamp(my_start), date_to_timestamp(my_end)]

    return day_range


###########################################################################################################################################
def week_timestamp_range_from_date(my_date):
    dt = datetime.datetime.strptime(my_date, '%Y%m%d%H%M%S')

    start = dt - datetime.timedelta(days=dt.weekday())
    end = start + datetime.timedelta(days=6)

    my_start = start.replace(hour=0, minute=0, second=1).strftime('%Y%m%d%H%M%S')
    my_end = end.replace(hour=23, minute=59, second=59).strftime('%Y%m%d%H%M%S')
    print("inside week_timestamp_range_from_date: ", my_start, my_end)
    week_range = [date_to_timestamp(my_start), date_to_timestamp(my_end)]

    return week_range


###########################################################################################################################################
def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)


###########################################################################################################################################
def month_timestamp_range_from_date(my_date):
    dt = datetime.datetime.strptime(my_date, '%Y%m%d%H%M%S')

    last_day = last_day_of_month(dt)
    my_start = dt.replace(day=1, hour=0, minute=0, second=1).strftime('%Y%m%d%H%M%S')
    my_end = dt.replace(day=int(last_day.strftime('%d')), hour=23, minute=59, second=59).strftime('%Y%m%d%H%M%S')
    print("inside week_timestamp_range_from_date: ", my_start, my_end)
    month_range = [date_to_timestamp(my_start), date_to_timestamp(my_end)]

    return month_range


###########################################################################################################################################
def send_mail(username, password, mail_server, toaddr, subject, body, attachments, login, tls):
    fromaddr = username
    # text = "This will be sent as text"

    msg = MIMEMultipart()
    msg['To'] = ", ".join(toaddr)
    msg['From'] = fromaddr
    msg['Subject'] = subject

    ### Attach e-mail body
    # part1 = MIMEText(text, 'plain')
    part1 = MIMEText(body, 'html')
    msg.attach(part1)

    ### Attach e-mail attachments
    for attachment in attachments:
        # my_attachment = open(attachment, "rb")
        # file_name = os.path.basename(attachment)
        part2 = MIMEBase('application', 'octet-stream')
        part2.set_payload(open(attachment, "rb").read())
        part2.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment))
        encoders.encode_base64(part2)
        msg.attach(part2)
        # part2.set_payload(open(attachment, "rb").read())
        # print(attachment)
        # part2.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attachment))
        # encoders.encode_base64(part2)
        # msg.attach(part2)
        # print(part2)

    mailserver = smtplib.SMTP(mail_server)
    # mailserver.ehlo()
    if tls:
        mailserver.starttls()
    # mailserver.ehlo()
    if login:
        mailserver.login(username, password)
    mailserver.sendmail(fromaddr, toaddr, msg.as_string())
    mailserver.quit()


###########################################################################################################################################

