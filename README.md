
This page will help you get your MMA8451 accelerometer working for your raspberry pie microprocessor! While other repositories exist for this particular chip, this one will allow you to tell the orientation your chip is in.

If this is your first time using a raspberry pi, I highly recommend you update your system before doing anything else. You can do this by typing "sudo apt-get update" and "sudo apt-get upgrade" into your command line. 

After those installations are complete, use "raspi-config" to enter your pi's configurations window, go to the Interface tab, and enable your I2C, SPI, and SSH. Then reboot your pi with "reboot".

Once the reboot is done, your'e going to want to install some libraries that the MMA8451 will need to work correctly. 
"pip3 install RPI.GPIO" and "pip3 install adafruit-blinka". 

Now your'e ready for action!!
