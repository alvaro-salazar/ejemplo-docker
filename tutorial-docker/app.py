import time
from datetime import datetime

print("Bienvenido al codelab de docker")
while True:
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print(f"Se ha consultado el log del contenedor a las {current_time}")
  time.sleep(3)
