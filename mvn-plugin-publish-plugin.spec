#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-plugin-publish-plugin
Version  : 1
Release  : 1
URL      : https://plugins.gradle.org/m2/com/gradle/publish/plugin-publish-plugin/0.10.0/plugin-publish-plugin-0.10.0.jar
Source0  : https://plugins.gradle.org/m2/com/gradle/publish/plugin-publish-plugin/0.10.0/plugin-publish-plugin-0.10.0.jar
Source1  : https://plugins.gradle.org/m2/com/gradle/publish/plugin-publish-plugin/0.10.0/plugin-publish-plugin-0.10.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-plugin-publish-plugin-data = %{version}-%{release}
Requires: mvn-plugin-publish-plugin-license = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-plugin-publish-plugin package.
Group: Data

%description data
data components for the mvn-plugin-publish-plugin package.


%package license
Summary: license components for the mvn-plugin-publish-plugin package.
Group: Default

%description license
license components for the mvn-plugin-publish-plugin package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-plugin-publish-plugin
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-plugin-publish-plugin/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/gradle/publish/plugin-publish-plugin/0.10.0
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/com/gradle/publish/plugin-publish-plugin/0.10.0/plugin-publish-plugin-0.10.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/gradle/publish/plugin-publish-plugin/0.10.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/gradle/publish/plugin-publish-plugin/0.10.0/plugin-publish-plugin-0.10.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/gradle/publish/plugin-publish-plugin/0.10.0/plugin-publish-plugin-0.10.0.jar
/usr/share/java/.m2/repository/com/gradle/publish/plugin-publish-plugin/0.10.0/plugin-publish-plugin-0.10.0.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-plugin-publish-plugin/LICENSE.txt
