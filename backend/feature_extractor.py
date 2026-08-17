from urllib.parse import urlparse
import re
import tldextract


def extract_basic_features(url):

    parsed = urlparse(url)

    domain = parsed.netloc
    path = parsed.path

    features = {}

    features["URLLength"] = len(url)

    features["DomainLength"] = len(domain)

    features["PathLength"] = len(path)

    features["SubDomains"] = max(
        len(tldextract.extract(url).subdomain.split(".")) - 1,
        0
    )

    features["Symbol@"] = 1 if "@" in url else 0

    features["Redirecting//"] = 1 if "//" in urlparse(url).path else 0

    features["HTTPS"] = 1 if parsed.scheme == "https" else 0

    features["UsingIP"] = 1 if re.match(
        r"^(?:https?://)?(?:\d{1,3}\.){3}\d{1,3}",
        url
    ) else 0

    return features