%global tl_name catoptions
%global tl_revision 68982

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2.7i
Release:	%{tl_revision}.1
Summary:	Preserving and recalling standard catcodes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/catoptions
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/catoptions.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/catoptions.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package changes package loading internals so that all subsequently
loaded packages can rely on normal/standard catcodes of all ASCII
characters. The package defines canonical control sequences to represent
all the visible ASCII characters. It also provides robust option parsing
mechanisms (XDeclareOption, XExecuteOptions and XProcessOptions, which
will be used by \documentclass if the package has already been loaded).
The package also provides a range of other TeX programming tools.

