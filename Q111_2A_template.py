#!/usr/bin/env python3
# ธนธรณ์ บุญเชิด
# 640510658
# Quiz2 1/64
# Problem 2A
# 204111 Sec 002

def splice(rna,start,stop,mode='alpha'):
    if mode =='alpha':
        s1 = stop + 1
        #print(s1)
        del rna[start:s1]
        #print(rna)
    if mode == 'beta':
        d = []
        k = 0
        s1 = stop + 1
        for i in rna:
            if k>= start and k<=stop:
                d.append(i)
            k = k + 1
        #print(d)
        del rna[start:s1]
        for i in d:
            rna.insert(start,i)
    if mode == 'gamma':
        d = []
        k = 0
        s1 = stop + 1
        for i in rna:
            if k>= start and k<=stop:
                d.append(i)
            k = k + 1
        #print(d)
        v1 = len(d)
        #print(v1)
        l = v1 // 2
        #print(l)
        #d[0],d[1]=d[1],d[0]
        for lias in range(l):
            rna[start],rna[start+1]=rna[start+1],rna[start]
            start = start + 2
            #print(rna)
    return rna

def main():
    rna = ['A','G','A','G','U','C','U','C']
    print(splice(rna,0,6,mode='gamma'))
    print(rna)
    
if __name__ == '__main__':
    main()
