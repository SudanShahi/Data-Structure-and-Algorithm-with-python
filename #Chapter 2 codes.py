#Chapter 2 codes 
from __future__ import annotations
import ctypes

class ReservedMemory():
    def __init__(self, size: int) -> None:
        if not isinstance(size, int):
            raise TypeError('Memory size must be a positive integer > 0!')
        if not 1 <= size <= 65536:
            raise ValueError('Reserved memory size must be between 1 and 65536 bytes!')
        self._reserved_memory = ctypes.create_string_buffer(size)

    def __len__(self) -> int:
        return len(self._reserved_memory)

    def copy(self, mem_source, count:int=None, source_index:int=0, destination_index:int=0) -> None:
        if count is None:
            count = len(mem_source._reserved_memory) - source_index
        self._reserved_memory[destination_index:destination_index+count] = \
            mem_source._reserved_memory[source_index:source_index+count]

    def __getitem__(self, k:int) -> int:
        return ord(self._reserved_memory[k])

    def __setitem__(self, k:int, val:int) -> None:
        self._reserved_memory[k] = val


class IntArray():
    def __init__(self, bytes_per_element:int = 2) -> None:
        self._resmem = None
        self._size = 0
        self._bytes_per_element = bytes_per_element
        self._shift_val = 2**((self._bytes_per_element * 8)-1)
        self._min_val = -self._shift_val
        self._max_val = self._shift_val - 1

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self) -> int:
        if self._iter_index < self._size:
            self._iter_index += 1
            return self.__getitem__(self._iter_index-1)
        raise StopIteration

    def __repr__(self) -> str:
        if not self._resmem:
            return "Empty IntArray"
        return f"IntArray ({self._size} elements): [{', '.join(str(v) for v in self)}]"

    def __setitem__(self, k:int, val:int) -> None:
        val_to_store = val + self._shift_val
        for b in range(self._bytes_per_element):
            self._resmem[k*self._bytes_per_element+b] = (val_to_store >> (8*b)) & 255

    def __getitem__(self, k:int) -> int:
        stored_val = 0
        for b in range(self._bytes_per_element):
            stored_val |= self._resmem[k*self._bytes_per_element+b] << (8*b)
        return stored_val - self._shift_val

    def append(self, val: int) -> None:
        self._size += 1
        new_resmem = ReservedMemory(self._size*self._bytes_per_element)
        if self._resmem:
            new_resmem.copy(self._resmem)
        self._resmem = new_resmem
        self.__setitem__(self._size-1, val)

    def pop(self) -> int:
        if self._size == 0:
            return None

        val = self.__getitem__(self._size-1)
        self._size -= 1

        if self._size > 0:
            new_resmem = ReservedMemory(self._size*self._bytes_per_element)
            new_resmem.copy(self._resmem, count=self._size*self._bytes_per_element)
        else:
            new_resmem = None

        self._resmem = new_resmem
        return val

    def insert(self, index:int, val:int) -> None:
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")

        if not isinstance(val, int) or not self._min_val <= val <= self._max_val:
            raise TypeError(
                f'Value must be an integer between {self._min_val} and {self._max_val}'
            )

        self._size += 1
        new_resmem = ReservedMemory(self._size * self._bytes_per_element)

        # Copy elements before index
        if self._resmem and index > 0:
            new_resmem.copy(
                self._resmem,
                count=index * self._bytes_per_element
            )

        # Copy elements after index
        if self._resmem and index < self._size - 1:
            new_resmem.copy(
                self._resmem,
                count=(self._size - index - 1) * self._bytes_per_element,
                source_index=index * self._bytes_per_element,
                destination_index=(index + 1) * self._bytes_per_element
            )

        self._resmem = new_resmem
        self.__setitem__(index, val)
array = IntArray()
for i in range(6):
    array.append(i)
array.insert(5, 10)
print(array)


#EXCERISE 2
from __future__ import annotations
import ctypes

class ReservedMemory():
    """
    A class to reserve and handle a contigous area of memory. The
    constructor needs the size of the memory area (in bytes) to be
    reserved.
    """
    def __init__(self, size: int) -> None:
        if not isinstance(size, int):
            raise(TypeError('Memory size must be a positive integer > 0!'))
        if not 1 <= size <= 65536:
            raise(ValueError('Reserved memory size must be between 1 and 65536 bytes!'))
        self._reserved_memory = ctypes.create_string_buffer(size)

    def __len__(self) -> int:
        return len(self._reserved_memory)

    def __repr__(self) -> str:
        l = len(self._reserved_memory)
        plural = 's' if l > 1 else ''
        str_repr = f"[{', '.join(str(ord(i)) for i in self._reserved_memory)}]"
        return f"ReservedMemory ({l} byte{plural}): {str_repr}"

    def copy(self, mem_source:ReservedMemory, count:int=None, source_index:int=0, destination_index:int=0) -> None:
        if count is None:
            count = len(mem_source._reserved_memory) - source_index
        self._reserved_memory[destination_index:destination_index+count] = \
            mem_source._reserved_memory[source_index:source_index+count]

    def __getitem__(self, k:int) -> int:
        return ord(self._reserved_memory[k])

    def __setitem__(self, k:int, val:int) -> None:
        self._reserved_memory[k] = val


