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

%install
umask 022
mkdir -p $RPM_BUILD_ROOT%{_dkroot}
pushd dotkit
tar --exclude Copyright -cf - . | (cd $RPM_BUILD_ROOT%{_dkroot} && tar xvf - )
popd dotkit

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_dkroot}
%doc dotkit/Copyright

# vi: expandtab sw=4 ts=4
