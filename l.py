    price = []
    try :
        price.append(results.find("span", {"class":"a-offscreen"}).text) 
    except :
        print("n/a")
    for error in price :
        if error == "n/a" :
            continue
    
    
    real_price = []
    try :
        real_price.append(results.find("span", {"class":"a-price a-text-price"}).text)
    except :
        print("n/a")
    for error in real_price :
        if error == "n/a" :
            continue
    
    delivery_price = []
    try :
        delivery_price.append(results.find("div", {"class":"a-row a-size-base a-color-secondary s-align-children-center"}).text)
    except :
        print("n/a")
    for error in real_price :
        if error == "n/a" :
            continue

    rating = []
    try :
        rating.append(results.find("div",{"class":"a-row a-size-small"}).text)   
    except :
        print("n/a")
    for error in rating :
        if error == "n/a" :
            continue



        
    for prix in result :
    price = []
    try :
        price.append(prix.find("span", {"class":"a-offscreen"}).text) 
    except :
        print("n/a")
    

for re_prix in result :

    real_price = []
    try :
        real_price.append(re_prix.find("span", {"class":"a-price a-text-price"}).text)
    except :
        print("n/a")   
    


for d_prix in result :

    delivery_price = []
    try :
        delivery_price.append(d_prix.find("div", {"class":"a-row a-size-base a-color-secondary s-align-children-center"}).text)
    except :
        print("n/a")