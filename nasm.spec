Summary:	The Netwide Assembler, a portable x86 assembler with Intel-like syntax
Name:		nasm
Version:	2.11.08
Release:	2
Epoch:		1
License:	BSD
Group:		Development/Tools
Url:		http://nasm.sourceforge.net
Source0:	http://www.nasm.us/pub/nasm/releasebuilds/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	ghostscript
BuildRequires:	groff
BuildRequires:	texinfo

%description
NASM is the Netwide Assembler, a free portable assembler for the Intel
80x86 microprocessor series, using primarily the traditional Intel
instruction mnemonics and syntax.

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

#----------------------------------------------------------------------------

%package doc
Summary:	Extensive documentation for NASM
Group:		Documentation
BuildArch:	noarch

%description doc
Extensive documentation for the Netwide Assembler, NASM, in HTML,
PostScript, RTF and text formats.

%files doc
%doc doc/nasmdoc.ps.xz doc/nasmdoc.txt.xz doc/html

#----------------------------------------------------------------------------

%package rdoff
Summary:	Tools for the RDOFF binary format, sometimes used with NASM
Group:		Development/Tools

%description rdoff
Tools for the operating-system independent RDOFF binary format, which
is sometimes used with the Netwide Assembler (NASM).  These tools
include linker, library manager, loader, and information dump.

%files rdoff
%doc rdoff/README rdoff/doc/v1-v2.txt
%{_bindir}/rdfdump
%{_bindir}/ldrdf
%{_bindir}/rdx
%{_bindir}/rdflib
%{_bindir}/rdf2bin
%{_bindir}/rdf2ihx
%{_bindir}/rdf2com

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure
%make everything

%install
%makeinstall install_rdf
cd doc
cp -r info %{buildroot}%{_infodir}
xz -v --text nasmdoc*.txt nasmdoc*.ps||true
cd html
ln -sf nasmdoc0.html index.html

