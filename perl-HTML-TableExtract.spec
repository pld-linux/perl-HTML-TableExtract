#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	TableExtract
Summary:	HTML::TableExtract - extracting the text contained in HTML tables
Summary(pl):	HTML::TableExtract - wyci±ganie tekstu zawartego w tabelach HTML
Name:		perl-HTML-TableExtract
Version:	1.08
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-HTML-Parser
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-26
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
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
