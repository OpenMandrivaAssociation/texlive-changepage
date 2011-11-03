# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/changepage
# catalog-date 2009-11-09 14:16:05 +0100
# catalog-license lppl1.3
# catalog-version 1.0c
Name:		texlive-changepage
Version:	1.0c
Release:	1
Summary:	Margin adjustment and detection of odd/even pages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/changepage
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changepage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changepage.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/changepage.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package provides commands to change the page layout in the
middle of a document, and to robustly check for typesetting on
odd or even pages. Instructions for use are at the end of the
file. The package is an extraction of code from the memoir
class, whose user interface it shares. It is intended the this
package will eventually replace the chngpage package, which is
distributed with the package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
