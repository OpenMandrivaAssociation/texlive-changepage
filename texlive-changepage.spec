Name:		texlive-changepage
Version:	15878
Release:	2
Summary:	Margin adjustment and detection of odd/even pages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/changepage
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changepage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changepage.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changepage.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands to change the page layout in the
middle of a document, and to robustly check for typesetting on
odd or even pages. Instructions for use are at the end of the
file. The package is an extraction of code from the memoir
class, whose user interface it shares. It is intended the this
package will eventually replace the chngpage package, which is
distributed with the package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/changepage/changepage.sty
%{_texmfdistdir}/tex/latex/changepage/chngpage.sty
%doc %{_texmfdistdir}/doc/latex/changepage/README
%doc %{_texmfdistdir}/doc/latex/changepage/changepage.pdf
#- source
%doc %{_texmfdistdir}/source/latex/changepage/changepage.ins
%doc %{_texmfdistdir}/source/latex/changepage/changepage.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
