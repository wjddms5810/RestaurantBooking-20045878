from communication import SmsSender, MailSender


class TestableSmsSender(SmsSender):
    def __init__(self):
        super().__init__()
        self._send_called = False

    def send(self, schedule):
        print("테스트용 SmsSender에서 send 메서드 실행됨")
        self._send_called = True

    @property
    def send_called(self) -> bool:
        return self._send_called


class TestableMailSender(MailSender):
    def __init__(self):
        self._send_mail_count = 0

    def send_mail(self, schedule):
        self._send_mail_count +=1

    @property
    def send_mail_count(self) -> int:
        return self._send_mail_count