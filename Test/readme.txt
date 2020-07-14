
What images are in this directory

CentOS-6.10-x86_64-netinstall.iso
  This is the network install and rescue image.
  This image is designed to be burned onto a CD. You then boot your computer off the CD.

CentOS-6.10-x86_64-minimal.iso
  The aim of this image is to install a very basic CentOS 6.10 system, with the minimum of packages needed to have a functional system.
  Please burn this image onto a CD and boot your computer off it. A preselected set of packages will be installed on your system. Everything else needs to be installed using yum.
  The set of packages installed by this image is identical to the one installed when choosing the group named "Minimal" from the full DVD image.

CentOS-6.10-x86_64-bin-DVD1.iso
CentOS-6.10-x86_64-bin-DVD2.iso
  These two dvd images contain the entire base distribution.
  Please burn DVD1 onto a DVD and boot your computer off it.
  A basic install will not need DVD2.
  After the installation is complete, please run "yum update" in order to update your system.

CentOS-6.10-x86_64-LiveDVD.iso
  This is a DVD live image of CentOS 6.10 designed to be burned onto a DVD. You then boot your computer using that DVD.
  Please read http://wiki.centos.org/Manuals/ReleaseNotes/CentOSLiveDVD6.10 for more details about this image.
  The disk can also be used to install CentOS 6.10 onto your computer but without offering any package selection options at install time.


 Remember that in order to be able to partition your disk you will need to run the GUI installer which in turns needs enough RAM. The same is true for the network setup step.
 The release notes ( http://wiki.centos.org/Manuals/ReleaseNotes/CentOS6.10 ) provide more details about these aspects.


----------------------

List of images in this directory
================================

CentOS-7-x86_64-DVD-2003.iso
  This DVD image contains all the packages that can be installed using the
  installer. This is the recommended image for most users.

CentOS-7-x86_64-NetInstall-2003.iso
  This is the network install and rescue image. The installer will ask from 
  where it should fetch the packages to be installed. This image is most 
  useful if you have a local mirror of CentOS packages.

CentOS-7-x86_64-Everything-2003.iso
  This image contains the complete set of packages for  CentOS Linux 7. It can be 
  used for installing or populating a local mirror. This image needs a 16GB USB 
  flash drive as it is too large for DVD isos.

CentOS-7-x86_64-LiveGNOME-2003.iso
CentOS-7-x86_64-LiveKDE-2003.iso
  These images are Live images of  CentOS Linux 7. Depending on the name they use the
  respective display manager. They are designed for testing purposes and
  exploring the  CentOS Linux 7 environment. They will not modify the content of your 
  hard disk, unless you choose to install  CentOS Linux 7 from within the Live
  environment. Please be advised that you can not change the set of installed
  packages in this case. This needs to be done within the installed system
  using 'yum'.

CentOS-7-x86_64-Minimal-2003.iso
  The aim of this image is to install a very basic  CentOS Linux 7 system, with the 
  minimum of packages needed to have a functional system. Please burn this image
  onto a CD and boot your computer off it. A preselected set of packages will be
  installed on your system. Everything else needs to be installed using yum. The set
  of packages installed by this image is identical to the one installed when choosing
  the group named "Minimal" from the full DVD image.

Using the installation images
=============================

You can burn these images to a DVD or 'dd' them to a USB flash drive. 
After the boot media has been prepared, boot the computer off the boot media. 
If you do an install to your hard disk using these installation images, please 
remember to run "yum update" after the installation to update your system to the 
latest packages.

Remember that in order to be able to partition your disk you will need to run
the GUI installer which in turns needs enough RAM. The same is true for the 
network setup step. Please refer to the release notes available at 
http://wiki.centos.org/Manuals/ReleaseNotes/CentOS7 for more details about
these aspects.

