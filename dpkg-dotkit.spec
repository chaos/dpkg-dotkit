Name: dpkg-dotkit
Version:
Release:
Source:
License: GPL
Summary: stripped down version of dotkit for use with dpkg-runtests.
Group: Utilities/System
BuildRoot: %{_tmppath}/%{name}-%{version}
BuildArch: noarch

%define debug_package %{nil}
%define __spec_install_post /usr/lib/rpm/brp-compress || :
%define __check_files %{nil}
%define _dkroot /usr/share/dpkg-dotkit

%description
Stripped down version of dotkit for use with dpkg-runtests.

%prep
%setup

%build
umask 022
tar -xzf dotkit060613.tar.gz
pushd dotkit || exit 1
    find . -name \*.dk | xargs rm -f
    find . -name \*.cvsignore | xargs rm -f
    rm -rf tru64_5 solaris_8_s64 redhat_9_ia32 irix_6.5 hpux_11 aix_5 
    rm -rf irix_6.5_64 etc/examples etc/test html man etc/RCS 
    rm -f Changes Copyright FAQ README etc/*.example
    find . -name macos_10 | xargs rm -rf
    echo "/usr/local/dpkg-db/info" > etc/DK_NODE
popd

%install
umask 022
mkdir -p $RPM_BUILD_ROOT%{_dkroot}
pushd dotkit
tar cf - . | (cd $RPM_BUILD_ROOT%{_dkroot} && tar xvf - )

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_dkroot}

# vi: expandtab sw=4 ts=4
