# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlPpixRegexp(PerlPackage):
    """Parse regular expressions"""

    homepage = "https://metacpan.org/pod/PPIx::Regexp"
    url = "https://cpan.metacpan.org/authors/id/W/WY/WYANT/PPIx-Regexp-0.088.tar.gz"

    maintainers("greenc-FNAL", "EbiArnie", "gartung", "marcmengel", "vito")

    license("Artistic-1.0-Perl OR GPL-1.0-or-later")

    version("0.088", sha256="885433f9b102fad4fd36b21c7320bb036036111caf998131bf416f7cd5ee9764")
    version("0.085", sha256="2ef0bb89248438e0138fc64c9ab0cacd0a532e908882a07dd8f0b841f130cf1d")
    version("0.084_01", sha256="7bb7e2d62a2118be6a6bcf23fddd1e0515650f8578fdb3204d3279536d58dfae")

    provides("perl-ppix-regexp-constant")
    provides("perl-ppix-regexp-dumper")
    provides("perl-ppix-regexp-element")
    provides("perl-ppix-regexp-lexer")
    provides("perl-ppix-regexp-node")
    provides("perl-ppix-regexp-node-range")
    provides("perl-ppix-regexp-node-unknown")
    provides("perl-ppix-regexp-structure")
    provides("perl-ppix-regexp-structure-assertion")
    provides("perl-ppix-regexp-structure-atomic-script-run")
    provides("perl-ppix-regexp-structure-branchreset")
    provides("perl-ppix-regexp-structure-capture")
    provides("perl-ppix-regexp-structure-charclass")
    provides("perl-ppix-regexp-structure-code")
    provides("perl-ppix-regexp-structure-main")
    provides("perl-ppix-regexp-structure-modifier")
    provides("perl-ppix-regexp-structure-namedcapture")
    provides("perl-ppix-regexp-structure-quantifier")
    provides("perl-ppix-regexp-structure-regexset")
    provides("perl-ppix-regexp-structure-regexp")
    provides("perl-ppix-regexp-structure-replacement")
    provides("perl-ppix-regexp-structure-script-run")
    provides("perl-ppix-regexp-structure-subexpression")
    provides("perl-ppix-regexp-structure-switch")
    provides("perl-ppix-regexp-structure-unknown")
    provides("perl-ppix-regexp-support")
    provides("perl-ppix-regexp-token")
    provides("perl-ppix-regexp-token-assertion")
    provides("perl-ppix-regexp-token-backreference")
    provides("perl-ppix-regexp-token-backtrack")
    provides("perl-ppix-regexp-token-charclass")
    provides("perl-ppix-regexp-token-charclass-posix")
    provides("perl-ppix-regexp-token-charclass-posix-unknown")
    provides("perl-ppix-regexp-token-charclass-simple")
    provides("perl-ppix-regexp-token-code")
    provides("perl-ppix-regexp-token-comment")
    provides("perl-ppix-regexp-token-condition")
    provides("perl-ppix-regexp-token-control")
    provides("perl-ppix-regexp-token-delimiter")
    provides("perl-ppix-regexp-token-greediness")
    provides("perl-ppix-regexp-token-grouptype")
    provides("perl-ppix-regexp-token-grouptype-assertion")
    provides("perl-ppix-regexp-token-grouptype-atomic-script-run")
    provides("perl-ppix-regexp-token-grouptype-branchreset")
    provides("perl-ppix-regexp-token-grouptype-code")
    provides("perl-ppix-regexp-token-grouptype-modifier")
    provides("perl-ppix-regexp-token-grouptype-namedcapture")
    provides("perl-ppix-regexp-token-grouptype-script-run")
    provides("perl-ppix-regexp-token-grouptype-subexpression")
    provides("perl-ppix-regexp-token-grouptype-switch")
    provides("perl-ppix-regexp-token-interpolation")
    provides("perl-ppix-regexp-token-literal")
    provides("perl-ppix-regexp-token-modifier")
    provides("perl-ppix-regexp-token-noop")
    provides("perl-ppix-regexp-token-operator")
    provides("perl-ppix-regexp-token-quantifier")
    provides("perl-ppix-regexp-token-recursion")
    provides("perl-ppix-regexp-token-reference")
    provides("perl-ppix-regexp-token-structure")
    provides("perl-ppix-regexp-token-unknown")
    provides("perl-ppix-regexp-token-unmatched")
    provides("perl-ppix-regexp-token-whitespace")
    provides("perl-ppix-regexp-tokenizer")
    provides("perl-ppix-regexp-util")

    depends_on("perl@5.6:", type=("build", "run", "test"))

    depends_on("perl-module-build@0.42:", type="build")

    depends_on("perl-ppi-dumper@1.238:", type=("build", "run", "test"))
    depends_on("perl-ppi-document@1.238:", type=("build", "run", "test"))
    depends_on("perl-scalar-util", type=("build", "run", "test"))
    depends_on("perl-list-util", type=("build", "run", "test"))
    depends_on("perl-task-weaken", type=("build", "run", "test"))
