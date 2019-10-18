class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current < self.capacity:
      self.storage.append(item)
      self.current += 1

  def get(self):
    if self.current == 0:
      return []
    return self.storage

if __name__ == "__main__":


    buffer = RingBuffer(3)

    
    print(buffer.get())




