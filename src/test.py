import validation


def main():
    print(validation.clean_domain("0.0.0.0:8743"))
    print(validation.clean_domain("www.python.org"))
