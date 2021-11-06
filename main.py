from kahoot import client
import time

bot = client()

joins = input("Joins: ")
pin = input("PIN: ")
username = input("Name: ")

for i in range(0, joins):
  
  bot.join(pin, username + str(i))

  def joinHandle():
    pass

  bot.on("joined", joinHandle)
  time.sleep(0.5)
