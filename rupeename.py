ones={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    "0":""    
}
tens={
    "1":"Ten",
    "2":"Twenty",
    "3":"Thirty",
    "4":"Fourty",
    "5":"Fifty",
    "6":"Sixty",
    "7":"Seventy",
    "8":"Eighty",
    "9":"Ninety",
    "0":""    
}
below_ten={
    "11":"Eleven",
    "12":"Twelve",
    "13":"Thirteen",
    "14":"Fourteen",
    "15":"Fifteen",
    "16":"Sixteen",
    "17":"Seventeen",
    "18":"Eighteen",
    "19":"Nineteen"
}
n=int(input("Enter the amount you want to convert into text:"))#1000
nu=[*str(n)]#["1","0","0","0"]
maxi=""
l=len(nu)
def grouping(x:list):
    a=len(nu)
    if a==1:
        o=x[-2:][-1]
        t="0"
        h="0"
        th="0"
        tth="0"
        l="0"
        tl="0"
        c="0"
        ct="0"
    if a==2:
        o=x[-2:][-1]
        t=x[-3:][-2]
        h="0"
        th="0"
        tth="0"
        l="0"
        tl="0"
        c="0"
        ct="0"
    if a==3:
        o=x[-2:][-1]
        t=x[-3:][-2]
        h=x[-4:][-3]
        th="0"
        tth="0"
        l="0"
        tl="0"
        c="0"
        ct="0"
    if a==4:
        o=x[-2:][-1]
        t=x[-3:][-2]
        h=x[-4:][-3]
        th=x[-5:][-4]
        tth="0"
        l="0"
        tl="0"
        c="0"
        ct="0"
    if a==5:
        o=x[-2:][-1]
        t=x[-3:][-2]
        h=x[-4:][-3]
        th=x[-5:][-4]
        tth=x[-6:][-5]
        l="0"
        tl="0"
        c="0"
        ct="0"
    if a==6:
        o=x[-2:][-1]
        t=x[-3:][-2]
        h=x[-4:][-3]
        th=x[-5:][-4]
        tth=x[-6:][-5]
        l=x[-7:][-6]
        tl="0"
        c="0"
        ct="0"
    if a==7:
        o=x[-2:][-1]
        t=x[-3:][-2]
        h=x[-4:][-3]
        th=x[-5:][-4]
        tth=x[-6:][-5]
        l=x[-7:][-6]
        tl=x[-8:][-7] 
        c="0"
        ct="0"
    if a==8:
        o=x[-2:][-1]
        t=x[-3:][-2]
        h=x[-4:][-3]
        th=x[-5:][-4]
        tth=x[-6:][-5]
        l=x[-7:][-6]
        tl=x[-8:][-7]
        c=x[-9:][-8]
        ct="0"
    if a==9:
        o=x[-2:][-1]
        t=x[-3:][-2]
        h=x[-4:][-3]
        th=x[-5:][-4]
        tth=x[-6:][-5]
        l=x[-7:][-6]
        tl=x[-8:][-7]
        c=x[-9:][-8]
        ct=x[-10:][-9]
    ten=t+o # type: ignore # ignore
    hund=h # type: ignore # ignore
    tenthou=tth+th # type: ignore # ignore
    tenlakh=tl+l # type: ignore # ignore
    crore=ct+c # type: ignore # ignore
    num=[crore,tenlakh,tenthou,hund,ten]

    return(num)
def co(x:str):
    y=[*x]
    
    text=""
    if int(x)<20 and int(x)>10:
        text=below_ten[x]
    elif int(x)<10 and int(x)>0:
        text=ones[str(int(x))]
    elif int(x)==0:
        tect=ones["0"]
    else:
        o=ones[y[1]]
        t=tens[y[0]]
        text=t+" "+o
    return text

