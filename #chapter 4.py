#chapter 4 
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def peek(self):
        return self._top.data if self._top else None

    def push(self, data):
        # create new node
        new_node = Node(data)

        # point new node to current top
        new_node.next = self._top

        # update top
        self._top = new_node

        # update size
        self._size += 1

    def pop(self):
        # if stack is empty
        if self._top is None:
            return None

        # store top value
        value = self._top.data

        # move top pointer
        self._top = self._top.next

        # update size
        self._size -= 1

        return value

    def __repr__(self):
        current = self._top
        values = ''

        while current:
            values += f', {current.data}'
            current = current.next

        plural = '' if self._size == 1 else 's'
        return f'<Stack ({self._size} element{plural}): [{values.lstrip(", ")}]>'
    mystack = Stack()
mystack.push('A')
print(mystack)

#2 
def check_balance(text):
    stack = Stack()
    pairs = 0

    # dictionary to match closing to opening brackets
    matching = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for i in range(len(text)):
        ch = text[i]

        # opening brackets → push to stack
        if ch == '(' or ch == '[' or ch == '{':
            stack.push(ch)

        # closing brackets → pop and check
        elif ch == ')' or ch == ']' or ch == '}':
            if len(stack) == 0:
                return f"Match error at position {i}"

            top = stack.pop()
            if top != matching[ch]:
                return f"Match error at position {i}"

            pairs += 1

    # if something is left open
    if len(stack) != 0:
        return f"Match error at position {len(text) - 1}"

    return f"Ok - {pairs}"
a(b)c[d]e{f}g

#3
class StackBasedQueue:
    def __init__(self):
        self._InboundStack = Stack()
        self._OutboundStack = Stack()
        self._size = 0

    def __len__(self):
        return self._size

    def enqueue(self, value):
        self._InboundStack.push(value)
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            return None

        if len(self._OutboundStack) == 0:
            while len(self._InboundStack) > 0:
                self._OutboundStack.push(self._InboundStack.pop())

        self._size -= 1
        return self._OutboundStack.pop()

    def __repr__(self):
        # Build a list of values without removing from stacks permanently
        temp_in = Stack()
        temp_out = Stack()

        values = []

        # Get values from outbound stack (front of queue)
        while len(self._OutboundStack) > 0:
            val = self._OutboundStack.pop()
            values.append(val)
            temp_out.push(val)

        # Restore outbound stack
        while len(temp_out) > 0:
            self._OutboundStack.push(temp_out.pop())

        # Get values from inbound stack (back of queue)
        in_values = []
        while len(self._InboundStack) > 0:
            val = self._InboundStack.pop()
            in_values.append(val)
            temp_in.push(val)

        # Restore inbound stack
        while len(temp_in) > 0:
            self._InboundStack.push(temp_in.pop())

        # Combine lists in correct queue order
        values.extend(reversed(in_values))

        # Reverse to match expected output (back -> front)
        values.reverse()

        plural = '' if self._size == 1 else 's'
        return f"<StackBasedQueue ({self._size} element{plural}): [{', '.join(str(v) for v in values)}]>"
    
    #4
    class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'<ListNode: {self.data}>'


class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def enqueue(self, value):
        """
        Add a new node to the left (front) of the queue.
        """
        new_node = ListNode(value, prev=None, next=self._head)

        # If queue is empty
        if self._head is None:
            self._head = new_node
            self._tail = new_node
        else:
            # Link old head with new node
            self._head.prev = new_node
            self._head = new_node

        self._size += 1

    def dequeue(self):
        """
        Remove the oldest element from the right (tail) of the queue.
        """
        if self._tail is None:
            return None

        value = self._tail.data

        # If only one element
        if self._head == self._tail:
            self._head = None
            self._tail = None
        else:
            # Remove tail and update pointer
            self._tail = self._tail.prev
            self._tail.next = None

        self._size -= 1
        return value

    def __repr__(self):
        current = self._head
        values = []

        while current:
            values.append(str(current.data))
            current = current.next

        return f"<Queue ({self._size} element{'s' if self._size != 1 else ''}): [{', '.join(values)}]>"
    #5
    def get_pairs(numbers):
    even_queue = Queue()
    odd_queue = Queue()
    result = []

    for num in numbers:
        if num % 2 == 0:  # even number
            if len(odd_queue) > 0:     # check if odd queue has values
                odd_val = odd_queue.dequeue()
                result.append((num, odd_val))
            else:
                even_queue.enqueue(num)
        else:  # odd number
            if len(even_queue) > 0:    # check if even queue has values
                even_val = even_queue.dequeue()
                result.append((even_val, num))
            else:
                odd_queue.enqueue(num)

    return result
#5
