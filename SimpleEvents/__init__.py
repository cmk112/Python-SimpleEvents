class Event:

    """
    EVENT class by Cody Kostyak
    Main componenet of simple events.
    METHODS:
    called(self, name:str) - used with decorator to register Event.
    call(self, name:str, **kwargs) - used to call the function (named by decorator call)
    """

    event_list = {}

    @classmethod
    def called(self, name:str):
        """
        use with decorator to register Event to the system. Called using Event.call(name,**kwargs).
        name = str
        """
        def run_func(func):
            if name not in self.event_list.keys():
                self.event_list[name] = []
            self.event_list[name].append(func)
            return func
        return run_func


    @classmethod
    def call(self, name:str, **kwargs):
        """
        Call an event by name (declared in Event.called decorator function), pass through **kwargs to the event saved in event_list.
        name = name of event declared by decorator function.
        **kwargs = arguments to pass to decorator function.
        """
        for func in self.event_list[name]:
            func(**kwargs)

