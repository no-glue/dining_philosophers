import threading
import random
import time

class Philosopher(threading.Thread):
  # show same mercy
  running = True
  # this is static, no need for object

  def __init__(self, xname, forkOnLeft, forkOnRight):
    threading.Thread.__init__(self)
    self.name = xname
    self.forkOnLeft = forkOnLeft
    self.forkOnRight = forkOnRight
  def run(self):
    while self.running:
      time.sleep(random.uniform(3, 13))
      # philosopher is sleeping (thinking)
      print "%s is hungry" % self.name
      self.dine()
  def dine(self):
    fork1, fork2 = self.forkOnLeft, self.forkOnRight
    while self.running:
      fork1.acquire(True)
      # blocking lock, the process will block until acquires the lock
      locked = fork2.acquire(False)
      # non blocking lock, the process will not block if no lock acquired
      if locked:
        break
        # acquired both forks
      fork1.release()
      fork1, fork2 = fork2, fork1
  def dining(self):

def DiningPhilosophers():

if __name__ == "__main__":
  DiningPhilosophers()
