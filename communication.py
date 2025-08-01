class SmsSender:
    def send(self, schedule):
        print(f"Sending SMS to {schedule.get_customer().phone_number} for schedule at {schedule.get_date_time()}")

class MailSender:
    def send_mail(self, schedule):
        if schedule.get_customer().get_email():
            print(f"Sending email to {schedule.get_customer().get_email()} for schedule at {schedule.get_date_time()}")
