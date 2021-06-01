from helpers.browser import check_sites
from dsl import all_sources

def run():
    """check masterlist of hardcoded websites for product availablity"""
    check_sites(all_sources)


if __name__ == "__main__":
    run()