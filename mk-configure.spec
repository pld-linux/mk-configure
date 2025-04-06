Summary:	Build system written in and for bmake and UNIX tools
Summary(pl.UTF-8):	System budowania napisany w i do użycia z bmake i narzędziami uniksowymi
Name:		mk-configure
Version:	0.40.0
Release:	1
License:	BSD
Group:		Development/Tools
Source0:	https://downloads.sourceforge.net/mk-configure/%{name}-%{version}.tar.gz
# Source0-md5:	25f7db282a7e2ae925d42b085b6878c5
URL:		https://sourceforge.net/projects/mk-configure/
BuildRequires:	bmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
# configuration is stored in .mk files
# (alternatively all users can export MKCOMPILERSETTINGS=yes to rebuild compiler settings in HOME)
%requires_eq	gcc
%requires_eq	gcc-c++
Requires:	bmake
Requires:	mk-files
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# not noarch due to stored compiler configuration...
%define		_enable_debug_packages	0

%description
mk-configure is a build system, written in and for bmake (portable
version of NetBSD make) and UNIX tools (shell, awk etc.).

mk-configure provides a number of include files (.mk files) written in
bmake and a number of standalone programs that should be installed to
user's host for building a software.

Features:
- an easy way for building standalone executables, static and shared
  libraries written in C, C++ and Objective C; .cat and .html files
  from man pages; .info pages from texinfo sources etc.
- installing and uninstalling executables, libraries, scripts,
  documentation files and others; DESTDIR support is also provided
- autoconf-like support for finding #include files, libraries and
  function implementation, function definitions, defines, types,
  struct members etc.
- a number of built-in checks for, e.g., system endianness, GNU bison,
  GNU flex programs and many others
- automatic dependency analysis built-in for C and C++
- extensibility by writing bmake include files
- support for regression tests
- mk-configure is small and easy

%description -l pl.UTF-8
mk-configure to system budowania, napisany w i dla bmake'a (przenośnej
wersji programu make z NetBSD) oraz narzędzi uniksowych (powłoki, awk
itp.).

mk-configure dostarcza pewną liczbę dołączanych plików (.mk),
napisanych w bmake'u i programów samodzielnych, które powinny być
zainstalowane do budowania oprogramowania.

Możliwości:
- łatwy sposób budowania samodzielnych programów, bibliotek
  statycznych i współdzielonych napisanych w C, C++ i Objective C;
  plików .cat i .html ze stron man; stron .info ze źródeł texinfo itp.
- instalowanie i odinstalowywanie binariów, bibliotek, skryptów,
  plików dokumentacji i innych; dostępna jest obsługa DESTDIR
- podobna do autoconfa obsługa znajdowania plików #include, bibliotek
  i implementacji funkcji, definicji funkcji, makr, typów, składowych
  struktur itp.
- wiele wbudowanych sprawdzeń, np. kolejności bajtów w systemie,
  programów GNU bison czy GNU flex i wielu innych
- wbudowana automatyczna analiza zależności dla C i C++
- rozszerzalny poprzez pisanie dołączanych plików bmake'a
- obsługa testów regresji
- jest mały i łatwy w użyciu

%prep
%setup -q

%define	set_env \
	export PREFIX=%{_prefix}; \
	export LIBEXECDIR=%{_libexecdir}; \
	export MANDIR=%{_mandir}; \
	export SYSCONFDIR=%{_sysconfdir}; \
	export USE_AWK=/bin/awk; \
	export USE_INSTALL=/usr/bin/install; \
	export USE_CC_COMPILERS="%{__cc}"; \
	export USE_CXX_COMPILERS="%{__cxx}"

%build
%{set_env}
bmake %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

%{set_env}
bmake install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/mk-configure

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md doc/{FAQ,LICENSE,NEWS,NOTES,TODO}
%attr(755,root,root) %{_bindir}/mkc_check_*
%attr(755,root,root) %{_bindir}/mkc_compiler_settings
%attr(755,root,root) %{_bindir}/mkc_install
%attr(755,root,root) %{_bindir}/mkc_which
%attr(755,root,root) %{_bindir}/mkcmake
%dir %{_libexecdir}/mk-configure
%{_libexecdir}/mk-configure/mkc_check_common.sh
%attr(755,root,root) %{_libexecdir}/mk-configure/mkc_get_deps
%dir %{_datadir}/mk-configure
%dir %{_datadir}/mk-configure/builtins
%{_datadir}/mk-configure/builtins/*.c
%{_datadir}/mk-configure/builtins/*.cc
%attr(755,root,root) %{_datadir}/mk-configure/builtins/endianness
%attr(755,root,root) %{_datadir}/mk-configure/builtins/prog_*
%{_datadir}/mk-configure/features
%{_datadir}/mk-configure/mk
%{_mandir}/man1/mkc_check_*.1*
%{_mandir}/man1/mkc_compiler_settings.1*
%{_mandir}/man1/mkc_install.1*
%{_mandir}/man1/mkc_which.1*
%{_mandir}/man1/mkcmake.1*
%{_mandir}/man7/mk-configure.7*
