#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	TableExtract
Summary:	HTML::TableExtract - extracting the text contained in HTML tables
Summary(pl):	HTML::TableExtract - wyci±ganie tekstu zawartego w tabelach HTML
Name:		perl-HTML-TableExtract
Version:	2.10
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e6e355f6049dc57706e719c5ce61ff39
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-HTML-Parser
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::TableExtract is a subclass of HTML::Parser that serves to
extract the textual information from tables of interest contained
within an HTML document. The text from each extracted table is stored
in tabe state objects which hold the information as an array of arrays
that represent the rows and cells of that table.

%description -l pl
HTML::TableExtract to podklasa HTML::Parser, która s³u¿y do wyci±gania
informacji tekstowych z tabel w dokumencie HTML. Tekst z ka¿dej tabeli
jest zapisywany w obiektach, które przechowuj± informacje jako tablicê
tablic, reprezentuj±c± wiersze i komórki tabeli.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
