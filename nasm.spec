Summary:	The Netwide Assembler, a portable x86 assembler with Intel-like syntax
Name:		nasm
Version:	3.01
Release:	1
License:	BSD
Group:		Development/Tools
Url:		https://www.nasm.us/
Source0:	http://www.nasm.us/pub/nasm/releasebuilds/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	xmlto
BuildRequires:	asciidoc
Obsoletes: %{name}-rdoff < %{EVRD}

%patchlist
nasm-3.00-clang.patch

%description
NASM is the Netwide Assembler, a free portable assembler for the Intel
80x86 microprocessor series, using primarily the traditional Intel
instruction mnemonics and syntax.

%files
%doc LICENSE CHANGES AUTHORS doc/internal.doc
%{_bindir}/nasm
%{_bindir}/ndisasm
%doc %{_mandir}/man1/nasm.1*
%doc %{_mandir}/man1/ndisasm.1*

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
xz -v --text nasmdoc*.txt nasmdoc*.ps||true
