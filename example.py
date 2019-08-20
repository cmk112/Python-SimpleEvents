from SimpleEvents import Event

# each time we use this decorator with a new name, a new event is created
@Event.called('input_received')
def input_processing(string):# **kwargs are used. You can treat them as a dict, or pass through the specific variables.

    if string == "hello":
            print("Well, hello there!")


class App:
    # the event execution list is dependant on position. This will run next.
    @Event.called('input_received')
    def shoot_em(string):

        print("I'm here! Hi.")

    # We can call 
    @Event.called('end_of_execution')
    def exit_text(string):

        print("The end. This is a different event.")


user_input = input(">")

#this is how you call the event.
Event.call('input_received', string=user_input)
Event.call('end_of_execution', string=None)