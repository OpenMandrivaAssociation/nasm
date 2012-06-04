Summary:	The Netwide Assembler, a portable x86 assembler with Intel-like syntax
Name:		nasm
Version:	2.10.01
Release:	2
Epoch:		1
License:	BSD
Group:		Development/Other
Source:		http://www.nasm.us/pub/nasm/releasebuilds/%{version}/%{name}-%{version}.tar.xz
URL:		http://nasm.sourceforge.net
BuildRequires:	ghostscript
BuildRequires:	groff
BuildRequires:	texinfo

%package doc
Summary:	Extensive documentation for NASM
Group:		Books/Computer books

%package rdoff
Summary:	Tools for the RDOFF binary format, sometimes used with NASM
Group:		Development/Other

%description
NASM is the Netwide Assembler, a free portable assembler for the Intel
80x86 microprocessor series, using primarily the traditional Intel
instruction mnemonics and syntax.

%description doc
Extensive documentation for the Netwide Assembler, NASM, in HTML,
PostScript, RTF and text formats.

%description rdoff
Tools for the operating-system independent RDOFF binary format, which
is sometimes used with the Netwide Assembler (NASM).  These tools
include linker, library manager, loader, and information dump.

%prep
%setup -q

%build
rm -f config.cache config.status config.log
%configure2_5x
make everything

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/{%{_bindir},%{_infodir},%{_mandir}/man1}
%makeinstall install_rdf
cd doc
install info/* %{buildroot}/%{_infodir}/
bzip2 -9f nasmdoc*.txt nasmdoc*.ps||true
cd html
ln -sf nasmdoc0.html index.html

%files
%doc LICENSE CHANGES TODO AUTHORS README doc/internal.doc
%attr(755,root,root) %{_bindir}/nasm
%attr(755,root,root) %{_bindir}/ndisasm
%attr(755,root,root) %{_bindir}/rdf2ith
%attr(755,root,root) %{_bindir}/rdf2srec
%{_mandir}/man1/ldrdf.1*
%{_mandir}/man1/nasm.1*
%{_mandir}/man1/ndisasm.1*
%{_mandir}/man1/rd*.1*
%{_infodir}/nasm.info*

%files doc
%doc doc/nasmdoc.ps.bz2 doc/nasmdoc.txt.bz2  doc/html

%files rdoff
%doc rdoff/README rdoff/doc/v1-v2.txt
%{_bindir}/rdfdump
%{_bindir}/ldrdf
%{_bindir}/rdx
%{_bindir}/rdflib
%{_bindir}/rdf2bin
%{_bindir}/rdf2ihx
%{_bindir}/rdf2com


