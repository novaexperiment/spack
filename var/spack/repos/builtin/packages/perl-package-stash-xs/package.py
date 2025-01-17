# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlPackageStashXs(PerlPackage):
    """Faster and more correct implementation of the Package::Stash API"""

    homepage = "https://metacpan.org/pod/Package::Stash::XS"
    url = "https://cpan.metacpan.org/authors/id/D/DO/DOY/Package-Stash-XS-0.28.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("0.28", sha256="23d8c5c25768ef1dc0ce53b975796762df0d6e244445d06e48d794886c32d486")
    depends_on("perl-test-fatal", type=("build", "test"))
    depends_on("perl@5.8.1:", type=("build", "run", "test"))
    depends_on("perl-extutils-makemaker", type=("build", "test"))
    depends_on("perl-scalar-util", type=("build", "test"))
    depends_on("perl-test-needs", type=("build", "test"))
    depends_on("perl-test-requires", type=("build", "test"))
