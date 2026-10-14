def domain(domain: str) -> str:
    # Handle incorrect stuff.
    # Like incorrect usage of ., or invalid characters
    # Maybe check DNS records of domain to make sure it is valid?
    return domain


def path(path: str) -> str:
    # Handle incorrect stuff.
    # Make sure it has the right structure, check if path starts with / or not,
    # valid characters, and all invalid characters are url encoded
    return path
