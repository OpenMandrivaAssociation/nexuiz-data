%define	oname nexuiz

Summary:	Data files for the open-source first-person shooter Nexuiz
Name:		%{oname}-data
Version:	2.5.2
Release:	5
License:	GPLv2+
Group:		Games/Other
URL:		http://www.nexuiz.com/
# (tpg) original source is here http://downloads.sourceforge.net/nexuiz/nexuiz-24.zip
# extract only needed files
# unzip nexuiz-252.zip
# mkdir nexuiz-data-2.5.2/
# mv Nexuiz/data/ Nexuiz/Docs Nexuiz/gpl.txt nexuiz-data-2.5.2/
# tar cYf nexuiz-data-2.5.2.tar.lzma nexuiz-data-2.5.2/
Source0:	%{oname}-data-%{version}.tar.lzma
Source11:	%{oname}-16x16.png
Source12:	%{oname}-32x32.png
Source13:	%{oname}-48x48.png
BuildArch:	noarch
Requires:	%{oname} = %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Nexuiz is a multiplayer 3D first-person shooter based upon a
heavily modified Quake 1 engine.

This package contains the data files for Nexuiz.

WARNING: This game contains violence that is not suitable for children.

%prep
%setup -q
chmod 644 *.txt
sed -i 's/\r//' Docs/*.htm* Docs/*.txt

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_gamesdatadir}/%{oname}/data/
install -m644 data/*.pk3 %{buildroot}%{_gamesdatadir}/%{oname}/data/
install -m644 %{SOURCE11} -D %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{oname}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{oname}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{oname}.png

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Docs
%{_gamesdatadir}/%{oname}
%{_iconsdir}/hicolor/*/apps/%{oname}.png


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 2.5.2-4mdv2011.0
+ Revision: 613052
- the mass rebuild of 2010.1 packages

* Tue Dec 15 2009 Samuel Verschelde <stormi@mandriva.org> 2.5.2-3mdv2010.1
+ Revision: 479052
- bump release

  + Funda Wang <fwang@mandriva.org>
    - rebuild
    - New version 2.5.2

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - update to new version 2.5.1

* Fri May 01 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 2.5-1mdv2010.0
+ Revision: 369301
- update to new version 2.5

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 2.4.2-2mdv2009.0
+ Revision: 268267
- rebuild early 2009.0 package (before pixel changes)

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - new version
    - fix docs

* Fri May 02 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 2.4-1mdv2009.0
+ Revision: 199945
- new version
- extract only needed files from the upstream all-in-one zip file
- move icons to the fd.o compiliant directory
- add scriplets
- spec file clean

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.3-1mdv2008.1
+ Revision: 136630
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jun 01 2007 Eskild Hustvedt <eskild@mandriva.org> 2.3-1mdv2008.0
+ Revision: 34290
- New version 2.3


* Sun Jan 28 2007 Eskild Hustvedt <eskild@mandriva.org> 2.2.3-1mdv2007.0
+ Revision: 114574
- New version 2.2.3(includes a security fix)

* Thu Dec 14 2006 Eskild Hustvedt <eskild@mandriva.org> 2.2.1-1mdv2007.1
+ Revision: 97145
- New version 2.2.1

  + Olivier Blin <oblin@mandriva.com>
    - Import nexuiz-data

* Thu Sep 14 2006 Eskild Hustvedt <eskild@mandriva.org> 2.1-1mdv
- New version 2.1

* Fri Jun 16 2006 Eskild Hustvedt <eskild@mandriva.org> 2.0-1mdv
- New version 2.0

* Thu Feb 16 2006 Eskild Hustvedt <eskild@mandriva.org> 1.5-1mdk
- New version 1.5

* Sun Oct 30 2005 Eskild Hustvedt <eskild@mandriva.org> 1.2.1-1mdk
- New version 1.2.1

* Wed Aug 31 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.2-1mdk
- 1.2

* Wed Jul 06 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.1-1mdk
- splitted out from nexuiz packag
- move data from %%{_libdir} to %%{_gamesdatadir}
- use png icons

