Summary:	Tool to inject shared libraries into running processes
Summary(pl.UTF-8):	-
Name:		injectso
Version:	0.2.1
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	http://www.securereality.com.au/archives/%{name}-%{version}.tar.gz
# Source0-md5:	a6d775a9b3ef890e2259b03e898def9c
URL:		-
BuildRequires:	autoconf
ExclusiveArch:	%{ix86} sparc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool to inject shared libraries into running processes.

%description -l pl.UTF-8

%prep
%setup -q -n %{name}-0.2

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install injectso $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.html README.txt TODO
%attr(755,root,root) %{_bindir}/injectso
