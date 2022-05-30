from mycroft import MycroftSkill, intent_file_handler


class RoboArmOnWheels(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('wheels.on.arm.robo.intent')
    def handle_wheels_on_arm_robo(self, message):
        action = message.data.get('action')

        self.speak_dialog('wheels.on.arm.robo', data={
            'action': action
        })


def create_skill():
    return RoboArmOnWheels()

