%define         realname Bucardo
Summary:	PgSQL replication system for both multi-master and multi-slave operations
Summary(pl.UTF-8):	System replikacji dla PgSQL wspierający multi-master i multi-slave
Name:		bucardo
Version:	4.4.0
Release:	0.1
License:	BSD
Group:		Applications/Databases
URL:		http://bucardo.org/
Source0:	http://bucardo.org/downloads/%{realname}-%{version}.tar.gz
BuildRequires:	perl(DBD::Pg)
BuildRequires:	perl(DBI)
BuildRequires:	perl(DBIx::Safe)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(Net::SMTP)
BuildRequires:	perl(Sys::Hostname)
BuildRequires:	perl(Sys::Syslog)
BuildRequires:	rpm-perlprov
Requires:	perl(DBD::Pg)
Requires:	perl(DBI)
Requires:	perl(DBIx::Safe)
Requires:	postgresql-module-plperl
Requires:	postgresql-module-plpgsql
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
#testsuite
Requires:	perl(Test::Harness)
Requires:	perl(Test::More)
Requires:	perl(Test::Simple)

%description
Bucardo is an asynchronous PostgreSQL replication system, allowing for
both multi-master and multi-slave operations. It was developed at
Backcountry.com primarily by Greg Sabino Mullane of End Point
Corporation.

%description -l pl.UTF-8
Bucardo jest systemem asynchronicznej replikacji PostgreSQL,
pozwalającym na replikację multi-master jak i master-slave. Został
on stworzony w Backcountry.com głównie przez Grega Sabino Mullane z
End Point Corporation

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_localstatedir}/run/%{name}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc bucardo_ctl.html Bucardo.pm.html bucardo.schema Changes
%doc INSTALL LICENSE README SIGNATURE TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*
%attr(755,root,root) %{_bindir}/%{name}_ctl
%{_datadir}/%{name}/%{name}.schema
%{_mandir}/man1/%{name}_ctl.1pm*
%dir %{_localstatedir}/run/%{name}
%dir %{_datadir}/%{name}/
