Name:		compat-srpm-macros
Version:	2023.11
Release:	3
Summary:	RPM macros for compatible building
Group:		Applications/Engineering
License:	MIT License
Source0:	macros.compat_srpm
Source1: LICENSE
BuildArch:	noarch

%description
macros.compat-srpm provides macros for building projects from
various distributions compatibly.

%prep

%build

%install
cp %{SOURCE1} LICENSE
rm -rf $RPM_BUILD_ROOT
install -Dm644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/macros.d/macros.compat_srpm
   
%clean 
rm -rf $RPM_BUILD_ROOT

%files
%doc LICENSE
%{_rpmconfigdir}/macros.d/macros.compat_srpm

%changelog
* Sun Nov 05 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2023.11
- Initial package
