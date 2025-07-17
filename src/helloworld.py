import logging

formatstring = "%(asctime)s %(message)s"
fo = logging.Formatter(formatstring)
sh = logging.StreamHandler()
sh.setFormatter(fo)
l = logging.getLogger(__name__)
l.setLevel(logging.DEBUG)
l.addHandler(sh)

def helloworld():
    """Stub function to set up environment"""
    print(f"Hello World.")
    l.debug("JWTO")
    return 5



if __name__ == "__main__":
    helloworld()



