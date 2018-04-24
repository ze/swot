from typing import TypeVar, List, FrozenSet
from os.path import isfile
import sys

__all__ = ["is_academic", "get_school_names"]

# blacklisted domains.
BLACKLIST = frozenset([
    "si.edu",
    "america.edu",
    "californiacolleges.edu",
    "australia.edu",
    "cet.edu"
])

# top level domains that we know are academic.
TLDS = frozenset([
    "ac.ae",
    "ac.at",
    "ac.bd",
    "ac.be",
    "ac.cn",
    "ac.cr",
    "ac.cy",
    "ac.fj",
    "ac.gg",
    "ac.gn",
    "ac.id",
    "ac.il",
    "ac.in",
    "ac.ir",
    "ac.jp",
    "ac.ke",
    "ac.kr",
    "ac.ma",
    "ac.me",
    "ac.mu",
    "ac.mw",
    "ac.mz",
    "ac.ni",
    "ac.nz",
    "ac.om",
    "ac.pa",
    "ac.pg",
    "ac.pr",
    "ac.rs",
    "ac.ru",
    "ac.rw",
    "ac.sz",
    "ac.th",
    "ac.tz",
    "ac.ug",
    "ac.uk",
    "ac.yu",
    "ac.za",
    "ac.zm",
    "ac.zw",
    "ed.ao",
    "ed.cr",
    "ed.jp",
    "edu",
    "edu.af",
    "edu.al",
    "edu.ar",
    "edu.au",
    "edu.az",
    "edu.ba",
    "edu.bb",
    "edu.bd",
    "edu.bh",
    "edu.bi",
    "edu.bn",
    "edu.bo",
    "edu.br",
    "edu.bs",
    "edu.bt",
    "edu.bz",
    "edu.ck",
    "edu.cn",
    "edu.co",
    "edu.cu",
    "edu.do",
    "edu.dz",
    "edu.ec",
    "edu.ee",
    "edu.eg",
    "edu.er",
    "edu.es",
    "edu.et",
    "edu.ge",
    "edu.gh",
    "edu.gr",
    "edu.gt",
    "edu.hk",
    "edu.hn",
    "edu.ht",
    "edu.in",
    "edu.iq",
    "edu.jm",
    "edu.jo",
    "edu.kg",
    "edu.kh",
    "edu.kn",
    "edu.kw",
    "edu.ky",
    "edu.kz",
    "edu.la",
    "edu.lb",
    "edu.lr",
    "edu.lv",
    "edu.ly",
    "edu.me",
    "edu.mg",
    "edu.mk",
    "edu.ml",
    "edu.mm",
    "edu.mn",
    "edu.mo",
    "edu.mt",
    "edu.mv",
    "edu.mw",
    "edu.mx",
    "edu.my",
    "edu.ni",
    "edu.np",
    "edu.om",
    "edu.pa",
    "edu.pe",
    "edu.ph",
    "edu.pk",
    "edu.pl",
    "edu.pr",
    "edu.ps",
    "edu.pt",
    "edu.pw",
    "edu.py",
    "edu.qa",
    "edu.rs",
    "edu.ru",
    "edu.sa",
    "edu.sc",
    "edu.sd",
    "edu.sg",
    "edu.sh",
    "edu.sl",
    "edu.sv",
    "edu.sy",
    "edu.tr",
    "edu.tt",
    "edu.tw",
    "edu.ua",
    "edu.uy",
    "edu.ve",
    "edu.vn",
    "edu.ws",
    "edu.ye",
    "edu.zm",
    "es.kr",
    "g12.br",
    "hs.kr",
    "ms.kr",
    "sc.kr",
    "sc.ug",
    "sch.ae",
    "sch.gg",
    "sch.id",
    "sch.ir",
    "sch.je",
    "sch.jo",
    "sch.lk",
    "sch.ly",
    "sch.my",
    "sch.om",
    "sch.ps",
    "sch.sa",
    "sch.uk",
    "school.nz",
    "school.za",
    "vic.edu.au"
])

def is_academic(email_or_domain: str) -> bool:
    """Identify whether an email or domain is academic."""

    parts = get_domain_parts(email_or_domain)
    return not is_blacklisted(parts) and (is_under_tld(parts) or len(get_school_names(parts)) > 0)

def is_blacklisted(parts: List[str]) -> bool:
    """Check if email or domain is blacklisted."""

    return check_parts(BLACKLIST, parts)

def is_under_tld(parts: List[str]) -> bool:
    """Check if email or domain is registered under a top level domain."""

    return check_parts(TLDS, parts)

Parts = TypeVar("Parts", str, List[str])

def get_school_names(domain: Parts) -> List[str]:
    """Get all school names registered under domain."""

    if isinstance(domain, str):
        return get_school_names(get_domain_parts(domain))

    base_path = "lib/domains"
    path = base_path

    for part in domain:
        path += f"/{part}"
        text_form = f"{path}.txt"

        if not isfile(text_form):
            continue

        with open(text_form) as school:
            return [names.strip() for names in school]

    return []

def get_domain_parts(email_or_domain: str) -> List[str]:
    """Remove all unnecessary information from an email or domain."""

    clean = email_or_domain.strip().lower()
    return clean.split("@", 1)[-1].split("://", 1)[-1].split(":")[0].split(".")[::-1]

def check_parts(search: FrozenSet[str], parts: List[str]) -> bool:
    """Check if domain information is held in any specific set."""

    slow_join = ""
    for part in parts:
        slow_join = part + slow_join
        if slow_join in search:
            return True
        slow_join = "." + slow_join

    return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(is_academic(sys.argv[1]))
    else:
        print("Error: no email or domain provided.")