Summary:	The Netwide Assembler, a portable x86 assembler with Intel-like syntax
Name:		nasm
Version:	2.16.01
Release:	2
Epoch:		1
License:	BSD
Group:		Development/Tools
Url:		http://nasm.sourceforge.net
Source0:	http://www.nasm.us/pub/nasm/releasebuilds/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	ghostscript
BuildRequires:	groff
BuildRequires:	perl(Font::TTF)
BuildRequires:	fontconfig
BuildRequires:	fonts-ttf-liberation
Obsoletes: %{name}-rdoff < %{EVRD}

%description
NASM is the Netwide Assembler, a free portable assembler for the Intel
80x86 microprocessor series, using primarily the traditional Intel
instruction mnemonics and syntax.

%files
%doc LICENSE CHANGES AUTHORS doc/internal.doc
%{_bindir}/nasm
%{_bindir}/ndisasm
%{_mandir}/man1/nasm.1*
%{_mandir}/man1/ndisasm.1*
#%{_infodir}/nasm.info*

#----------------------------------------------------------------------------

#%package doc
#Summary:	Extensive documentation for NASM
#Group:		Documentation
#BuildArch:	noarch

#%description doc
#Extensive documentation for the Netwide Assembler, NASM, in HTML,
#PostScript, RTF and text formats.

#%files doc
#%doc doc/nasmdoc.ps.xz doc/nasmdoc.txt.xz doc/html

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure

%make_build all manpages
# all manpages rdf

%install
%make_install

cd doc
#cp -r info %{buildroot}%{_infodir}
xz -v --text nasmdoc*.txt nasmdoc*.ps||true
#cd html
#ln -sf nasmdoc0.html index.html
