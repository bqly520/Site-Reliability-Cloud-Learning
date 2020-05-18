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

### BIOS (Basic Input Output System)
* When power is first applied to the hardware, **POST(Power on Self Test)** is the task that is part of BIOS to ensure that the computer hardware functioned correctly.
* It looks for the boot loader in floppy, cd-rom, or hard drive. You can typically press `F11` or `F12` during the BIOS startup to change the boot sequence
* BIOS POST checks for *basic operability of the hardware*. Once the boot loader is detected and loaded into **MEMORY**, BIOS gives **CONTROL** to it!
* So, in simple terms **BIOS loads and executes the MBR boot loader.**

### MBR (Master Boot Record)
* It is located in the 1st sector of the bootable disk. Typically `/dev/hda`(HDD), or `/dev/sda`(SSD).
* MBR is less than 512 bytes in size and contains information about **GRUB**. This has three components 
    1. **Primary Boot Loader** info in 1st 446 bytes 
	2. **Partition Table** info in next 64 bytes 
    3. **MBR Validation Check** in last 2 bytes.
* So, in simple terms **MBR loads and executes the GRUB boot loader.**

### GRUB (Grand Unified Boot Loader)
* At this stage, if you have **multiple kernel images** installed on your system, you can choose which one to be executed.
* GRUB displays a splash screen, waits for few seconds, if you don’t enter anything, it **loads the default kernel image** as specified in the **grub configuration file**.
* Grub configuration file is `/boot/grub/grub.conf` (`/etc/grub.conf` is a link to this).
* So, in simple terms **GRUB just loads and executes Kernel and initrd images.**

### Kernel
* Mounts the root **file system** as specified in the `“root=”` in grub.conf
* Kernel executes the `/sbin/init` program
* Since init was the 1st program to be executed by **Linux Kernel**, it has the process id (PID) of 1. Do a `‘ps -ef | grep init’` and check the pid.
* **initrd(Initial Ram Disk)** is used by kernel as **temporary root file system until kernel is booted** and the real root file system is mounted. It also contains necessary drivers compiled inside, which helps it to access the hard drive partitions, and other hardware.
* So, in simple terms **Kernel executes the /sbin/init program**

### Init
* Looks at the `/etc/inittab` file to decide the Linux run level.
* Following are the available run levels (Define these later)
    - 0 – halt
	- 1 – Single user mode
	- 2 – Multiuser, without NFS
	- 3 – Full multiuser mode
	- 4 – unused
	- 5 – X11
    - 6 – reboot
* Init identifies the default run level from `/etc/inittab` and uses that to load all appropriate program.
* Execute `‘grep initdefault /etc/inittab’` on your system to identify the default run level
* Typically you would set the default run level to either **3 or 5**. To get in trouble, set it to **0 or 6**
* So, in simple terms **Init looks at the /etc/inittab file to decide the Linux run level.**

### About Run Level Programs
* Depending on your **default init level setting**, the system will execute the programs from one of the following directories.
    - Run level 0 – /etc/rc.d/rc0.d/
	- Run level 1 – /etc/rc.d/rc1.d/
	- Run level 2 – /etc/rc.d/rc2.d/
	- Run level 3 – /etc/rc.d/rc3.d/
	- Run level 4 – /etc/rc.d/rc4.d/
	- Run level 5 – /etc/rc.d/rc5.d/
    - Run level 6 – /etc/rc.d/rc6.d/
* Please note that there are also **symbolic links** available for these directory under `/etc` directly. So, `/etc/rc0.d` is linked to `/etc/rc.d/rc0.d`.
* Under the `/etc/rc.d/rc*.d/` directories, you would see programs that start with **S** and **K**.
	- Programs starts with **S** are used during startup. **S for startup**.
    - Programs starts with **K** are used during shutdown. **K for kill**.
* There are **numbers right next to S and K** in the program names. Those are the sequence number in which the programs should be started or killed.
    - For example, **S12**syslog is to start the syslog deamon, which has the sequence number of 12. **S80**sendmail is to start the sendmail daemon, which has the sequence number of 80. So, **syslog** program will be started before **sendmail**.