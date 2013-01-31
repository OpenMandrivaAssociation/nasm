Summary:	The Netwide Assembler, a portable x86 assembler with Intel-like syntax
Name:		nasm
Version:	2.10.07
Release:	1
Epoch:		1
License:	BSD
Group:		Development/Other
Source0:	http://www.nasm.us/pub/nasm/releasebuilds/%{version}/%{name}-%{version}.tar.xz
URL:		http://nasm.sourceforge.net
BuildRequires:	ghostscript
BuildRequires:	groff
BuildRequires:	texinfo

%package	doc
Summary:	Extensive documentation for NASM
Group:		Books/Computer books
BuildArch:	noarch

%package	rdoff
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
%configure2_5x
make everything

%install
%makeinstall install_rdf
cd doc
cp -r info %{buildroot}%{_infodir}
xz -v --text nasmdoc*.txt nasmdoc*.ps||true
cd html
ln -sf nasmdoc0.html index.html

%files
%doc LICENSE CHANGES TODO AUTHORS README doc/internal.doc
%{_bindir}/nasm
%{_bindir}/ndisasm
%{_bindir}/rdf2ith
%{_bindir}/rdf2srec
%{_mandir}/man1/ldrdf.1*
%{_mandir}/man1/nasm.1*
%{_mandir}/man1/ndisasm.1*
%{_mandir}/man1/rd*.1*
%{_infodir}/nasm.info*

%files doc
%doc doc/nasmdoc.ps.xz doc/nasmdoc.txt.xz doc/html

%files rdoff
%doc rdoff/README rdoff/doc/v1-v2.txt
%{_bindir}/rdfdump
%{_bindir}/ldrdf
%{_bindir}/rdx
%{_bindir}/rdflib
%{_bindir}/rdf2bin
%{_bindir}/rdf2ihx
%{_bindir}/rdf2com
