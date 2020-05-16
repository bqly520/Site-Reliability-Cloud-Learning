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

#### BIOS
* 