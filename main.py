def main():
    result = []
    for i in range(1, 16):
        if i % 3 == 0 and i % 5 == 0:
            result.append('bizzbuzz')
        elif i % 3 == 0:
            result.append('bizz')
        elif i % 5 == 0:
            result.append('buzz')
        else:
            result.append(i) 
    print(result)    



if __name__ == "__main__":
    main()

