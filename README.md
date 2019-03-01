
This page will help you get your MMA8451 accelerometer working for your raspberry pie microprocessor! While other repositories exist for this particular chip, this one will allow you to tell the orientation your chip is in. (NOTE: this project was built on a raspberry pi 3 B+)

If this is your first time using a raspberry pi, I highly recommend you update your system before doing anything else. You can do this by typing "sudo apt-get update" and "sudo apt-get upgrade" into your command line. 

After those installations are complete, use "raspi-config" to enter your pi's configurations window, go to the Interface tab, and enable your I2C, SPI, and SSH. Then reboot your pi with "reboot".

Once the reboot is done, your'e going to want to install some libraries that the MMA8451 will need to work correctly. 
"pip3 install RPI.GPIO" and "pip3 install adafruit-blinka". 

Now your'e ready for action!!

Wire the MMA8451 to your raspberyy pi with Vin to pin 1, ground to pin 9, SCL to pin 5, and SDA to pin 3. To check that your wiring is correct, type "sudo i2cdectect -y 1" and if it is only the term "1D" should show in the matrix. If you do not get that then try again. 

You should now be set to run your code! On a final note, if you get the "error 121" when you try to run it, it means the baudrate of you pi is too fast for your chip. You will need to go into the boot configuration to fix this issue. Do this with "sudo nano /boot/config.txt" and then add the line "dtparam=i2c-baudrate=10000". The pi's default baudrate is 100000 and is sometime too fast for your chip.
