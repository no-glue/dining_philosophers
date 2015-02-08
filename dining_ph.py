import threading
import random
import time

class Philosopher(threading.Thread):
  # show same mercy
  running = True
  # this is static, no need for object

  def __init__(self, xname, forkOnLeft, forkOnRight):
    # init
    threading.Thread.__init__(self)
    self.name = xname
    self.forkOnLeft = forkOnLeft
    self.forkOnRight = forkOnRight
  def run(self):
    # running
    while self.running:
      time.sleep(random.uniform(3, 13))
      # philosopher is sleeping (thinking)
      print "%s is hungry" % self.name
      self.dine()
  def dine(self):
    # getting chopsticks
    fork1, fork2 = self.forkOnLeft, self.forkOnRight
    while self.running:
      fork1.acquire(True)
      # blocking lock, the process will block until acquires the lock
      locked = fork2.acquire(False)
      # non blocking lock, the process will not block if no lock acquired
      if locked:
        break
        # acquired both forks, quit
      fork1.release()
      fork1, fork2 = fork2, fork1
    else:
      return
    self.dining()
    fork2.release()
    fork1.release()
  def dining(self):
    # dinning
    print "%s starts eating " % self.name
    time.sleep(random.uniform(1, 10))
    print "%s finishes eating and leaves to think" % self.name

def DiningPhilosophers():
  forks = [threading.Lock() for i in range(5)]
  philosopherNames = ["Aristotle", "Kant", "Buddha", "Euler", "Russel"]
  philosophers = [Philosopher(philosopherNames[i], forks[i%5], forks[(i+1)%5]) for i in range(5)]
  random.seed(507129)
  Philosopher.running = True
  for philosopher in philosophers:
    philosopher.start()
  time.sleep(100)
  Philosopher.running = False
  print "Now we are finishing"

if __name__ == "__main__":
  DiningPhilosophers()
