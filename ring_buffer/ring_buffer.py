



class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # check if you went over capacity
    # set current back to 0 
    # print(self.current)
    if self.current == self.capacity:
      self.current = 0

     # keep track of current item and set it with current 
    if self.current < self.capacity:
      self.storage[self.current] = item
      self.current += 1

  def get(self):
    # get all items that are not None
    return [item for item in self.storage if item != None]

if __name__ == "__main__":
    buffer = RingBuffer(3)
    print(buffer.get())

    buffer.append('a')
    buffer.append('b')
    buffer.append('c')

    buffer.append('d')
    print(buffer.get())