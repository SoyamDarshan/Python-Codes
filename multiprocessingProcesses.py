from multiprocessing import Pool

def job(num):
    return num + 2

if __name__ == '__main__':
    p=Pool(processes=20)
    data = p.map(job,[4])
    p.close()
    print(data)