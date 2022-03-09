from mycroft import MycroftSkill, intent_file_handler

import sysv_ipc as sysv

message_name_1 = "test"
message_name_2 = "wake"
message_type = 1
key = sysv.ftok("/home/robot/ftok_file", 1, True)
queue = sysv.MessageQueue(key, sysv.IPC_CREAT)

class IoTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.add_event('recognizer_loop:wakeword',
                       self.handle_wakeword)

    @intent_file_handler('test.io.intent')
    def handle_test_io(self, message):
        self.speak_dialog('test.io')
        queue.send(message_name_1, True, message_type)

    def handle_wakeword(self, message):
        queue.send(message_name_2, True, message_type)


def create_skill():
    return IoTest()

