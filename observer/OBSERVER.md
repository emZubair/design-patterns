### Observer Pattern

Observer pattern keeps the objects in loop when something happens which they care about.
```markdown
Observer pattern defines a one-to-many dependency between objects so that when one object changes state, 
all of its dependents are notified and updated automatically. 
```
The subject and observers define the one-to-many relationship. We have one subject, who notifies many observers
when something in the subject changes. The observers are dependent on the subject —- when the subject’s 
state changes, the observers are notified.
The subject implements a subject interface same goes for the observers with observer interface.

Observer pattern offer loose coupling between the subject and observers. Observer only knows about the main interface 
it doesn't know about the concrete implementations of that interface, so we can add/remove or update existing 
observers at the runtime and Subject and observers can exist independently of each other. Changes inside any of them 
wouldn't affect each other.