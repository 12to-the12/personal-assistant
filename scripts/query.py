# responsbile for actually making the openai api call
from dotenv import load_dotenv
import dotenv
import os
import openai
from pathlib import Path
from config import config




if config["model"] == "gpt-3.5-turbo" or config["model"] == "gpt-4":
    config["chat"] = True
else:
    config["chat"] = False


dotenv_path = config["dotenv_path"]
load_dotenv(dotenv_path)
openai.api_key = os.getenv("OPENAI_API_KEY")


def query_completion(prompt, temperature=config["temperature"], max_tokens=config["max_tokens"]):
    response = openai.Completion.create(
        engine=config["model"],
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens
        # stop="\n"
    )
    # print(response)
    response = response.choices[0].text
    return response




def query_chat(messages=None, model="gpt-4"):
    print('posting')
    # print(model)
    # print(messages)
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    # print('received')
    response = response['choices'][0]['message']['content']
    return response

import os
clear = lambda : os.system("clear")

if __name__ == "__main__":
    clear()
    print("querying response")
    prompt="""

    I am running Fedora 37, I am trying to reinstall nvidia drivers on my device, and I think kernel-core has drivers related stuff

    Asahi linux is a project to port to the M1 Mac, I am running x86_64 on an Asus device, why does apple related stuff appear? Please help. 
    Bash results:
    [logan@laptop ~]$ sudo dracut --force
    cp: cannot stat '/usr/share/asahi-scripts/*': No such file or directory
    dracut-install: Failed to find module 'apple_mailbox'
    dracut: FAILED:  /usr/lib/dracut/dracut-install -D /var/tmp/dracut.IfsNJM/initramfs -N ^nvidia$|^nvidia_drm$|^nvidia-modeset$|^nvidia-uvm$ --kerneldir /lib/modules/6.3.5-100.fc37.x86_64/ -m apple_mailbox nvme_apple pinctrl-apple-gpio macsmc macsmc-rtkit i2c-apple tps6598x apple-dart dwc3 dwc3-of-simple nvmem-apple-efuses phy-apple-atc xhci-pci pcie-apple gpio_macsmc spi-apple spi-hid-apple spi-hid-apple-of rtc-macsmc simple-mfd-spmi spmi-apple-controller nvmem_spmi_mfd apple-dockchannel dockchannel-hid apple-rtkit-helper
    [logan@laptop ~]$ 
    """

    prompt="""
    I am running Fedora 37, I am trying to reinstall nvidia drivers on my device, and I think kernel-core has drivers related stuff
    ```bash
    dracut --force
    ```
    fails with

    ```
    cp: cannot stat '/usr/share/asahi-scripts/*': No such file or directory
    ``` 

    /usr/lib/dracut/dracut.conf.d

    contains

    01-dist.conf  02-rescue.conf  50-nss-softokn.conf

    Asahi linux is a project to port to the M1 Mac, I am running x86_64 on an Asus device, why is apple related stuff giving me errors? Please help. 

    I just deleted the entry 10-asahi.conf
    with sudo rm /usr/lib/dracut/dracut.conf.d/10-asahi.conf
    why am I still getting errors related to it?

    ```bash
    grep -r "asahi" /usr/lib/dracut/dracut.conf.d/
    ```
    returns nothing


    ```bash
    [logan@laptop share]$ ls /usr/lib/dracut/modules.d/ | grep asahi
    99asahi-firmware
    [logan@laptop share]$ sudo find / -name "*asahi*"
    find: ‘/proc/6096/task/181906’: No such file or directory
    find: ‘/run/user/1000/doc’: Permission denied
    find: ‘/run/user/1000/gvfs’: Permission denied
    find: ‘/tmp/.mount_ObsidiYIq79F’: Permission denied
    /usr/lib/dracut/modules.d/99asahi-firmware
    /usr/lib/dracut/modules.d/99asahi-firmware/install-asahi-firmware.sh
    /usr/lib/dracut/modules.d/99asahi-firmware/load-asahi-firmware.sh
    /usr/share/licenses/dracut-asahi
    /var/cache/PackageKit/38/metadata/fedora-38-x86_64/packages/dracut-asahi-20221206-2.fc38.noarch.rpm
    ```
    """
    prompt="""
    I am running Fedora 37, I am trying to reinstall nvidia drivers on my device, and I think kernel-core has drivers related stuff
    ```bash
    [logan@laptop share]$ sudo dnf remove *nvidia*
    Error: 
     Problem: The operation would result in removing the following protected packages: kernel-core
    ```
    """

    prompt = """
    I am running Fedora 37, I am trying to reinstall nvidia drivers on my device, and I think kernel-core has drivers related stuff
    ```bash
    [logan@laptop ~]$ nvidia-smi
    NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.
    [logan@laptop ~]$ sudo akmods --force
    Checking kmods exist for 6.3.5-100.fc37.x86_64             [  OK  ]
    Building and installing nvidia-kmod                        [FAILED]
    Building rpms failed; see /var/cache/akmods/nvidia/520.56.06-1-for-6.3.5-100.fc37.x86_64.failed.log for details

    Hint: Some kmods were ignored or failed to build or install.
    You can try to rebuild and install them by by calling
    '/usr/sbin/akmods --force' as root.

    Checking kmods exist for 6.3.12-100.fc37.x86_64            [  OK  ]
    Building and installing nvidia-kmod                        [FAILED]
    Building rpms failed; see /var/cache/akmods/nvidia/520.56.06-1-for-6.3.12-100.fc37.x86_64.failed.log for details

    Hint: Some kmods were ignored or failed to build or install.
    You can try to rebuild and install them by by calling
    '/usr/sbin/akmods --force' as root.
    [logan@laptop ~]$ cat /var/cache/akmods/nvidia/520.56.06-1-for-6.3.5-100.fc37.x86_64.failed.log
    2023/07/16 12:23:21 akmods: Building RPM using the command '/sbin/akmodsbuild --kernels 6.3.5-100.fc37.x86_64 /usr/src/akmods/nvidia-kmod.latest'
    %dir /lib/modules/6.3.5-100.fc37.x86_64/extra
    /lib/modules/6.3.5-100.fc37.x86_64/extra/nvidia/

    %global __kmodtool_kernel_uname_r 6.3.5-100.fc37.x86_64
    %global __spec_install_post \
      %{?__debug_package:%{__debug_install_post}}\
      %{__arch_install_post}\
      %{__os_install_post}\
      %{?__kmodtool_signmodules:%{__kmodtool_modsign_install_post}}\
      %{?__kmodtool_zipmodules:%{__kmodtool_modzip_install_post}}

    %global kmodinstdir_prefix  /lib/modules/
    %global kmodinstdir_postfix /extra/nvidia/
    %global kernel_versions     6.3.5-100.fc37.x86_64___%{_usrsrc}/kernels/6.3.5-100.fc37.x86_64

    + cd /tmp/akmodsbuild.rrrkJc3Q/BUILD
    + rm -rf nvidia-kmod-520.56.06
    + /usr/bin/mkdir -p nvidia-kmod-520.56.06
    + cd nvidia-kmod-520.56.06
    + /usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
    + tar --use-compress-program xz -xf /usr/share/nvidia-kmod-520.56.06/nvidia-kmod-520.56.06-x86_64.tar.xz
    tar (child): /usr/share/nvidia-kmod-520.56.06/nvidia-kmod-520.56.06-x86_64.tar.xz: Cannot open: No such file or directory
    tar (child): Error is not recoverable: exiting now
    tar: Child returned status 2
    tar: Error is not recoverable: exiting now
    error: Bad exit status from /var/tmp/rpm-tmp.2Y6hNn (%prep)

    RPM build warnings:
        user mockbuild does not exist - using root
        group mock does not exist - using root
        user mockbuild does not exist - using root
        group mock does not exist - using root

    RPM build errors:
        Bad exit status from /var/tmp/rpm-tmp.2Y6hNn (%prep)
    --- snip --- (this part says that it failed to build)
    ```

    on boot I get the message nvidia kernel missing, falling back to Nouveau

    I have uninstalled and reinstalled the drivers over and over again, it has not fixed the problem
    Can you tell me why akmods fails?

    this is my boot sequence:
    ```
    savedefault
    load_video
    set gfxpayload=keep
    insmod gzio
    insmod part_gpt
    insmod ext2
    search --no-floppy --fs-uuid --set=root 654813ac-64d8-47e6-bc8d-de7362e1cee2
    echo	'Loading Linux 6.3.12-100.fc37.x86_64 ...'
    linux	/vmlinuz-6.3.12-100.fc37.x86_64 root=UUID=afbcbb5f-b016-4708-93a5-a86c4cdbf63f ro rootflags=subvol=root rd.driver.blacklist=nouveau modprobe.blacklist=nouveau nvidia-drm.modeset=1 rhgb rd.driver.blacklist=nouveau modprobe.blacklist=nouveau nvidia-drm.modeset=1 
    echo	'Loading initial ramdisk ...'
    initrd	/initramfs-6.3.12-100.fc37.x86_64.img
    ```
    """

    prompt = """
    this is my boot sequence:
    ```
    savedefault
    load_video
    set gfxpayload=keep
    insmod gzio
    insmod part_gpt
    insmod ext2
    search --no-floppy --fs-uuid --set=root 654813ac-64d8-47e6-bc8d-de7362e1cee2
    echo	'Loading Linux 6.3.12-100.fc37.x86_64 ...'
    linux	/vmlinuz-6.3.12-100.fc37.x86_64 root=UUID=afbcbb5f-b016-4708-93a5-a86c4cdbf63f ro rootflags=subvol=root rd.driver.blacklist=nouveau modprobe.blacklist=nouveau nvidia-drm.modeset=1 rhgb rd.driver.blacklist=nouveau modprobe.blacklist=nouveau nvidia-drm.modeset=1 
    echo	'Loading initial ramdisk ...'
    initrd	/initramfs-6.3.12-100.fc37.x86_64.img
    ```

    and this prints when booting:
    ```
    Booting 'Fedora Linux (6.3.5-100.fc37.x86_64) 37 (Workstation Edition)'
    error ../..grub-core/fs/fshelp.c:257:file /EFI/FEDORA/grubenv' not found.
    Loading Linux 6.3.5-100.fc37.x86_64 ...
    Loading initial ramdisk ...

    Press any key to continue..._
    ```
    A few questions:
    - is this a sign of a problem?
    - What commands can I run to gather more information if it is?
    - are any of these boot lines extraneous?
    - please explain every boot line and everything that prints out
    - am I meant to edit grub configs directly or the system configuration instead?
    - how do I get rid of blacklist nouveau?

    """

    prompt = """
    I am running Fedora 37 GNOME with Wayland, I am trying to get the nvidia drivers working on my device
    right now, all I'm trying to do is get nouveau to work again

    Device: Asus Zephyrus G14 2020

    
    [logan@laptop ~]$ lspci | grep VGA
    01:00.0 VGA compatible controller: NVIDIA Corporation GA107M [GeForce RTX 3050 Mobile] (rev a1)
    04:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Cezanne [Radeon Vega Series / Radeon Vega Mobile Series] (rev c5)
    [logan@laptop ~]$ lspci | grep -i nvidia
    01:00.0 VGA compatible controller: NVIDIA Corporation GA107M [GeForce RTX 3050 Mobile] (rev a1)
    01:00.1 Audio device: NVIDIA Corporation Device 2291 (rev a1)
    ```

    under Settings About:
    Graphics only shows AMD Radeon™ Graphics

    sudo lshw -c video
    indicates nouveau is the driver


    I expect to see "No Nvidia drivers detected, falling back to Nouveau" when booting, but I don't see it
    """

    # prompt = """
    # Fedora
    # - How do I edit grub boot configuration entries?
    # - How do I regenerate boot configuration
    # - Am I supposed to directly edit them, or are they suppoed to be generated
    # """

    prompt = """
    I am running Fedora 37 GNOME with Wayland, I am trying to get the nvidia drivers working on my device
    ```bash
    [logan@laptop ~]$ sudo akmods --force --verbose
    Checking kmods exist for 6.3.7-100.fc37.x86_64             [  OK  ]
    Building and installing nvidia-kmod                        [FAILED]
    Building rpms failed; see /var/cache/akmods/nvidia/520.56.06-1-for-6.3.7-100.fc37.x86_64.failed.log for details

    Hint: Some kmods were ignored or failed to build or install.
    You can try to rebuild and install them by by calling
    '/usr/sbin/akmods --force' as root.

    Checking kmods exist for 6.3.12-100.fc37.x86_64            [  OK  ]
    Building and installing nvidia-kmod                        [FAILED]
    Building rpms failed; see /var/cache/akmods/nvidia/520.56.06-1-for-6.3.12-100.fc37.x86_64.failed.log for details

    Hint: Some kmods were ignored or failed to build or instasudo dnf remove *nvidia* --noautoremove --exclude=nvidia-gpu-firmware
    '/usr/sbin/akmods --force' as root.

    ```

    /var/cache/akmods/nvidia/520.56.06-1-for-6.3.7-100.fc37.x86_64.failed.log : 
    ```
    2023/07/16 14:19:21 akmods: Building RPM using the command '/sbin/akmodsbuild --kernels 6.3.7-100.fc37.x86_64 /usr/src/akmods/nvidia-kmod.latest'
    %dir /lib/modules/6.3.7-100.fc37.x86_64/extra
    /lib/modules/6.3.7-100.fc37.x86_64/extra/nvidia/

    %global __kmodtool_kernel_uname_r 6.3.7-100.fc37.x86_64
    %global __spec_install_post \
      %{?__debug_package:%{__debug_install_post}}\
      %{__arch_install_post}\
      %{__os_install_post}\
      %{?__kmodtool_signmodules:%{__kmodtool_modsign_install_post}}\
      %{?__kmodtool_zipmodules:%{__kmodtool_modzip_install_post}}

    %global kmodinstdir_prefix  /lib/modules/
    %global kmodinstdir_postfix /extra/nvidia/
    %global kernel_versions     6.3.7-100.fc37.x86_64___%{_usrsrc}/kernels/6.3.7-100.fc37.x86_64

    + cd /tmp/akmodsbuild.SLlHYH8P/BUILD
    + rm -rf nvidia-kmod-520.56.06
    + /usr/bin/mkdir -p nvidia-kmod-520.56.06
    + cd nvidia-kmod-520.56.06
    + /usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
    + tar --use-compress-program xz -xf /usr/share/nvidia-kmod-520.56.06/nvidia-kmod-520.56.06-x86_64.tar.xz
    tar (child): /usr/share/nvidia-kmod-520.56.06/nvidia-kmod-520.56.06-x86_64.tar.xz: Cannot open: No such file or directory
    tar (child): Error is not recoverable: exiting now
    tar: Child returned status 2
    tar: Error is not recoverable: exiting now
    error: Bad exit status from /var/tmp/rpm-tmp.DU8Ta9 (%prep)

    RPM build warnings:
        user mockbuild does not exist - using root
        group mock does not exist - using root
        user mockbuild does not exist - using root
        group mock does not exist - using root

    RPM build errors:
        Bad exit status from /var/tmp/rpm-tmp.DU8Ta9 (%prep)
    --- snip ---
    2023/07/16 14:19:22 akmodsbuild: tar (child): /usr/share/nvidia-kmod-520.56.06/nvidia-kmod-520.56.06-x86_64.tar.xz: Cannot open: No such file or directory
    2023/07/16 14:19:22 akmodsbuild: tar (child): Error is not recoverable: exiting now
    2023/07/16 14:19:22 akmodsbuild: tar: Child returned status 2
    2023/07/16 14:19:22 akmodsbuild: tar: Error is not recoverable: exiting now
    2023/07/16 14:19:22 akmodsbuild: error: Bad exit status from /var/tmp/rpm-tmp.DU8Ta9 (%prep)
    2023/07/16 14:19:22 akmodsbuild: 
    2023/07/16 14:19:22 akmodsbuild: RPM build warnings:
    2023/07/16 14:19:22 akmodsbuild: user mockbuild does not exist - using root
    2023/07/16 14:19:22 akmodsbuild: group mock does not exist - using root
    2023/07/16 14:19:22 akmodsbuild: user mockbuild does not exist - using root
    2023/07/16 14:19:22 akmodsbuild: group mock does not exist - using root
    2023/07/16 14:19:22 akmodsbuild: 
    2023/07/16 14:19:22 akmodsbuild: RPM build errors:
    2023/07/16 14:19:22 akmodsbuild: Bad exit status from /var/tmp/rpm-tmp.DU8Ta9 (%prep)
    2023/07/16 14:19:22 akmodsbuild: 
    2023/07/16 14:19:22 akmods: Building rpms failed; see /var/cache/akmods/nvidia/520.56.06-1-for-6.3.7-100.fc37.x86_64.failed.log for details
    ```
    

    """

    prompt = """
    Help, I'm running Fedora and I can't get other kernel version boot entries to show when booting, despite rebuilding multiple times, and them being in /boot
    """etc/default/grub
        {"role": "user", "content": prompt}
    ]
    print( query_chat(messages=messages) )