def number(c,l,th,h,o):
    ic=int(c)
    il=int(l)
    ith=int(th)
    ih=int(h)
    io=int(o)
    
    if ic==0 and il==0 and ith==0 and ih==0:
        num=o
    elif ic==0 and il==0 and ith==0 and io!=0:
        num=co(h)+" hundred and "+co(o)
    elif ic==0 and il==0 and io==0 and ith==0:
        num=co(h)+" hundred"
    elif ic==0 and il==0 and io!=0 and ih!=0:
        num=co(th)+" thousand "+co(h)+" hundred and "+co(o)
    elif ic==0 and il==0 and io==0 and ith!=0:
        num=co(th)+" thousand "+co(h)+" hundred"
    elif ic==0 and il==0 and io!=0 and ih==0 and ith!=0:
        num=co(th)+" thousand and "+co(o)
    elif ic==0 and il!=0 and ith!=0 and ih!=0 and io!=0:#lakhs
        num=co(l)+" lakh "+co(th)+" thousand "+co(h)+" hundred and "+co(o)
    elif ic==0 and il!=0 and ith==0 and ih==0 and io==0:
        num=co(l)+" lakh "
    elif ic==0 and il!=0 and ith!=0 and ih==0 and io==0:
        num=co(l)+" lakh "+co(th)+" thousand "
    elif ic==0 and il!=0 and ith==0 and ih!=0 and io==0:
        num=co(l)+" lakh "+co(h)+" hundred"
    elif ic==0 and il!=0 and ith==0 and ih==0 and io!=0:
        num=co(l)+" lakh "+co(o)
    elif ic==0 and il!=0 and ith!=0 and ih!=0 and io==0:
        num=co(l)+" lakh "+co(th)+" thousand "+co(h)+" hundred"
    elif ic==0 and il!=0 and ith==0 and ih!=0 and io!=0:
        num=co(l)+" lakh "+co(h)+" hundred and "+co(o)
    elif ic==0 and il!=0 and ith!=0 and ih==0 and io!=0:
        num=co(l)+" lakh "+co(th)+" thousand "+co(o)
    elif ic!=0 and il!=0 and ith!=0 and ih!=0 and io!=0:#crore 1
        num=co(c)+" crore "+co(l)+" lakh "+co(th)+" thousand "+co(h)+" hundred and "+co(o)
    elif ic!=0 and il==0 and ith==0 and ih==0 and io==0:#crore 2
        num=co(c)+" crore "
    elif ic!=0 and il!=0 and ith==0 and ih==0 and io==0:#crore 3
        num=co(c)+" crore "+co(l)+" lakh "
    elif ic!=0 and il==0 and ith!=0 and ih==0 and io==0:#crore 4
        num=co(c)+" crore "+co(l)+co(th)+" thousand "
    elif ic!=0 and il==0 and ith==0 and ih!=0 and io==0:#crore 5
        num=co(c)+" crore "+co(h)+" hundred"
    elif ic!=0 and il==0 and ith==0 and ih==0 and io!=0:#crore 6
        num=co(c)+" crore "+co(o)
    elif ic!=0 and il!=0 and ith!=0 and ih==0 and io==0:#crore 7
        num=co(c)+" crore "+co(l)+" lakh "+co(th)+" thousand "
    elif ic!=0 and il==0 and ith==0 and ih!=0 and io!=0:#crore 8
        num=co(c)+" crore "+co(h)+" hundred and "+co(o)
    elif ic!=0 and il!=0 and ith==0 and ih!=0 and io==0:#crore 9
        num=co(c)+" crore "+co(l)+" lakh "+co(h)+" hundred"
    elif ic!=0 and il==0 and ith!=0 and ih==0 and io!=0:#crore 10
        num=co(c)+" crore "+co(th)+" thousand "+co(o)
    elif ic!=0 and il!=0 and ith==0 and ih==0 and io!=0:#crore 11
        num=co(c)+" crore "+co(l)+" lakh "+co(o)
    elif ic!=0 and il==0 and ith!=0 and ih!=0 and io==0:#crore 12
        num=co(c)+" crore "+co(th)+" thousand "+co(h)+" hundred"
    elif ic!=0 and il!=0 and ith!=0 and ih!=0 and io==0:#crore 13
        num=co(c)+" crore "+co(l)+" lakh "+co(th)+" thousand "+co(h)+" hundred"
    elif ic!=0 and il==0 and ith!=0 and ih!=0 and io!=0:#crore 14
        num=co(c)+" crore "+co(th)+" thousand "+co(h)+" hundred and "+co(o)
    elif ic!=0 and il!=0 and ith==0 and ih!=0 and io!=0:#crore 15
        num=co(c)+" crore "+co(l)+" lakh "+co(h)+" hundred and "+co(o)
    elif ic!=0 and il!=0 and ith!=0 and ih==0 and io!=0:#crore 16
        num=co(c)+" crore "+co(l)+" lakh "+co(th)+" thousand "+co(o)

    return(num)# type:ignore


if n<20 and n>10:
    print(f"₹{n} -> Rs.",below_ten[str(n)])
elif n<10 and n>0:
    print(f"₹{n} -> Rs.",(ones[str(n)]))
elif n==0:
    print(f"₹{n} -> Rs.","zero")
else:
    nu=grouping(nu)
    crore= (nu[0])
    lak=(nu[1])
    thousand=(nu[2])
    hundred=(nu[3])
    one=(nu[4])
    print(f"₹{n} -> Rs.",number(crore,lak,thousand,hundred,one))
