class Chatbot:
    """ An object that can engage in rudimentary conversation with a human. """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        """ Returns the Chatbot's way of introducing itself. """
        return "Hello, my name is " + self.name

    def response(self, prompt_from_human):
        """ Returns the Chatbot's response to something the human said. """
        return "It is very interesting that you say: '" + prompt_from_human + "'"


# TODO: keep reading! see below
class BoredChatbot(Chatbot):

    def response(self, prompt_from_human):
        count = len(prompt_from_human)
        if count < 20:
            return "It is very interesting that you say: '" + prompt_from_human + "'"
        else:
            return "zzz... Oh excuse me, I dozed off reading your essay."


sally = BoredChatbot("Sally")
human_message =input(sally.greeting())
print(sally.response(human_message))
