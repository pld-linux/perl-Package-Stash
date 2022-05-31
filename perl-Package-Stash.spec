#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Package
%define		pnam	Stash
Summary:	Package::Stash - routines for manipulating stashes
Summary(pl.UTF-8):	Package::Stash - funkcje do manipulowania tablicami symboli
Name:		perl-Package-Stash
Version:	0.40
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Package/Package-Stash-%{version}.tar.gz
# Source0-md5:	7a2922941cc2aad6a52642e4fb13d07b
URL:		https://metacpan.org/release/Package-Stash
BuildRequires:	perl-Dist-CheckConflicts >= 0.02
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.31
BuildRequires:	perl-devel >= 1:5.8.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Module-Implementation >= 0.06
BuildRequires:	perl-Package-Stash-XS >= 0.26
BuildRequires:	perl-Package-DeprecationManager
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Requires
BuildRequires:	perl-Test-Simple >= 0.88
%endif
Suggests:	perl-Package-Stash-XS >= 0.26
Conflicts:	perl-Class-MOP <= 1.08
Conflicts:	perl-MooseX-Method-Signatures <= 0.36
Conflicts:	perl-MooseX-Role-WithOverloading <= 0.08
Conflicts:	perl-namespace-clean <= 0.18
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Manipulating stashes (Perl's symbol tables) is occasionally necessary,
but incredibly messy, and easy to get wrong. This module hides all of
that behind a simple API.

%description -l pl.UTF-8
Manipulowanie stashami (perlowymi tablicami symboli) jest czasem
niezbędne, ale bardzo zawiłe i błędogenne. Ten moduł ukrywa wszystko w
prostym API.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

# already handled by rpm Conflicts - don't generate Dist::CheckConflicts dep
%{__rm} $RPM_BUILD_ROOT%{_bindir}/package-stash-conflicts \
	$RPM_BUILD_ROOT%{perl_vendorlib}/Package/Stash/Conflicts.pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Package/Stash.pm
%{perl_vendorlib}/Package/Stash
%{_mandir}/man3/Package::Stash*.3pm*
