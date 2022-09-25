import nidaqmx
import time
import thermistor
# Initialize DAQ Device 
from nidaqmx.constants
import (TerminalConfiguration)
# Initialize DAQ Device
task_ai = nidaqmx.Task()
task_ai.ai_channels.add_ai_voltage_chan("Dev1/ai0", 
terminal_config=TerminalConfiguration.RSE)
task_ai.start()
task_do = nidaqmx.Task()
task_do.do_channels.add_do_chan("Dev1/port0/line0")
task_do.start()
alarmlimit = 28 #degrees Celsius
Ts = 2
N = 10
# Start Logging
for k in range(N):
Vout = task_ai.read()
TempC = thermistor.thermistorTemp(Vout)
print(round(TempC,1))
if TempC >= alarmlimit:
task_do.write(True)
print("Alarm!")
else:
task_do.write(False) 
print("OK")
time.sleep(Ts)
# Terminate DAQ Device
task_ai.stop; task_ai.close()
task_do.stop; task_do.close()