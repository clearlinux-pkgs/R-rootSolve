#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rootSolve
Version  : 1.8.2.1
Release  : 31
URL      : https://cran.r-project.org/src/contrib/rootSolve_1.8.2.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rootSolve_1.8.2.1.tar.gz
Summary  : Nonlinear Root Finding, Equilibrium and Steady-State Analysis of
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-rootSolve-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-rootSolve package.
Group: Libraries

%description lib
lib components for the R-rootSolve package.


%prep
%setup -q -c -n rootSolve
cd %{_builddir}/rootSolve

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589538756

%install
export SOURCE_DATE_EPOCH=1589538756
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rootSolve
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rootSolve
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rootSolve
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rootSolve || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rootSolve/CITATION
/usr/lib64/R/library/rootSolve/DESCRIPTION
/usr/lib64/R/library/rootSolve/INDEX
/usr/lib64/R/library/rootSolve/Meta/Rd.rds
/usr/lib64/R/library/rootSolve/Meta/demo.rds
/usr/lib64/R/library/rootSolve/Meta/features.rds
/usr/lib64/R/library/rootSolve/Meta/hsearch.rds
/usr/lib64/R/library/rootSolve/Meta/links.rds
/usr/lib64/R/library/rootSolve/Meta/nsInfo.rds
/usr/lib64/R/library/rootSolve/Meta/package.rds
/usr/lib64/R/library/rootSolve/Meta/vignette.rds
/usr/lib64/R/library/rootSolve/NAMESPACE
/usr/lib64/R/library/rootSolve/R/rootSolve
/usr/lib64/R/library/rootSolve/R/rootSolve.rdb
/usr/lib64/R/library/rootSolve/R/rootSolve.rdx
/usr/lib64/R/library/rootSolve/demo/Jacobandroots.R
/usr/lib64/R/library/rootSolve/demo/Steadystate.R
/usr/lib64/R/library/rootSolve/doc/index.html
/usr/lib64/R/library/rootSolve/doc/rootSolve.R
/usr/lib64/R/library/rootSolve/doc/rootSolve.Rnw
/usr/lib64/R/library/rootSolve/doc/rootSolve.pdf
/usr/lib64/R/library/rootSolve/doc/vignettes.bib
/usr/lib64/R/library/rootSolve/dynload/anoxmod.R
/usr/lib64/R/library/rootSolve/dynload/anoxmod.f
/usr/lib64/R/library/rootSolve/dynload/anoxmodc.c
/usr/lib64/R/library/rootSolve/help/AnIndex
/usr/lib64/R/library/rootSolve/help/aliases.rds
/usr/lib64/R/library/rootSolve/help/paths.rds
/usr/lib64/R/library/rootSolve/help/rootSolve.rdb
/usr/lib64/R/library/rootSolve/help/rootSolve.rdx
/usr/lib64/R/library/rootSolve/html/00Index.html
/usr/lib64/R/library/rootSolve/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rootSolve/libs/rootSolve.so
/usr/lib64/R/library/rootSolve/libs/rootSolve.so.avx2
/usr/lib64/R/library/rootSolve/libs/rootSolve.so.avx512
