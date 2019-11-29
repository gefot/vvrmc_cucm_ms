class CallTreeStats:
    def __init__(self, extension, department):
        self.extension = extension
        self.department = department
        self.full_filename = "unknown"
        self.email_subject = "unknown"
        self.html_content = "unknown"

        self.total = 0
        self.total_perDay = [0 for i in range(32)]
        self.total_perHour = [0 for i in range(24)]

        self.answered_1stLevel = 0
        self.answered_1stLevel_percent = 0
        self.answered_1stLevel_perDay = [0 for i in range(32)]
        self.answered_1stLevel_perDay_percent = [0 for i in range(32)]
        self.answered_1stLevel_perHour = [0 for i in range(24)]
        self.answered_1stLevel_perHour_percent = [0 for i in range(24)]

        self.missed_1stLevel = 0
        self.missed_1stLevel_percent = 0
        self.missed_1stLevel_perDay = [0 for i in range(32)]
        self.missed_1stLevel_perDay_percent = [0 for i in range(32)]
        self.missed_1stLevel_perHour = [0 for i in range(24)]
        self.missed_1stLevel_perHour_percent = [0 for i in range(24)]

        self.answered_aa = 0
        self.answered_aa_percent = 0
        self.answered_aa_perDay = [0 for i in range(32)]
        self.answered_aa_perDay_percent = [0 for i in range(32)]
        self.answered_aa_perHour = [0 for i in range(24)]
        self.answered_aa_perHour_percent = [0 for i in range(24)]

        # TODO
        self.missed_aa = 0
        self.missed_aa_perDay = [0 for i in range(32)]
        self.missed_aa_perHour = [0 for i in range(24)]

    def __str__(self):
        return "\ntotal: {}\ntotal_perDay: {}\ntotal_perHour: {}" \
               "\n\nanswered_1stLevel: {}" \
               "\nanswered_1stLevel_perDay: {}\nanswered_1stLevel_perDay_percent: {}" \
               "\nanswered_1stLevel_perHour: {}\nanswered_1stLevel_perHour_percent: {}" \
               "\n\nmissed_1stLevel: {}" \
               "\nmissed_1stLevel_perDay: {}\nmissed_1stLevel_perDay_percent: {}" \
               "\nmissed_1stLevel_perHour: {}\nmissed_1stLevel_perHour_percent: {}" \
               "\n\nanswered_aa: {}" \
               "\nanswered_aa_perDay: {}\nanswered_aa_perDay_percent: {}" \
               "\nanswered_aa_perHour: {}\nanswered_aa_perHour_percent: {}".format(
            self.total, self.total_perDay, self.total_perHour,
            self.answered_1stLevel,
            self.answered_1stLevel_perDay, self.answered_1stLevel_perDay_percent,
            self.answered_1stLevel_perHour, self.answered_1stLevel_perHour_percent,
            self.missed_1stLevel,
            self.missed_1stLevel_perDay, self.missed_1stLevel_perDay_percent,
            self.missed_1stLevel_perHour, self.missed_1stLevel_perHour_percent,
            self.answered_aa,
            self.answered_aa_perDay, self.answered_aa_perDay_percent,
            self.answered_aa_perHour, self.answered_aa_perHour_percent)

    def populate_percentages(self):

        try:
            self.answered_1stLevel_percent = str(round(float(self.answered_1stLevel) / self.total * 100, 1)) + "%"
        except:
            self.answered_1stLevel = str(0.0) + "%"
        try:
            self.missed_1stLevel_percent = str(round(float(self.missed_1stLevel) / self.total * 100, 1)) + "%"
        except:
            self.missed_1stLevel_percent = str(0.0) + "%"
        try:
            self.answered_aa_percent = str(round(float(self.answered_aa) / self.total * 100, 1)) + "%"
        except:
            self.answered_aa_percent = str(0.0) + "%"

        for i in range(32):
            try:
                self.answered_1stLevel_perDay_percent[i] = str(round(float(self.answered_1stLevel_perDay[i]) / self.total_perDay[i] * 100, 1)) + "%"
            except:
                self.answered_1stLevel_perDay_percent[i] = str(0.0) + "%"
        for i in range(32):
            try:
                self.missed_1stLevel_perDay_percent[i] = str(round(float(self.missed_1stLevel_perDay[i]) / self.total_perDay[i] * 100, 1)) + "%"
            except:
                self.missed_1stLevel_perDay_percent[i] = str(0.0) + "%"
        for i in range(32):
            try:
                self.answered_aa_perDay_percent[i] = str(round(float(self.answered_aa_perDay[i]) / self.total_perDay[i] * 100, 1)) + "%"
            except:
                self.answered_aa_perDay_percent[i] = str(0.0) + "%"

        for i in range(24):
            try:
                self.answered_1stLevel_perHour_percent[i] = str(round(float(self.answered_1stLevel_perHour[i]) / self.total_perHour[i] * 100, 1)) + "%"
            except:
                self.answered_1stLevel_perHour_percent[i] = str(0.0) + "%"
        for i in range(24):
            try:
                self.missed_1stLevel_perHour_percent[i] = str(round(float(self.missed_1stLevel_perHour[i]) / self.total_perHour[i] * 100, 1)) + "%"
            except:
                self.missed_1stLevel_perHour_percent[i] = str(0.0) + "%"
        for i in range(24):
            try:
                self.answered_aa_perHour_percent[i] = str(round(float(self.answered_aa_perHour[i]) / self.total_perHour[i] * 100, 1)) + "%"
            except:
                self.answered_aa_perHour_percent[i] = str(0.0) + "%"

    def create_csv_file(self):

        f = open(self.full_filename, "w")
        f.write("Total Calls: {}\n".format(self.total))
        f.write("Answered 1st Level: {} ({})\n".format(self.answered_1stLevel, self.answered_1stLevel_percent))
        f.write("Missed 1st Level: {} ({})\n".format(self.missed_1stLevel, self.missed_1stLevel_percent))
        f.write("Asnwered AA: {} ({})\n".format(self.answered_aa, self.answered_aa_percent))

        f.write("\n\nCalls Per Day")
        f.write("\nCall Type / Day,")
        f.write(",".join([str(i) for i in range(32)]))
        f.write("\nAnswered 1st Level,")
        f.write(",".join([str(i) for i in self.answered_1stLevel_perDay]))
        f.write("\nAnswered 1st Level (%),")
        f.write(",".join([str(i) for i in self.answered_1stLevel_perDay_percent]))
        f.write("\nMissed 1st Level,")
        f.write(",".join([str(i) for i in self.missed_1stLevel_perDay]))
        f.write("\nMissed 1st Level (%),")
        f.write(",".join([str(i) for i in self.missed_1stLevel_perDay_percent]))
        f.write("\nAnswered AA,")
        f.write(",".join([str(i) for i in self.answered_aa_perDay]))
        f.write("\nAnswered AA (%),")
        f.write(",".join([str(i) for i in self.answered_aa_perDay_percent]))

        f.write("\n\nCalls Per Hour")
        f.write("\nCall Type / Hour,")
        f.write(",".join([str(i) for i in range(24)]))
        f.write("\nAnswered 1st Level,")
        f.write(",".join([str(i) for i in self.answered_1stLevel_perHour]))
        f.write("\nAnswered 1st Level (%),")
        f.write(",".join([str(i) for i in self.answered_1stLevel_perHour_percent]))
        f.write("\nMissed 1st Level,")
        f.write(",".join([str(i) for i in self.missed_1stLevel_perHour]))
        f.write("\nMissed 1st Level (%),")
        f.write(",".join([str(i) for i in self.missed_1stLevel_perHour_percent]))
        f.write("\nAnswered AA,")
        f.write(",".join([str(i) for i in self.answered_aa_perHour]))
        f.write("\nAnswered AA (%),")
        f.write(",".join([str(i) for i in self.answered_aa_perHour_percent]))
        f.close()

    def create_html_content(self):

        self.html_content = "Total Calls: {}<br>".format(self.total)
        self.html_content += "Answered 1st Level: {} ({})<br>".format(self.answered_1stLevel, self.answered_1stLevel_percent)
        self.html_content += "Missed 1st Level: {} ({})<br>".format(self.missed_1stLevel, self.missed_1stLevel_percent)
        self.html_content += "Asnwered AA: {} ({})<br>".format(self.answered_aa, self.answered_aa_percent)


