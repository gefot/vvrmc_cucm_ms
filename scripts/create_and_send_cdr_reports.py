
import datetime
import json
import sys

sys.path.append('/home/gfot/cucm-cdr-analyzer')

from modules import module_funcs
from modules import classes


access = json.load(open('/home/gfot/cucm-cdr-analyzer/data/security/access.json'))
if len(sys.argv) == 2:
    REPORT_TYPE = sys.argv[1]
else:
    REPORT_TYPE = "monthly"
SEND_EMAILS = False

OUTPUT_PATH = '/home/gfot/cucm-cdr-analyzer/data/output/'
DEPARTMENTS = {'Main_Hospital': '1001', '1801_Clinic': '5810', 'Specialty_Clinic': '5850'}
EXTENSIONS = {'Orthopediatric_Clinic': '7002', 'Urology_Clinic': '1733'}
HUNTPILOTS = {'IT_Helpdesk': '3333'}

# date = "20190913000000"
date = datetime.datetime.today().strftime('%Y%m%d%H%M%S')

if REPORT_TYPE == "daily":
    day_timestamp_range = module_funcs.day_timestamp_range_from_date(date)
    start_timestamp = day_timestamp_range[0]
    end_timestamp = day_timestamp_range[1]

elif REPORT_TYPE == "weekly":
    week_timestamp_range = module_funcs.week_timestamp_range_from_date(date)
    week_number = datetime.datetime.strptime(date, '%Y%m%d%H%M%S').strftime("%V")
    start_timestamp = week_timestamp_range[0]
    end_timestamp = week_timestamp_range[1]
    start_date = module_funcs.timestamp_to_date(start_timestamp).strftime('%Y_%m_%d')
    end_date = module_funcs.timestamp_to_date(end_timestamp).strftime('%Y_%m_%d')

elif REPORT_TYPE == "monthly":
    month_timestamp_range = module_funcs.month_timestamp_range_from_date(date)
    month_name = datetime.datetime.strptime(date, '%Y%m%d%H%M%S').strftime("%B")
    year = datetime.datetime.strptime(date, '%Y%m%d%H%M%S').strftime("%Y")
    start_timestamp = month_timestamp_range[0]
    end_timestamp = month_timestamp_range[1]

################
## CALL TREES ##
################
for department, extension in DEPARTMENTS.items():
    print("\n\n\n----->{}".format(department))
    cdr_records = module_funcs.get_cdr_by_called_number(start_timestamp, end_timestamp, extension)
    callTreeStats = classes.CallTreeStats(extension, department)
    module_funcs.count_calls_by_call_tree(callTreeStats, cdr_records)
    callTreeStats.populate_percentages()

    if REPORT_TYPE == "daily":
        callTreeStats.full_filename = OUTPUT_PATH + "Daily_Report_" + datetime.datetime.strptime(date, '%Y%m%d%H%M%S').strftime('%Y_%m_%d') + "_" + department + ".csv"
        callTreeStats.email_subject = "{}: Daily Call Report for {}".format(datetime.datetime.strptime(date, '%Y%m%d%H%M%S').strftime('%Y_%m_%d'), department)
    elif REPORT_TYPE == "weekly":
        callTreeStats.full_filename = "{}Weekly_Report_Week_{}__{}-{}__{}.csv".format(
            OUTPUT_PATH, week_number, start_date, end_date, department)
        callTreeStats.email_subject = "{}: Weekly Call Report (Week {} - {}-{} ) for {}".format(
            datetime.datetime.strptime(date, '%Y%m%d%H%M%S').strftime('%Y_%m_%d'), week_number, start_date, end_date, department)
    elif REPORT_TYPE == "monthly":
        callTreeStats.full_filename = "{}Monthly_Report_{}_{}.csv".format(
            OUTPUT_PATH, year, month_name, department)
        callTreeStats.email_subject = "{}: Monthly Call Report ({}_{}) for {}".format(
            datetime.datetime.strptime(date, '%Y%m%d%H%M%S').strftime('%Y_%m_%d'), year, month_name, department)

    callTreeStats.create_csv_file()
    callTreeStats.create_html_content()
    print(callTreeStats.full_filename)
    print(callTreeStats.email_subject)
    print(callTreeStats.html_content)
    print(callTreeStats)

################
## EXTENSIONS ##
################
for department, extension in EXTENSIONS.items():
    print("\n\n\n----->{}".format(department))
    cdr_records = module_funcs.get_cdr_by_called_number(start_timestamp, end_timestamp, extension)
    extensionStats = classes.ExtensionStats(extension, department)
    module_funcs.count_calls_by_extension(extensionStats, cdr_records)
    extensionStats.populate_percentages()

    if REPORT_TYPE == "daily":
        extensionStats.full_filename = OUTPUT_PATH + "Daily_Report_" + datetime.datetime.strptime(date, '%Y%m%d%H%M%S').strftime('%Y_%m_%d') + "_" + department + ".csv"
        extensionStats.email_subject = "{}: Daily Call Report for {}".format(datetime.datetime.strptime(date, '%Y%m%d%H%M%S').strftime('%Y_%m_%d'), department)
    elif REPORT_TYPE == "weekly":
        extensionStats.full_filename = "{}Weekly_Report_Week_{}__{}-{}__{}.csv".format(
            OUTPUT_PATH, week_number, start_date, end_date, department)
        extensionStats.email_subject = "{}: Weekly Call Report (Week {} - {}-{} ) for {}".format(
            datetime.datetime.strptime(date, '%Y%m%d%H%M%S').strftime('%Y_%m_%d'), week_number, start_date, end_date, department)
    elif REPORT_TYPE == "monthly":
        extensionStats.full_filename = "{}Monthly_Report_{}_{}.csv".format(
            OUTPUT_PATH, year, month_name, department)
        extensionStats.email_subject = "{}: Monthly Call Report ({}_{}) for {}".format(
            datetime.datetime.strptime(date, '%Y%m%d%H%M%S').strftime('%Y_%m_%d'), year, month_name, department)

    extensionStats.create_csv_file()
    extensionStats.create_html_content()
    print(extensionStats.full_filename)
    print(extensionStats.email_subject)
    print(extensionStats.html_content)
    print(extensionStats)


