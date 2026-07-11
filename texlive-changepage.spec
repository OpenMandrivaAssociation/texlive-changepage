%global tl_name changepage
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0c
Release:	%{tl_revision}.1
Summary:	Margin adjustment and detection of odd/even pages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/changepage
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/changepage.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/changepage.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/changepage.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands to change the page layout in the middle of
a document, and to robustly check for typesetting on odd or even pages.
Instructions for use are at the end of the file. The package is an
extraction of code from the memoir class, whose user interface it
shares. It is intended the this package will eventually replace the
chngpage package, which is distributed with the package.

