Name:           hola
Version:        1.0
Release:        1%{?dist}
Summary:        Un simple programa Hola Mundo

License:        GPL
URL:            http://ejemplo.com
Source0:        %{name}.c

BuildRequires:  gcc
BuildRequires:  make

%description
Un programa simple que imprime "¡Hola Mundo!" en la consola.

%prep
cp %{SOURCE0} .

%build
gcc -o hola hola.c

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 hola %{buildroot}%{_bindir}/hola

%files
%{_bindir}/hola

%changelog
* Wed Nov 20 2024 Usuario <mguazzardo76@gmail.com> - 1.0-1
- Primera versión del paquete
