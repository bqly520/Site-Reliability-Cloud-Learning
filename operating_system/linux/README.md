# Linux

## Sections

* [Boot Process](#boot-process)

### Boot Process
* `BIOS` (Basic Input Output System which executes **MBR**)
* `MBR` (Master Boot Record which executes **GRUB**)
* `GRUB` (Grand Unified Boot Loader which executes **Kernel**)
* `Kernel` (Kernel loads and executes **/sbin/init**)
* `Init` (Init executes runlevel programs)
* `Runlevel` (Runlevel programs are executed from **/etc/rc.d/rc*.d/**)

#### BIOS (Basic Input Output System)
* When power is first applied to the hardware, **POST(Power on Self Test)** is the task that is part of BIOS to ensure that the computer hardware functioned correctly.
* It looks for the boot loader in floppy, cd-rom, or hard drive. You can typically press `F11` or `F12` during the BIOS startup to change the boot sequence
* BIOS POST checks for *basic operability of the hardware*. Once the boot loader is detected and loaded into **MEMORY**, BIOS gives **CONTROL** to it!
* So, in simple terms **BIOS loads and executes the MBR boot loader.**

#### MBR (Master Boot Record)
* It is located in the 1st sector of the bootable disk. Typically `/dev/hda`(HDD), or `/dev/sda`(SSD).
* MBR is less than 512 bytes in size and contains information about **GRUB**. This has three components 
    1. **Primary Boot Loader** info in 1st 446 bytes 
	2. **Partition Table** info in next 64 bytes 
    3. **MBR Validation Check** in last 2 bytes.
* So, in simple terms **MBR loads and executes the GRUB boot loader.**
