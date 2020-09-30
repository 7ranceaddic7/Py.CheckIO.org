from typing import Iterable
from collections import deque

def replace_first(items: list) -> Iterable:
  # if len(items)<=1:
  #   return items
  # else:
  #   items = items[1:] + [items[0]]
  #   return items
  return items if not items else items[1:] + [items[0]]

if __name__ == '__main__':
    print("Example:")
    print(list(replace_first([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(replace_first([1, 2, 3, 4])) == [2, 3, 4, 1]
    assert list(replace_first([1])) == [1]
    assert list(replace_first([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
