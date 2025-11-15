%global BuildArch x86_64
BuildArch:     x86_64
Name:          evernight-vista-boot-interface
Version:       2026.1
Release:       1.fc43
Source0:       https://github.com/EvernightFedora/evernight-vista-boot-interface/archive/refs/heads/main.zip
License:       GPLv3
Group:         Unspecified
Summary:       Plymouth "Spinner" theme Evernight Vista Edition






Conflicts:     plymouth-theme-spinner
#Conflicts:     march7th-vista-boot-interface
Obsoletes:      march7th-vista-boot-interface
Provides:      plymouth(system-theme)
Provides:      march7th-ace-boot-interface
Provides:      march7th-ace-boot-interface >= 2025.3-1.fc41
#Provides:      plymouth-plugin-two-step
Requires(post): /bin/sh  
Requires(postun): /bin/sh  
Requires:      font(cantarell)  
Requires:      font(cantarelllight)  
Requires:      plymouth-plugin-two-step
Requires(post): plymouth-scripts  
#Requires:      rpmlib(CompressedFileNames) <= 3.0.4-1
#Requires:      rpmlib(FileDigests) <= 4.6.0-1
#Requires:      rpmlib(PayloadFilesHavePrefix) <= 4.0-1
#Requires:      rpmlib(PayloadIsZstd) <= 5.4.18-1


%prep
%setup -q -n evernight-vista-boot-interface-main


%install
mkdir -p %{buildroot}/
cp -r /builddir/build/BUILD/evernight-vista-boot-interface-2026.1-build/evernight-vista-boot-interface-main/* %{buildroot}


%description
This package contains the "spinner" boot splash theme for
Plymouth. It features a small spinner on a dark background.
%files
%dir %attr(0755, root, root) "/usr/share/plymouth/themes/bgrt"
%attr(0644, root, root) "/usr/share/plymouth/themes/bgrt/bgrt.plymouth"
%dir %attr(0755, root, root) "/usr/share/plymouth/themes/spinner"
%attr(0644, root, root) "/usr/share/plymouth/themes/spinner/bullet.png"
%attr(0644, root, root) "/usr/share/plymouth/themes/spinner/capslock.png"
%attr(0644, root, root) "/usr/share/plymouth/themes/spinner/entry.png"
%attr(0644, root, root) "/usr/share/plymouth/themes/spinner/keyboard.png"
%attr(0644, root, root) "/usr/share/plymouth/themes/spinner/keymap-render.png"
%attr(0644, root, root) "/usr/share/plymouth/themes/spinner/lock.png"
%attr(0644, root, root) "/usr/share/plymouth/themes/spinner/spinner.plymouth"
%attr(0644, root, root) "/usr/share/plymouth/themes/spinner/throbber-0001.png"
%attr(0644, root, root) "/usr/share/plymouth/themes/spinner/throbber-0002.png"
%attr(0644, root, root) "/usr/share/plymouth/themes/spinner/throbber-0003.png"
%attr(0644, root, root) "/usr/share/plymouth/themes/spinner/throbber-0004.png"
%attr(0644, root, root) "/usr/share/plymouth/themes/spinner/throbber-0005.png"
%attr(0644, root, root) "/usr/share/plymouth/themes/spinner/throbber-0006.png"
%attr(0644, root, root) "/usr/share/plymouth/themes/spinner/throbber-0007.png"
%attr(0644, root, root) "/usr/share/plymouth/themes/spinner/throbber-0008.png"
%attr(0644, root, root) "/usr/share/plymouth/themes/spinner/throbber-0009.png"
%attr(0644, root, root) "/usr/share/plymouth/themes/spinner/throbber-0010.png"
"/usr/share/plymouth/themes/spinner/throbber-0011.png"
"/usr/share/plymouth/themes/spinner/throbber-0012.png"
"/usr/share/plymouth/themes/spinner/throbber-0013.png"
"/usr/share/plymouth/themes/spinner/throbber-0014.png"
"/usr/share/plymouth/themes/spinner/throbber-0015.png"
"/usr/share/plymouth/themes/spinner/throbber-0016.png"
"/usr/share/plymouth/themes/spinner/throbber-0017.png"
"/usr/share/plymouth/themes/spinner/throbber-0018.png"
"/usr/share/plymouth/themes/spinner/throbber-0019.png"
"/usr/share/plymouth/themes/spinner/throbber-0020.png"
"/usr/share/plymouth/themes/spinner/throbber-0021.png"
"/usr/share/plymouth/themes/spinner/throbber-0022.png"
"/usr/share/plymouth/themes/spinner/throbber-0023.png"
"/usr/share/plymouth/themes/spinner/throbber-0024.png"
"/usr/share/plymouth/themes/spinner/throbber-0025.png"
"/usr/share/plymouth/themes/spinner/throbber-0026.png"
"/usr/share/plymouth/themes/spinner/throbber-0027.png"
"/usr/share/plymouth/themes/spinner/throbber-0028.png"
"/usr/share/plymouth/themes/spinner/throbber-0029.png"
"/usr/share/plymouth/themes/spinner/throbber-0030.png"



%post -p /bin/sh
export PLYMOUTH_PLUGIN_PATH=/usr/lib64/plymouth/
# On upgrades replace charge with the new bgrt default
if [ $1 -eq 2 ]; then
    if [ "$(/usr/sbin/plymouth-set-default-theme)" == "charge" ]; then
        /usr/sbin/plymouth-set-default-theme bgrt
    fi
fi



%postun -p /bin/sh
export PLYMOUTH_PLUGIN_PATH=/usr/lib64/plymouth/
if [ $1 -eq 0 ]; then
    if [ "$(/usr/sbin/plymouth-set-default-theme)" == "bgrt" -o \
         "$(/usr/sbin/plymouth-set-default-theme)" == "spinner" ]; then
        /usr/sbin/plymouth-set-default-theme --reset
    fi
fi



