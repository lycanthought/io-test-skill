from mycroft import MycroftSkill, intent_file_handler


class IoTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.io.intent')
    def handle_test_io(self, message):
        self.speak_dialog('test.io')


def create_skill():
    return IoTest()

