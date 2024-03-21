# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlPackageStash(PerlPackage):
    """Routines for manipulating stashes"""

    homepage = "https://metacpan.org/pod/Package::Stash"
    url = "https://cpan.metacpan.org/authors/id/D/DO/DOY/Package-Stash-0.37.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("0.37", sha256="06ab05388f9130cd377c0e1d3e3bafeed6ef6a1e22104571a9e1d7bfac787b2c")

    provides("perl-package-stash-pp")
    depends_on("perl-package-stash-xs@0.26:", type="run")
    depends_on("perl-dist-checkconflicts@0.2:", type="run")
    depends_on("perl-extutils-makemaker", type=("build", "test"))
    depends_on("perl-test-needs", type=("build", "test"))
    depends_on("perl@5.8.1:", type=("build", "run", "test"))
    depends_on("perl-test-fatal", type=("build", "test"))
    depends_on("perl-module-implementation@0.6:", type="run")
    depends_on("perl-scalar-util", type="run")
    depends_on("perl-cpan-meta-check@0.11:", type=("build", "test"))
