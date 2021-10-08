# Postmortem
Since last month thousands of our timecard machines have stopped working. 

In the days that followed, complaints about devices caught in an endless startup boot loop began to trickle in through our support line.

To fix the issue, we had to replace the inoperable ones.

Drilling in

One thing you have to understand is that these internet-connected timecard machines in question are programmed to log their activities and send copies of this information to our database. This telemetry is sent to our servers when the player's firmware is told to check for a software update. These logs include things like when the machine went to standby, or how many punches occur in a day. 

The cause of the failure was an XML file downloaded by the network-connected devices from our servers during periodic logging policy checks.
This file, when fetched and saved to the device's flash storage and processed by the equipment, crashed the system software and force a reboot. Upon reboot, the device parsed the XML file again from its flash storage, crashed and rebooted again. And so on, and so on, and so on. Crucially, the XML file would be parsed before a new one could be fetched from the internet, so once the bad configuration file was fetched and stored by these particular devices there was no way we could fix this out in the field.
The problem with the XML file is that it wasn't formatted in a way compatible with the device's code. Though a valid XML file, it contained an empty list element, we're told:
<?xml version="1.0"?> <Policy>

<period val="2023-02-21T17:00:01"/> <server type="operating"/>
<list/>

</Policy>
Unfortunately for Us, the code which handles the processing of the log policy XML file has not been tested for such an empty <list/> element and causes a crash. The device code appears not to have been designed to handle that possibility because the empty list produces an invalid memory reference in the device's main program, which causes the kernel to terminate it.
Crashing the main program results in a reboot, but since the logging policy XML file is always processed early on after startup, the crash simply reoccurs before a fixed version of the file can be fetched. The result is that the player is stuck in a permanent boot loop
The only ways to revive the device is: erase the invalid policy file from the flash partition, or update the firmware of the device with a version in which the XML parse bug has been corrected. 
![Soldering image](/Soldering.png)
Unfortunately, both of these fixes require low-level access to the serial debug port of the device, soldering wires to the motherboard, proprietary hardware and software tools. Therefore we needed to bring in the devices to repair them in house.
From this point forward we’ve changed the xml policies and the main program to parse the xml after the full boot cycle. This way we would be able in the case it we send a broken xml again, we would be able to simply load from a usb making it a much easier repair
