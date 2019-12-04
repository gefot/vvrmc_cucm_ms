import sys

# This is needed so as to run on CLI
sys.path.append('/home/gfot/vvrmc_cucm_ms')

import datetime
import json

from modules import module_cdr_funcs
from modules import module_general_funcs
from modules import cdr_classes

ACCESS = json.load(open('/home/gfot/vvrmc_cucm_ms/data/security/access.json'))

# end_date = "20190913000000"
end_date = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
start_date = (datetime.datetime.today() - datetime.timedelta(minutes=5)).strftime('%Y%m%d%H%M%S')

start_timestamp = module_general_funcs.date_to_timestamp(start_date)
end_timestamp = module_general_funcs.date_to_timestamp(end_date)

# print(start_date)
# print(end_date)
print(start_timestamp)
print(end_timestamp)

cdr_records = module_cdr_funcs.get_cdr(start_timestamp, end_timestamp, "*", "911")
for cdr_record in cdr_records:
    extension = cdr_record[4]
    date = module_general_funcs.timestamp_to_date(int(cdr_record[3]))
    print(cdr_record)

    body = "Extension <b>{}</b> <u>dialed 911</u> at {}".format(extension, date)
    print(body)

    # Send E-mail
    subject = "911 Report"
    attachments = []
    USERNAME = str(ACCESS["o365"]["username"])
    PASSWORD = str(ACCESS["o365"]["password"])
    MAIL_SERVER = str(ACCESS["o365"]["mail_server"])
    # toaddr = ["val.king@whitehatvirtual.com", "Albert.Lattimer@vvrmc.org", \
    #           "Brittany.Harle@vvrmc.org", "malachi.fisher@vvrmc.org", "georgios.fotiadis@whitehatvirtual.com"]
    toaddr = ["georgios.fotiadis@whitehatvirtual.com"]
    module_general_funcs.send_mail(USERNAME, PASSWORD, MAIL_SERVER, toaddr, subject, body, attachments, False, False)

