from mycroft import MycroftSkill, intent_file_handler

import sysv_ipc as sysv

message = 'test'
message_type = 1
key = 0
queue = 0

class IoTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        key = sysv.ftok("/home/robot/ftok_file", 1, True)
        queue = sysv.MessageQueue(message_queue_key, sysv.IPC_CREAT)

    @intent_file_handler('test.io.intent')
    def handle_test_io(self, message):
        self.speak_dialog('test.io')
        queue.send(message, True, message_type)

def create_skill():
    return IoTest()

