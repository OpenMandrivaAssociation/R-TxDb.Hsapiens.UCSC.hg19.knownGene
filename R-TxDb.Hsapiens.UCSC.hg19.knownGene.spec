%global packname  TxDb.Hsapiens.UCSC.hg19.knownGene
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.6.2
Release:          1
Summary:          Annotation package for the Hsapiens_UCSC_hg19_knownGene_TxDb object
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-GenomicFeatures R-AnnotationDbi
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-GenomicFeatures R-AnnotationDbi

%description
Contains the Hsapiens_UCSC_hg19_knownGene_TxDb object annotation database
as generated from UCSC

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
