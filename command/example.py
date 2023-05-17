from abc import ABC, abstractmethod
import inspect


class Command(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError(f"{inspect.stack()[0][3]} not implemented")

    @abstractmethod
    def undo(self):
        raise NotImplementedError(f"{inspect.stack()[0][3]} not implemented")


class NoCommand(Command):
    def execute(self):
        print("No Command found")

    def undo(self):
        print("No Command found")


class Light:
    def __init__(self, name):
        self.name = name

    def off(self):
        print(f"Turning {self.name} light off")

    def on(self):
        print(f"Turning {self.name} light on!!!")


class LightOnCommand(Command):

    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):

    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class Controller:
    def __init__(self):
        self.on_commands = []
        self.off_commands = []
        self.last_command = NoCommand()

        _kitchen_light = Light(name="Kitchen Light")

        kitchen_light_on_command = LightOnCommand(_kitchen_light)
        kitchen_light_off_command = LightOffCommand(_kitchen_light)
        self.on_commands.append(kitchen_light_on_command)
        self.off_commands.append(kitchen_light_off_command)

        bedroom_light = Light(name="Bedroom Light")
        bedroom_light_on_command = LightOnCommand(bedroom_light)
        bedroom_light_off_command = LightOffCommand(bedroom_light)
        self.on_commands.append(bedroom_light_on_command)
        self.off_commands.append(bedroom_light_off_command)

    def set_command(self, on_command, off_command):
        self.on_commands.append(on_command)
        self.off_commands.append(off_command)

    def on_command_for_index(self, index):
        last_command = self.on_commands[index]
        last_command.execute()

    def off_command_for_index(self, index):
        last_command = self.on_commands[index]
        last_command.execute()

    def undo_last_command(self):
        self.last_command.undo()
        self.last_command = NoCommand()

    def clear_all_slots(self):
        self.on_commands = []
        self.off_commands = []


controller = Controller()
controller.on_command_for_index(0)
controller.on_command_for_index(1)

controller.off_command_for_index(1)
controller.off_command_for_index(0)

no_command = NoCommand()

controller.set_command(no_command, no_command)
controller.off_command_for_index(2)
controller.off_command_for_index(2)


"""
We can also use the lambda functions instead of commands
"""
