### Queue Challenge: Kigali Arena Concert Entry

**Scenario:**  
Design a queue system for managing entry to a concert at Kigali Arena.

**Requirements:**  
- Attendees arrive and join the queue in the order they arrive.
- Security checks each attendee one by one.
- No attendee can skip the line.

**Why Not Use a Stack?**  
A stack (LIFO) would allow the last person to arrive to enter first, which is unfair and causes disorder. A queue (FIFO) ensures the first person to arrive is the first to enter, maintaining fairness and order.

**Diagram:**

```
[Front]  Attendee1 <- Attendee2 <- Attendee3 <- ... <- AttendeeN  [Rear]
```

**Summary:**  
A queue system is ideal for concert entry because it processes attendees in the exact order they arrive, ensuring fairness and smooth flow.