import ctypes
import gc
import sys

def ref_count(address:int)->int:
    '''' a function that rteturn reference count for object using memory address '''
    return ctypes.c_long.from_address(address).value

def is_mutable(obj) -> bool:
    return isinstance(obj, (list, dict, set, bytearray))

def inspect_variables(name: str , val):
    member_add = id(val)
    print(f"\n--- checking: {name} ---")
    print(f"Type: {type(val).__name__}")
    print(f"Value: {val!r}")
    print(f"(ID): {hex(member_add)}")
    print(f"(Mutable): {is_mutable(val)}")
    print(f"(Ref Count): {ref_count(member_add)}")
    
def demonstrate_interning():
        print("\n--- Integer Interning ([-5, 256]) ---")
        a = 256
        b = 256
        print(f"256 is 256? -> {a is b} (same id: {id(a) == id(b)})")
        x = 257
        y = 257
        print(f"257 is 257? -> {x is y} (repl stuff)")
def demonstrate_circular_ref():

    gc.disable()  
    class Node:
     def __init__(self, name):
        self.name = name
        self.link = None

    node1 = Node("A")
    node2 = Node("B")
    node1.link = node2
    node2.link = node1

    addr1, addr2 = id(node1), id(node2)
    print(f"Ref count before gc: A={ref_count(addr1)}, B={ref_count(addr2)}")
    del node1
    del node2
    print(f"Ref count after del (circular ref): A={ref_count(addr1)}, B={ref_count(addr2)}")
    unreachable = gc.collect()
    print(f"object collected by gc: {unreachable}")
    gc.enable()

if __name__ == "__main__":
    x = [1, 2, 3]
    inspect_variables("x", x)
    demonstrate_interning()
    demonstrate_circular_ref()
    