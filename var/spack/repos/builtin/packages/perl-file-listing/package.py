# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlFileListing(PerlPackage):
    """Parse directory listing"""

    homepage = "https://metacpan.org/pod/File::Listing"
    url = "https://cpan.metacpan.org/authors/id/G/GA/GAAS/File-Listing-6.04.tar.gz"

    license("GPL-1.0-or-later OR Artistic-1.0-Perl")

    version("6.04", sha256="1e0050fcd6789a2179ec0db282bf1e90fb92be35d1171588bd9c47d52d959cf5")

    provides("perl-file-listing-apache")
    provides("perl-file-listing-dosftp")
    provides("perl-file-listing-netware")
    provides("perl-file-listing-unix")
    provides("perl-file-listing-vms")
    depends_on("perl@5.6:", type=("build", "run", "test"))
    depends_on("perl-extutils-makemaker", type="build")
    depends_on("perl-http-date", type="run")
