import itertools

from requests import get


class GetScanTargets:

    def __init__(self):
        self.url = (
            "https://raw.githubusercontent.com/"
            "projectdiscovery/public-bugbounty-programs/"
            "refs/heads/main/chaos-bugbounty-list.json"
        )

    def _get_domains(self) -> list:
        res = get(self.url)
        if not res.ok:
            return []
        _domains = [
            i.get("domains", []) for i in res.json().get("programs", {})
        ]  # noqa
        return list(itertools.chain(*_domains))

    @property
    def domains(self) -> set:
        try:
            _domains = self._get_domains()
            _domains.sort()
            return set(_domains)
        except Exception:
            return set()
