%define pkgname progressbar
Summary:	Text progress bar library for Ruby
Summary(pl.UTF-8):	Biblioteka tekstowego paska postępu dla języka Ruby
Name:		ruby-%{pkgname}
Version:	0.11.0
Release:	2
License:	Ruby License
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	b0aeb7f9bb4b6c5562582a009132c285
URL:		https://github.com/peleteiro/progressbar
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby/ProgressBar is a text progress bar library for Ruby. It can
indicate progress with percentage, a progress bar, and estimated
remaining time.

%description -l pl.UTF-8
Ruby/ProgressBar to biblioteka tekstowego paska postępu dla języka
Ruby. Potrafi podawać postęp przy użyciu procentów, paska postępu oraz
estymacji czasu pozostałego do zakończenia.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML do biblioteki %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML do biblioteki %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri do biblioteki %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacja w formacie ri do biblioteki %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
%{__rm} ri/created.rid
%{__rm} ri/cache.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_ridir},%{ruby_rdocdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.rdoc
%{ruby_vendorlibdir}/progressbar.rb

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/ProgressBar
%{ruby_ridir}/ReversedProgressBar
