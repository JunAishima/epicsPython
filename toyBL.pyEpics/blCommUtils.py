import time
global message_string_pv

def broadcast_output(s):
  time.sleep(0.01)
  message_string_pv.put(s,wait=True)
