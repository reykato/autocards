from algorithm import get_next_interval as spacing

def main():
    print(spacing(1, 60, 12) == 60)
    print(spacing(1, 12181, 0) == 60)
    print(spacing(1, 4323, 999999) == 60)
    print(spacing(1, 0, 436346) == 60)
    
    print(spacing(2, 60, 360) == 360)
    print(spacing(2, 12181, 0) == 12181 + 35)
    print(spacing(2, 4323, 999999) == 4323 + 35)
    print(spacing(2, 0, 436346) == 360)
    
    print(spacing(3, 60, 12))
    print(spacing(3, 12181, 0))
    print(spacing(3, 4323, 999999))
    print(spacing(3, 0, 436346))

    

if __name__ == '__main__':
    main()
