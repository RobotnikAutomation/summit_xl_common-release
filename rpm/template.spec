Name:           ros-indigo-summit-xl-pad
Version:        1.0.5
Release:        0%{?dist}
Summary:        ROS summit_xl_pad package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/summit_xl_pad
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-diagnostic-updater
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-robotnik-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-twist-mux
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-diagnostic-updater
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-robotnik-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs

%description
The summit_xl_pad package allows to control the summit_xl product range
(summit_xl, summit_xl_omni, x_wam) teleoperation

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Jul 05 2016 Carlos Villar <cvillar@robotnik.es> - 1.0.5-0
- Autogenerated by Bloom

* Thu Jun 30 2016 Carlos Villar <cvillar@robotnik.es> - 1.0.4-0
- Autogenerated by Bloom

* Wed Jun 29 2016 Carlos Villar <cvillar@robotnik.es> - 1.0.3-0
- Autogenerated by Bloom

* Tue Jun 28 2016 Carlos Villar <cvillar@robotnik.es> - 1.0.2-0
- Autogenerated by Bloom

