Summary: X.Org SGML documentation generation tools
Name: xorg-sgml-doctools
Version: 1.1.1
Release: 4.1%{?dist}
License: MIT
Group: Development/Tools
URL: http://www.x.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: noarch

Source0: ftp://ftp.x.org/pub/individual/doc/%{name}-%{version}.tar.bz2

BuildRequires: pkgconfig

%description
This package is required in order to generate the X.Org X11 documentation
from source.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{_datadir}/sgml/X11
%{_datadir}/sgml/X11/defs.ent

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.1.1-4.1
- Rebuilt for RHEL 6

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 15 2008 Adam Jackson <ajax@redhat.com> 1.1.1-2
- Fix license tag.

* Mon Feb 05 2007 Adam Jackson <ajax@redhat.com> 1.1.1-1
- Update to 1.1.1

* Mon Jul 24 2006 Mike A. Harris <mharris@redhat.com> 1.1-2.fc6
- Change rpm Group to "Application/Text" which is what sgml-common uses.

* Mon Jul 24 2006 Mike A. Harris <mharris@redhat.com> 1.1-1.fc6
- Initial build.
