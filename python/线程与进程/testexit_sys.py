# Author: Jason Lu
def later():
    import sys
    print('Bye sys world')
    try:
        sys.exit(42)
        print('Never reached')
    except SystemExit:
        print('Ignored...')
    finally:
        print('Cleanup')

if __name__ == '__main__': later()