###########################################################################################################################################
class ExtensionStats:
    def __init__(self, extension, department):
        self.extension = extension
        self.department = department
        self.full_filename = "unknown"
        self.email_subject = "unknown"

        self.total = 0
        self.total_perDay = [0 for i in range(32)]
        self.total_perHour = [0 for i in range(24)]

        self.answered = 0
        self.answered_percent = 0
        self.answered_perDay = [0 for i in range(32)]
        self.answered_perDay_percent = [0 for i in range(32)]
        self.answered_perHour = [0 for i in range(24)]
        self.answered_perHour_percent = [0 for i in range(24)]

        self.missed = 0
        self.missed_percent = 0
        self.missed_perDay = [0 for i in range(32)]
        self.missed_perDay_percent = [0 for i in range(32)]
        self.missed_perHour = [0 for i in range(24)]
        self.missed_perHour_percent = [0 for i in range(24)]

        self.answered_vm = 0
        self.answered_vm_percent = 0
        self.answered_vm_perDay = [0 for i in range(32)]
        self.answered_vm_perDay_percent = [0 for i in range(32)]
        self.answered_vm_perHour = [0 for i in range(24)]
        self.answered_vm_perHour_percent = [0 for i in range(24)]

    def __str__(self):
        return "\ntotal: {}\ntotal_perDay: {}\ntotal_perHour: {}" \
               "\n\nanswered_1stLevel: {}" \
               "\nanswered_perDay: {}\nanswered_perDay_percent: {}" \
               "\nanswered_perHour: {}\nanswered_perHour_percent: {}" \
               "\n\nmissed_1stLevel: {}" \
               "\nmissed_perDay: {}\nmissed_perDay_percent: {}" \
               "\nmissed_perHour: {}\nmissed_perHour_percent: {}" \
               "\n\nanswered_aa: {}" \
               "\nanswered_aa_perDay: {}\nanswered_aa_perDay_percent: {}" \
               "\nanswered_aa_perHour: {}\nanswered_aa_perHour_percent: {}".format(
            self.total, self.total_perDay, self.total_perHour,
            self.answered,
            self.answered_perDay, self.answered_perDay_percent,
            self.answered_perHour, self.answered_perHour_percent,
            self.missed,
            self.missed_perDay, self.missed_perDay_percent,
            self.missed_perHour, self.missed_perHour_percent,
            self.answered_vm,
            self.answered_vm_perDay, self.answered_vm_perDay_percent,
            self.answered_vm_perHour, self.answered_vm_perHour_percent)

    def populate_percentages(self):

        try:
            self.answered_percent = str(round(float(self.answered) / self.total * 100, 1)) + "%"
        except:
            self.answered_percent = str(0.0) + "%"
        try:
            self.missed_percent = str(round(float(self.missed) / self.total * 100, 1)) + "%"
        except:
            self.missed_percent = str(0.0) + "%"
        try:
            self.answered_vm_percent = str(round(float(self.answered_vm) / self.total * 100, 1)) + "%"
        except:
            self.answered_vm_percent = str(0.0) + "%"

        for i in range(32):
            try:
                self.answered_perDay_percent[i] = str(round(float(self.answered_perDay[i]) / self.total_perDay[i] * 100, 1)) + "%"
            except:
                self.answered_perDay_percent[i] = str(0.0) + "%"
        for i in range(32):
            try:
                self.missed_perDay_percent[i] = str(round(float(self.missed_perDay[i]) / self.total_perDay[i] * 100, 1)) + "%"
            except:
                self.missed_perDay_percent[i] = str(0.0) + "%"
        for i in range(32):
            try:
                self.answered_vm_perDay_percent[i] = str(round(float(self.answered_vm_perDay[i]) / self.total_perDay[i] * 100, 1)) + "%"
            except:
                self.answered_vm_perDay_percent[i] = str(0.0) + "%"

        for i in range(24):
            try:
                self.answered_perHour_percent[i] = str(round(float(self.answered_perHour[i]) / self.total_perHour[i] * 100, 1)) + "%"
            except:
                self.answered_perHour_percent[i] = str(0.0) + "%"
        for i in range(24):
            try:
                self.missed_perHour_percent[i] = str(round(float(self.missed_perHour[i]) / self.total_perHour[i] * 100, 1)) + "%"
            except:
                self.missed_perHour_percent[i] = str(0.0) + "%"
        for i in range(24):
            try:
                self.answered_vm_perHour_percent[i] = str(round(float(self.answered_vm_perHour[i]) / self.total_perHour[i] * 100, 1)) + "%"
            except:
                self.answered_vm_perHour_percent[i] = str(0.0) + "%"

    def create_csv_file(self):

        f = open(self.full_filename, "w")
        f.write("Total Calls: {}\n".format(self.total))
        f.write("Answered 1st Level: {} ({})\n".format(self.answered, self.answered_percent))
        f.write("Missed 1st Level: {} ({})\n".format(self.missed, self.missed_percent))
        f.write("Asnwered VM: {} ({})\n".format(self.answered_vm, self.answered_vm_percent))

        f.write("\n\nCalls Per Day")
        f.write("\nCall Type / Day,")
        f.write(",".join([str(i) for i in range(32)]))
        f.write("\nAnswered 1st Level,")
        f.write(",".join([str(i) for i in self.answered_perDay]))
        f.write("\nAnswered 1st Level (%),")
        f.write(",".join([str(i) for i in self.answered_perDay_percent]))
        f.write("\nMissed 1st Level,")
        f.write(",".join([str(i) for i in self.missed_perDay]))
        f.write("\nMissed 1st Level (%),")
        f.write(",".join([str(i) for i in self.missed_perDay_percent]))
        f.write("\nAnswered VM,")
        f.write(",".join([str(i) for i in self.answered_vm_perDay]))
        f.write("\nAnswered VM (%),")
        f.write(",".join([str(i) for i in self.answered_vm_perDay_percent]))

        f.write("\n\nCalls Per Hour")
        f.write("\nCall Type / Hour,")
        f.write(",".join([str(i) for i in range(24)]))
        f.write("\nAnswered 1st Level,")
        f.write(",".join([str(i) for i in self.answered_perHour]))
        f.write("\nAnswered 1st Level (%),")
        f.write(",".join([str(i) for i in self.answered_perHour_percent]))
        f.write("\nMissed 1st Level,")
        f.write(",".join([str(i) for i in self.missed_perHour]))
        f.write("\nMissed 1st Level (%),")
        f.write(",".join([str(i) for i in self.missed_perHour_percent]))
        f.write("\nAnswered VM,")
        f.write(",".join([str(i) for i in self.answered_vm_perHour]))
        f.write("\nAnswered VM (%),")
        f.write(",".join([str(i) for i in self.answered_vm_perHour_percent]))
        f.close()

    def create_html_content(self):

        self.html_content = "Total Calls: {}<br>".format(self.total)
        self.html_content += "Answered 1st Level: {} ({})<br>".format(self.answered, self.answered_percent)
        self.html_content += "Missed 1st Level: {} ({})<br>".format(self.missed, self.missed_percent)
        self.html_content += "Asnwered VM: {} ({})<br>".format(self.answered_vm, self.answered_vm_percent)


