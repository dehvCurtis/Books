


# check installed packages, installs if not already installed
package_check:
  pkg.installed:
    - name: linux-firmware
    - name: microcode_ctl

# install the latest kernel
install-latest-kernel:
  kernelpkg.upgrade

kernel_check:
  module.run:
    - name: grains.setval
    - key: kernel_check_val
    - val: complete


# reboot operations
boot-latest-kernel:
  kernelpkg.latest_installed:
    - reboot: True
    - at_time: 1
    - onchanges:
      - kernel: install-latest-kernel



