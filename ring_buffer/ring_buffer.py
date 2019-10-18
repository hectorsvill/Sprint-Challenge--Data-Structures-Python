



class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current < self.capacity:
      # keep track of current item and set it with current 
      self.storage[self.current] = item
      self.current += 1

  def get(self):
    if self.current == 0:
      return []
    return self.storage

if __name__ == "__main__":
    buffer = RingBuffer(3)
    print(buffer.get())

    buffer.append('a')
    buffer.append('b')
    buffer.append('c')
    buffer.append('d')

    print(buffer.get())