class IntArray():
    def __init__(self, bytes_per_element:int = 2) -> None:
        self._resmem = None
        self._size = 0
        self._bytes_per_element = bytes_per_element
        self._shift_val = 2**((self._bytes_per_element * 8)-1)
        self._min_val = -self._shift_val
        self._max_val = self._shift_val - 1

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self) -> int:
        if self._iter_index < self._size:
            self._iter_index += 1
            return self.__getitem__(self._iter_index-1)
        else:
            raise StopIteration

    def __repr__(self) -> str:
        if not self._resmem:
            return "Empty IntArray"
        plural = 's' if self._size > 1 else ''
        return f"IntArray ({self._size} element{plural}): [{', '.join(str(v) for v in self)}]"

    def __setitem__(self, k:int, val:int) -> None:
        val_to_store = val + self._shift_val
        for byte_index in range(self._bytes_per_element):
            self._resmem[k*self._bytes_per_element+byte_index] = \
                (val_to_store >> (8*byte_index)) & 255

    def __getitem__(self, k:int) -> int:
        stored_val = 0
        for byte_index in range(self._bytes_per_element):
            stored_val |= self._resmem[k*self._bytes_per_element+byte_index] << (8*byte_index)
        return stored_val - self._shift_val

    def append(self, val: int) -> None:
        self._size += 1
        new_resmem = ReservedMemory(self._size*self._bytes_per_element)
        if self._resmem:
            new_resmem.copy(self._resmem)
        self._resmem = new_resmem
        self.__setitem__(self._size-1, val)

    def pop(self) -> int:
        if self._size == 0:
            return None

        val = self.__getitem__(self._size-1)
        self._size -= 1

        if self._size > 0:
            new_resmem = ReservedMemory(self._size*self._bytes_per_element)
            new_resmem.copy(self._resmem, count=self._size*self._bytes_per_element)
        else:
            new_resmem = None

        self._resmem = new_resmem
        return val

    def remove(self, index:int) -> int:
        # Index validation
        if not isinstance(index, int):
            raise IndexError('Index must be integer')
        if index < 0 or index >= self._size:
            raise IndexError('Index out of bounds')

        # Value to return
        removed_value = self.__getitem__(index)

        # New size
        new_size = self._size - 1

        # If array becomes empty
        if new_size == 0:
            self._resmem = None
            self._size = 0
            return removed_value

        # Allocate new memory
        new_resmem = ReservedMemory(new_size * self._bytes_per_element)

        # Copy bytes before removed index
        bytes_before = index * self._bytes_per_element
        if bytes_before > 0:
            new_resmem.copy(self._resmem, count=bytes_before)

        # Copy bytes after removed index
        bytes_after = (self._size - index - 1) * self._bytes_per_element
        if bytes_after > 0:
            new_resmem.copy(
                self._resmem,
                count=bytes_after,
                source_index=(index + 1) * self._bytes_per_element,
                destination_index=index * self._bytes_per_element
            )

        self._resmem = new_resmem
        self._size = new_size
        return removed_value
array = IntArray()
for i in range(6):
    array.append(i)
val = array.remove(3)
print(val, array)

#EXCERISE 3
from __future__ import annotations
import ctypes


class ReservedMemory():
    def __init__(self, size: int) -> None:
        if not isinstance(size, int):
            raise TypeError('Memory size must be a positive integer > 0!')
        if not 1 <= size <= 65536:
            raise ValueError('Reserved memory size must be between 1 and 65536 bytes!')
        self._reserved_memory = ctypes.create_string_buffer(size)

    def __len__(self) -> int:
        return len(self._reserved_memory)

    def copy(self, mem_source, count=None, source_index=0, destination_index=0) -> None:
        if count is None:
            count = len(mem_source._reserved_memory) - source_index

        self._reserved_memory[destination_index:destination_index+count] = \
            mem_source._reserved_memory[source_index:source_index+count]

    def __getitem__(self, k: int) -> int:
        return ord(self._reserved_memory[k])

    def __setitem__(self, k: int, val: int) -> None:
        self._reserved_memory[k] = val


class IntArray():
    def __init__(self, bytes_per_element: int = 2) -> None:
        self._resmem = None
        self._size = 0
        self._bytes_per_element = bytes_per_element
        self._shift_val = 2 ** ((bytes_per_element * 8) - 1)
        self._min_val = -self._shift_val
        self._max_val = self._shift_val - 1

    def __len__(self) -> int:
        return self._size

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self) -> int:
        if self._iter_index < self._size:
            val = self[self._iter_index]
            self._iter_index += 1
            return val
        raise StopIteration

    def __repr__(self) -> str:
        if not self._resmem:
            return "Empty IntArray"
        return f"IntArray ({self._size} elements): [{', '.join(str(v) for v in self)}]"

    def __getitem__(self, k: int) -> int:
        stored_val = 0
        for i in range(self._bytes_per_element):
            stored_val |= self._resmem[k * self._bytes_per_element + i] << (8 * i)
        return stored_val - self._shift_val

    def __setitem__(self, k: int, val: int) -> None:
        val += self._shift_val
        for i in range(self._bytes_per_element):
            self._resmem[k * self._bytes_per_element + i] = (val >> (8 * i)) & 255

    def append(self, val: int) -> None:
        self._size += 1
        new_mem = ReservedMemory(self._size * self._bytes_per_element)
        if self._resmem:
            new_mem.copy(self._resmem)
        self._resmem = new_mem
        self[self._size - 1] = val

    def pop(self):
        if self._size == 0:
            return None
        val = self[self._size - 1]
        self._size -= 1
        if self._size > 0:
            new_mem = ReservedMemory(self._size * self._bytes_per_element)
            new_mem.copy(self._resmem, self._size * self._bytes_per_element)
            self._resmem = new_mem
        else:
            self._resmem = None
        return val

    def search(self, value):
        for i in range(self._size):
            if self[i] == value:
                return i
        return -1
array = IntArray()
for i in range(6):
    array.append(i+i)

print(array.search(8))
