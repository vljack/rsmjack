# rsmjack

Uses [FRC4564's Maestro library][frcmaestro] to drive the Pololu Micro Maestro 6-channel USB servo controller of the RobotSexMachine v1. (Google it.)



# Usage

Do NOT use this if you are not comfortable changing your robot's default settings and do not know how to change them back! See **Disclaimer**.)

1. Set your Micro Maestro to **USB Dual Port** mode in "Serial Settings" in Pololu Maestro Control Center. 

2. Install PySerial.

3. Find your servo controller's device name in /dev. Add it to `demo.py` in place of `YOURDEVICENAME`.

4. Run `python3 demo.py`.



# Disclaimer

Use at your own risk. I am not responsible for any damage caused by this software.



[frcmaestro]: <https://github.com/FRC4564/Maestro>


# License

MIT