###########################################################################################################################################
class HuntPilotStats:
    def __init__(self, huntpilot, department):
        self.huntpilot = huntpilot
        self.department = department
        self.full_filename = "unknown"
        self.email_subject = "unknown"

        self.total = 0
        self.total_perDay = [0 for i in range(32)]
        self.total_perHour = [0 for i in range(24)]

        self.answered = 0
        self.answered_percent = 0
        self.answered_perDay = [0 for i in range(32)]
        self.answered_perDay_percent = [0 for i in range(32)]
        self.answered_perHour = [0 for i in range(24)]
        self.answered_perHour_percent = [0 for i in range(24)]

        self.missed = 0
        self.missed_percent = 0
        self.missed_perDay = [0 for i in range(32)]
        self.missed_perDay_percent = [0 for i in range(32)]
        self.missed_perHour = [0 for i in range(24)]
        self.missed_perHour_percent = [0 for i in range(24)]

        self.answered_vm = 0
        self.answered_vm_percent = 0
        self.answered_vm_perDay = [0 for i in range(32)]
        self.answered_vm_perDay_percent = [0 for i in range(32)]
        self.answered_vm_perHour = [0 for i in range(24)]
        self.answered_vm_perHour_percent = [0 for i in range(24)]

        self.answeredBy = {}

    def __str__(self):
        return "\ntotal: {}\ntotal_perDay: {}\ntotal_perHour: {}" \
               "\n\nanswered: {}" \
               "\nanswered_perDay: {}\nanswered_perDay_percent: {}" \
               "\nanswered_perHour: {}\nanswered_perHour_percent: {}" \
               "\n\nmissed: {}" \
               "\nmissed_perDay: {}\nmissed_perDay_percent: {}" \
               "\nmissed_perHour: {}\nmissed_perHour_percent: {}" \
               "\n\nanswered_vm: {}" \
               "\nanswered_vm_perDay: {}\nanswered_vm_perDay_percent: {}" \
               "\nanswered_vm_perHour: {}\nanswered_vm_perHour_percent: {}" \
               "\n\nansweredBy: {}".format(
            self.total, self.total_perDay, self.total_perHour,
            self.answered,
            self.answered_perDay, self.answered_perDay_percent,
            self.answered_perHour, self.answered_perHour_percent,
            self.missed,
            self.missed_perDay, self.missed_perDay_percent,
            self.missed_perHour, self.missed_perHour_percent,
            self.answered_vm,
            self.answered_vm_perDay, self.answered_vm_perDay_percent,
            self.answered_vm_perHour, self.answered_vm_perHour_percent,
            self.answeredBy)

    def populate_percentages(self):

        try:
            self.answered_percent = str(round(float(self.answered) / self.total * 100, 1)) + "%"
        except:
            self.answered_percent = str(0.0) + "%"
        try:
            self.missed_percent = str(round(float(self.missed) / self.total * 100, 1)) + "%"
        except:
            self.missed_percent = str(0.0) + "%"
        try:
            self.answered_vm_percent = str(round(float(self.answered_vm) / self.total * 100, 1)) + "%"
        except:
            self.answered_vm_percent = str(0.0) + "%"

        for i in range(32):
            try:
                self.answered_perDay_percent[i] = str(round(float(self.answered_perDay[i]) / self.total_perDay[i] * 100, 1)) + "%"
            except:
                self.answered_perDay_percent[i] = str(0.0) + "%"
        for i in range(32):
            try:
                self.missed_perDay_percent[i] = str(round(float(self.missed_perDay[i]) / self.total_perDay[i] * 100, 1)) + "%"
            except:
                self.missed_perDay_percent[i] = str(0.0) + "%"
        for i in range(32):
            try:
                self.answered_vm_perDay_percent[i] = str(round(float(self.answered_vm_perDay[i]) / self.total_perDay[i] * 100, 1)) + "%"
            except:
                self.answered_vm_perDay_percent[i] = str(0.0) + "%"

        for i in range(24):
            try:
                self.answered_perHour_percent[i] = str(round(float(self.answered_perHour[i]) / self.total_perHour[i] * 100, 1)) + "%"
            except:
                self.answered_perHour_percent[i] = str(0.0) + "%"
        for i in range(24):
            try:
                self.missed_perHour_percent[i] = str(round(float(self.missed_perHour[i]) / self.total_perHour[i] * 100, 1)) + "%"
            except:
                self.missed_perHour_percent[i] = str(0.0) + "%"
        for i in range(24):
            try:
                self.answered_vm_perHour_percent[i] = str(round(float(self.answered_vm_perHour[i]) / self.total_perHour[i] * 100, 1)) + "%"
            except:
                self.answered_vm_perHour_percent[i] = str(0.0) + "%"

    def create_csv_file(self):

        f = open(self.full_filename, "w")
        f.write("Total Calls: {}\n".format(self.total))
        f.write("Answered 1st Level: {} ({})\n".format(self.answered, self.answered_percent))
        f.write("Missed 1st Level: {} ({})\n".format(self.missed, self.missed_percent))
        f.write("Asnwered VM: {} ({})\n".format(self.answered_vm, self.answered_vm_percent))

        f.write("\n\nCalls Per Day")
        f.write("\nCall Type / Day,")
        f.write(",".join([str(i) for i in range(32)]))
        f.write("\nAnswered 1st Level,")
        f.write(",".join([str(i) for i in self.answered_perDay]))
        f.write("\nAnswered 1st Level (%),")
        f.write(",".join([str(i) for i in self.answered_perDay_percent]))
        f.write("\nMissed 1st Level,")
        f.write(",".join([str(i) for i in self.missed_perDay]))
        f.write("\nMissed 1st Level (%),")
        f.write(",".join([str(i) for i in self.missed_perDay_percent]))
        f.write("\nAnswered VM,")
        f.write(",".join([str(i) for i in self.answered_vm_perDay]))
        f.write("\nAnswered VM (%),")
        f.write(",".join([str(i) for i in self.answered_vm_perDay_percent]))

        f.write("\n\nCalls Per Hour")
        f.write("\nCall Type / Hour,")
        f.write(",".join([str(i) for i in range(24)]))
        f.write("\nAnswered 1st Level,")
        f.write(",".join([str(i) for i in self.answered_perHour]))
        f.write("\nAnswered 1st Level (%),")
        f.write(",".join([str(i) for i in self.answered_perHour_percent]))
        f.write("\nMissed 1st Level,")
        f.write(",".join([str(i) for i in self.missed_perHour]))
        f.write("\nMissed 1st Level (%),")
        f.write(",".join([str(i) for i in self.missed_perHour_percent]))
        f.write("\nAnswered VM,")
        f.write(",".join([str(i) for i in self.answered_vm_perHour]))
        f.write("\nAnswered VM (%),")
        f.write(",".join([str(i) for i in self.answered_vm_perHour_percent]))
        f.close()

    def create_html_content(self):

        self.html_content = "Total Calls: {}<br>".format(self.total)
        self.html_content += "Answered 1st Level: {} ({})<br>".format(self.answered, self.answered_percent)
        self.html_content += "Missed 1st Level: {} ({})<br>".format(self.missed, self.missed_percent)
        self.html_content += "Asnwered VM: {} ({})<br><br><br>".format(self.answered_vm, self.answered_vm_percent)

        self.html_content += "Answered calls:<br>"
        for name, calls in self.answeredBy.items():
            self.html_content += "{}: {}<br>".format(name, calls)


###########################################################################################################################################