#################
## Hunt Pilots ##
#################
print("\n\n\n----->IT Helpdesk")
for department, extension in HUNTPILOTS.items():
    cdr_records = module_funcs.get_cdr_by_called_number(start_timestamp, end_timestamp, extension)
    huntpilotStats = classes.HuntPilotStats(extension, department)
    module_funcs.count_calls_by_hunt_pilot(huntpilotStats, cdr_records)
    huntpilotStats.populate_percentages()

    if REPORT_TYPE == "daily":
        huntpilotStats.full_filename = OUTPUT_PATH + "Daily_Report_" + datetime.datetime.strptime(date, '%Y%m%d%H%M%S').strftime('%Y_%m_%d') + "_" + department + ".csv"
        huntpilotStats.email_subject = "{}: Daily Call Report for {}".format(datetime.datetime.strptime(date, '%Y%m%d%H%M%S').strftime('%Y_%m_%d'), department)
    elif REPORT_TYPE == "weekly":
        huntpilotStats.full_filename = "{}Weekly_Report_Week_{}__{}-{}__{}.csv".format(
            OUTPUT_PATH, week_number, start_date, end_date, department)
        huntpilotStats.email_subject = "{}: Weekly Call Report (Week {} - {}-{} ) for {}".format(
            datetime.datetime.strptime(date, '%Y%m%d%H%M%S').strftime('%Y_%m_%d'), week_number, start_date, end_date, department)
    elif REPORT_TYPE == "monthly":
        huntpilotStats.full_filename = "{}Monthly_Report_{}_{}.csv".format(
            OUTPUT_PATH, year, month_name, department)
        huntpilotStats.email_subject = "{}: Monthly Call Report ({}_{}) for {}".format(
            datetime.datetime.strptime(date, '%Y%m%d%H%M%S').strftime('%Y_%m_%d'), year, month_name, department)

    huntpilotStats.create_csv_file()
    huntpilotStats.create_html_content()
    print(huntpilotStats.full_filename)
    print(huntpilotStats.email_subject)
    print(huntpilotStats.html_content)
    print(huntpilotStats)



###############
# Send Emails #
###############
if SEND_EMAILS:
    for department, extension in DEPARTMENTS.items():
        USERNAME = str(access["o365"]["username"])
        PASSWORD = str(access["o365"]["password"])
        MAIL_SERVER = str(access["o365"]["mail_server"])
        # toaddr = ["abhijit.dhar@whitehatvirtual.com", "val.king@whitehatvirtual.com", \
        #           "dgalma01@vvrmc.org", "maricela.sandoval@amistadmp.org", "melanie.torres@vvrmc.org", \
        #           "Albert.Lattimer@vvrmc.org", "letty.ortiz@vvrmc.org",
        #           "georgios.fotiadis@whitehatvirtual.com"]
        toaddr = ["georgios.fotiadis@whitehatvirtual.com"]
        # toaddr = ["georgios.fotiadis@whitehatvirtual.com", "Maricela.Sandoval@vvrmc.org"]
        module_funcs.send_mail(USERNAME, PASSWORD, MAIL_SERVER, toaddr, callTreeStats.email_subject, callTreeStats.html_content, [callTreeStats.full_filename], False, False)

    for department, extension in EXTENSIONS.items():
        USERNAME = str(access["o365"]["username"])
        PASSWORD = str(access["o365"]["password"])
        MAIL_SERVER = str(access["o365"]["mail_server"])
        # toaddr = ["abhijit.dhar@whitehatvirtual.com", "val.king@whitehatvirtual.com", \
        #           "dgalma01@vvrmc.org", "maricela.sandoval@amistadmp.org", "melanie.torres@vvrmc.org", \
        #           "Albert.Lattimer@vvrmc.org", "letty.ortiz@vvrmc.org",
        #           "georgios.fotiadis@whitehatvirtual.com"]
        # toaddr = ["georgios.fotiadis@whitehatvirtual.com", "Maricela.Sandoval@vvrmc.org"]
        toaddr = ["georgios.fotiadis@whitehatvirtual.com"]
        module_funcs.send_mail(USERNAME, PASSWORD, MAIL_SERVER, toaddr, extensionStats.email_subject, extensionStats.html_content, [extensionStats.full_filename], False, False)

    for department, extension in HUNTPILOTS.items():
        USERNAME = str(access["o365"]["username"])
        PASSWORD = str(access["o365"]["password"])
        MAIL_SERVER = str(access["o365"]["mail_server"])
        toaddr = ["georgios.fotiadis@whitehatvirtual.com"]
        # toaddr = ["val.king@whitehatvirtual.com", "georgios.fotiadis@whitehatvirtual.com"]
        module_funcs.send_mail(USERNAME, PASSWORD, MAIL_SERVER, toaddr, huntpilotStats.email_subject, huntpilotStats.html_content, [huntpilotStats.full_filename], False, False)

