### Command Pattern

```markdown
Creates command objects which encapsulate an object and provide a way to interact with that object's inner methods 
via a generic interface.
```
Command pattern is a behavioural pattern, a command object encapsulates a receiver into an object that exposes just one 
method called `execute`, which causes actions to be called on the receiver object. From the outside no one knows what 
action gets performed on the receiver.

A remote control with different slots where each slot can be assigned a random device. Respective on/off buttons with the 
slot control/interact with the assigned device, where turning the on button turns of the respective device 
assigned to that button.

For the slots, where no devices are assigned, we assign `NoCommand`, so that we can avoid null check every time 
the command is triggered.


