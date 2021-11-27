import random

#중식 - 리스트, 가격, 칼로리
ChineseFood_list = ['짜장면', '간짜장', '짬뽕', '탕수육', '우동(중)', '울면', '볶음밥', '짬뽕밥', '잡채밥', '군만두', '양장피', '팔보채', '깐풍기', '깐쇼새우', '마라탕']
ChineseFood_price_dictionary = {'짜장면':6000, '간짜장':7000, '짬뽕':7000, '탕수육':20000, '우동(중)':8000, '울면':8000, '볶음밥':7000, '짬뽕밥':7000, '잡채밥':8000, '군만두':5000, '양장피':30000, '팔보채':30000, '깐풍기':19000, '깐쇼새우':25000, '마라탕':10000}
ChineseFood_calory_dictionary = {'짜장면':785, '간짜장':810, '짬뽕':764, '탕수육':1182, '우동(중)':692, '울면':706, '볶음밥':760, '짬뽕밥':482, '잡채밥':673, '군만두':400, '양장피':602, '팔보채':580, '깐풍기':900, '깐쇼새우':706, '마라탕':450}

#일식 - 리스트, 가격, 칼로리
JapaneseFood_list = ['돈까스', '치킨까스', '고구마치즈돈까스', '카레돈까스', '치즈돈까스', '함박스테이크', '냉모밀', '우동(일)', '감자고로케', '밀푀유나베','샤브샤브', '광어초밥', '연어초밥', '모듬초밥']
JapaneseFood_price_dictionary = {'돈까스':8000, '치킨까스':8500, '고구마치즈돈까스':8500, '카레돈까스':8000, '치즈돈까스':8500, '함박스테이크':9000, '냉모밀':7500, '우동(일)':6000, '감자고로케':4500, '밀푀유나베':22000,'샤브샤브':18000, '광어초밥':18000, '연어초밥':16000, '모듬초밥':20000}
JapaneseFood_calory_dictionary = {'돈까스':673, '치킨까스':594, '고구마치즈돈까스':680, '카레돈까스':552, '치즈돈까스':721, '함박스테이크':561, '냉모밀':430, '우동(일)':700, '감자고로케':630, '밀푀유나베':895,'샤브샤브':384, '광어초밥':462, '연어초밥':528, '모듬초밥':557}

#한식 - 리스트, 가격, 칼로리
KoreanFood_list = ['부대찌개', '김치찌개', '된장찌개', '찜닭', '비빔밥', '삼겹살구이', '닭도리탕', '코다리조림', '제육볶음', '순두부찌개' , '청국장', '감자탕', '삼계탕', '냉면', '김치찜', '보쌈', '족발', '돼지국밥', '순대국밥']
KoreanFood_price_dictionary = {'부대찌개':15000, '김치찌개':7000, '된장찌개':7000, '찜닭':20000, '비빔밥':8000, '삼겹살구이':18000, '닭도리탕':35000, '코다리조림':25000, '제육볶음':20000, '순두부찌개':7000 , '청국장':8000, '감자탕':35000, '삼계탕':15000, '냉면':8500, '김치찜':22000, '보쌈':45000, '족발':41000, '돼지국밥':8000, '순대국밥':8000}
KoreanFood_calory_dictionary = {'부대찌개':712, '김치찌개':465, '된장찌개':200, '찜닭':850, '비빔밥':586, '삼겹살구이':699, '닭도리탕':327, '코다리조림':219, '제육볶음':572, '순두부찌개':259 , '청국장':117, '감자탕':151, '삼계탕':900, '냉면':415, '김치찜':550, '보쌈':1162, '족발':916, '돼지국밥':470, '순대국밥':488}
                            
#분식 - 리스트, 가격, 칼로리
FlourbasedFood_list = ['떡볶이', '로제떡볶이','참치마요컵밥', '스팸마요컵밥', '쫄면', '김밥', '오뎅탕', '어묵꼬치', '핫도그', '김말이', '야채튀김', '만두튀김', '순대', '새우튀김', '피카츄']
FlourbasedFood_price_dictionary = {'떡볶이':14000, '로제떡볶이':16000,'참치마요컵밥':3500, '스팸마요컵밥':3500, '쫄면':6000, '김밥':3000, '오뎅탕':6000, '어묵꼬치':2500, '핫도그':1500, '김말이':2000, '야채튀김':1000, '만두튀김':2000, '순대':3000, '새우튀김':2000, '피카츄':1500}
FlourbasedFood_calory_dictionary = {'떡볶이':335, '로제떡볶이':420,'참치마요컵밥':425, '스팸마요컵밥':445, '쫄면':495, '김밥':560, '오뎅탕':140, '어묵꼬치':255, '핫도그':300, '김말이':325, '야채튀김':101, '만두튀김':475, '순대':500, '새우튀김':300, '피카츄':221}

#치킨 - 리스트, 가격, 칼로리
Chicken_list = ['후라이드치킨', '양념치킨', '굽네고추바사삭', '굽네볼케이노','고추마요치킨', '블랙알리오', '슈프림양념치킨', '교촌콤보', '교촌레드콤보', '교촌허니콤보', '알싸한마늘치킨', '자메이카통다리구이','포테킹후라이드', '뿌링클', '맛초킹', '쇼킹핫치킨'] 
Chicken_price_dictionary = {'후라이드치킨':18000, '양념치킨':19000, '굽네고추바사삭':17000, '굽네볼케이노':17000,'고추마요치킨':17900, '블랙알리오':17900, '슈프림양념치킨':18000, '교촌콤보':17000, '교촌레드콤보':18000, '교촌허니콤보':18000, '알싸한마늘치킨':15000, '자메이카통다리구이':19500,'포테킹후라이드':18000, '뿌링클':17000, '맛초킹':17000, '쇼킹핫치킨':18000}
Chicken_calory_dictionary = {'후라이드치킨':1851, '양념치킨':2126, '굽네고추바사삭':1400, '굽네볼케이노':1097,'고추마요치킨':2500, '블랙알리오':2500, '슈프림양념치킨':2700, '교촌콤보':2400, '교촌레드콤보':2400, '교촌허니콤보':2400, '알싸한마늘치킨':2000, '자메이카통다리구이':1400,'포테킹후라이드':2600, '뿌링클':2650, '맛초킹':2500, '쇼킹핫치킨':2000}

#양식 - 리스트, 가격, 칼로리
WesternFood_list = ['까르보나라파스타', '목살필라프', '새우필라프', '토마토파스타', '로제파스타', '알리오올리오파스타', '리조또', '스테이크', '찹스테이크', '감바스', '바베큐폭립', '치즈피자', '페퍼로니피자', '불고기피자', '고구마피자', '포테이토피자'] 
WesternFood_price_dictionary = {'까르보나라파스타':8500, '목살필라프':9500, '새우필라프':9500, '토마토파스타':8500, '로제파스타':9500, '알리오올리오파스타':8500, '리조또':8500, '스테이크':13000, '찹스테이크':13500, '감바스':15000, '바베큐폭립':25000, '치즈피자':15000, '페퍼로니피자':17000, '불고기피자':21000, '고구마피자':23000, '포테이토피자':19000}
WesternFood_calory_dictionary = {'까르보나라파스타':595, '목살필라프':802, '새우필라프':400, '토마토파스타':290, '로제파스타':543, '알리오올리오파스타':480, '리조또':500, '스테이크':540, '찹스테이크':498, '감바스':480, '바베큐폭립':1000, '치즈피자':1136, '페퍼로니피자':1304, '불고기피자':1272, '고구마피자':1488, '포테이토피자':1408}

#패스트푸드 - 리스트, 가격, 칼로리
FastFood_list = ['와플', '불고기버거', '새우버거', '치즈버거', '치킨버거', '감자튀김', '치즈스틱', '토스트', '타코', '샌드위치']
FastFood_price_dictionary = {'와플':5000, '불고기버거':3900, '새우버거':3900, '치즈버거':4500, '치킨버거':3100, '감자튀김':1700, '치즈스틱':1900, '토스트':5000, '타코':4500, '샌드위치':6000}
FastFood_calory_dictionary = {'와플':600, '불고기버거':390, '새우버거':492, '치즈버거':483, '치킨버거':355, '감자튀김':313, '치즈스틱':310, '토스트':420, '타코':300, '샌드위치':378}   

#아시안 - 리스트, 가격, 칼로리
AsianFood_list = ['쌀국수', '팟타이', '분짜', '인도커리', '난', '탄두리치킨', '짜조', '똠양꿍', '망고라씨', '나시고랭', '반미']
AsianFood_price_dictionary = {'쌀국수':8000, '팟타이':9000, '분짜':10000, '인도커리':13000, '난':3000, '탄두리치킨':20000, '짜조':6900, '똠양꿍':10000, '망고라씨':5000, '나시고랭':8000, '반미':8000}
AsianFood_calory_dictionary = {'쌀국수':320, '팟타이':340, '분짜':765, '인도커리':632, '난':137, '탄두리치킨':396, '짜조':63, '똠양꿍':280, '망고라씨':235, '나시고랭':430, '반미':716}

#리스트, 가격, 칼로리 합본
AllFood_list = ChineseFood_list + JapaneseFood_list + KoreanFood_list + FlourbasedFood_list + Chicken_list + WesternFood_list + FastFood_list + AsianFood_list
AllFood_price = {**ChineseFood_price_dictionary, **JapaneseFood_price_dictionary, **KoreanFood_price_dictionary, **FlourbasedFood_price_dictionary, **Chicken_price_dictionary, **WesternFood_price_dictionary, **FastFood_price_dictionary, **AsianFood_price_dictionary}
AllFood_calory = {**ChineseFood_calory_dictionary, **JapaneseFood_calory_dictionary, **KoreanFood_calory_dictionary, **FlourbasedFood_calory_dictionary, **Chicken_calory_dictionary, **WesternFood_calory_dictionary, **FastFood_calory_dictionary, **AsianFood_calory_dictionary}

#함수 모음
#1. 음식 종류를 기준으로 랜덤 추출하는 함수
def ChooseList(listnum) :
    if listnum == 1 :
        choiceFood = random.choice(ChineseFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif listnum == 2 :
        choiceFood = random.choice(JapaneseFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif listnum == 3 :
        choiceFood = random.choice(KoreanFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif listnum == 4 :
        choiceFood = random.choice(FlourbasedFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif listnum == 5 :
        choiceFood = random.choice(Chicken_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif listnum == 6 :
        choiceFood = random.choice(WesternFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif listnum == 7 :
        choiceFood = random.choice(FastFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif listnum == 8 :
        choiceFood = random.choice(AsianFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    else :
        print("숫자를 잘못 입력했습니다. 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")

#2. 가격을 기준으로 랜덤 추출하는 함수
def ChoosePrice(choicenum) :
    choiceFood1 = random.choice(AllFood_list)
    if choicenum == 1 :
        if 0 <= AllFood_price[choiceFood1] <= 8000 :
            print(choiceFood1, ":", AllFood_price[choiceFood1],"원 , ", AllFood_calory[choiceFood1], "칼로리")
        else :
            ChoosePrice(choicenum)
    elif choicenum == 2 :
        if 8000 < AllFood_price[choiceFood1] <= 15000 :
            print(choiceFood1, ":", AllFood_price[choiceFood1],"원 , ", AllFood_calory[choiceFood1], "칼로리")
        else :
            ChoosePrice(choicenum)
    elif choicenum == 3 :
        if AllFood_price[choiceFood1] > 15000 :
            print(choiceFood1, ":", AllFood_price[choiceFood1],"원 , ", AllFood_calory[choiceFood1], "칼로리")
        else :
            ChoosePrice(choicenum)
    else :
        print("숫자를 잘못 입력했습니다. 랜덤으로 음식을 뽑겠습니다.")
        print(choiceFood1, ":", AllFood_price[choiceFood1],"원 , ", AllFood_calory[choiceFood1], "칼로리")

#3. 칼로리를 기준으로 랜덤 추출하는 함수
def ChooseCalory(choicenum) :
    choiceFood1 = random.choice(AllFood_list)
    if choicenum == 1 :
        if 0 <= AllFood_calory[choiceFood1] <= 500 :
            print(choiceFood1, ":", AllFood_price[choiceFood1],"원 , ", AllFood_calory[choiceFood1], "칼로리")
        else :
            ChooseCalory(choicenum)
    elif choicenum == 2 :
        if 500 < AllFood_calory[choiceFood1] <= 900 :
            print(choiceFood1, ":", AllFood_price[choiceFood1],"원 , ", AllFood_calory[choiceFood1], "칼로리")
        else :
            ChooseCalory(choicenum)
    elif choicenum == 3 :
        if AllFood_calory[choiceFood1] > 900 :
            print(choiceFood1, ":", AllFood_price[choiceFood1],"원 , ", AllFood_calory[choiceFood1], "칼로리")
        else :
            ChooseCalory(choicenum)
    else :
        print("숫자를 잘못 입력했습니다. 랜덤으로 음식을 뽑겠습니다.")
        print(choiceFood1, ":", AllFood_price[choiceFood1],"원 , ", AllFood_calory[choiceFood1], "칼로리")

#1.음식종류 & 2.가격을 기준으로 랜덤 추출하는 함수
def ChooseListPrice(listnum, ChoicePriceNum) :
    if listnum == 1 and ChoicePriceNum == 1 :
        choiceFood = random.choice(ChineseFood_list)
        if 0 <= ChineseFood_price_dictionary[choiceFood] <= 8000 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPrice(listnum, ChoicePriceNum)
    elif listnum == 1 and ChoicePriceNum == 2 :
        choiceFood = random.choice(ChineseFood_list)
        if 8000 < ChineseFood_price_dictionary[choiceFood] <= 15000 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPrice(listnum, ChoicePriceNum)
    elif listnum == 1 and ChoicePriceNum == 3 :
        choiceFood = random.choice(ChineseFood_list)
        if ChineseFood_price_dictionary[choiceFood] > 15000 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPrice(listnum, ChoicePriceNum)
    elif listnum == 2 and ChoicePriceNum == 1 :
        choiceFood = random.choice(JapaneseFood_list)
        if 0 <= JapaneseFood_price_dictionary[choiceFood] <= 8000 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPrice(listnum, ChoicePriceNum)
    elif listnum == 2 and ChoicePriceNum == 2 :
        choiceFood = random.choice(JapaneseFood_list)
        if 8000 < JapaneseFood_price_dictionary[choiceFood] <= 15000 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPrice(listnum, ChoicePriceNum)
    elif listnum == 2 and ChoicePriceNum == 3 :
        choiceFood = random.choice(JapaneseFood_list)
        if JapaneseFood_price_dictionary[choiceFood] > 15000 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPrice(listnum, ChoicePriceNum)
    elif listnum == 3 and ChoicePriceNum == 1 :
        choiceFood = random.choice(KoreanFood_list)
        if 0 <= KoreanFood_price_dictionary[choiceFood] <= 8000 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPrice(listnum, ChoicePriceNum)
    elif listnum == 3 and ChoicePriceNum == 2 :
        choiceFood = random.choice(KoreanFood_list)
        if 8000 < KoreanFood_price_dictionary[choiceFood] <= 15000 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPrice(listnum, ChoicePriceNum)
    elif listnum == 3 and ChoicePriceNum == 3 :
        choiceFood = random.choice(KoreanFood_list)
        if KoreanFood_price_dictionary[choiceFood] > 15000 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPrice(listnum, ChoicePriceNum)
    elif listnum == 4 and ChoicePriceNum == 1 :
        choiceFood = random.choice(FlourbasedFood_list)
        if 0 <= FlourbasedFood_price_dictionary[choiceFood] <= 8000 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPrice(listnum, ChoicePriceNum)
    elif listnum == 4 and ChoicePriceNum == 2 :
        choiceFood = random.choice(FlourbasedFood_list)
        if 8000 < FlourbasedFood_price_dictionary[choiceFood] <= 15000 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPrice(listnum, ChoicePriceNum)
    elif listnum == 4 and ChoicePriceNum == 3 :
        choiceFood = random.choice(FlourbasedFood_list)
        if FlourbasedFood_price_dictionary[choiceFood] > 15000 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPrice(listnum, ChoicePriceNum)
    elif listnum == 5 and ChoicePriceNum == 1 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif listnum == 5 and ChoicePriceNum == 2 :
        choiceFood = random.choice(Chicken_list)
        if 8000 < Chicken_price_dictionary[choiceFood] <= 15000 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPrice(listnum, ChoicePriceNum)
    elif listnum == 5 and ChoicePriceNum == 3 :
        choiceFood = random.choice(Chicken_list)
        if Chicken_price_dictionary[choiceFood] > 15000 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPrice(listnum, ChoicePriceNum)
    elif listnum == 6 and ChoicePriceNum == 1 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif listnum == 6 and ChoicePriceNum == 2 :
        choiceFood = random.choice(WesternFood_list)
        if 8000 < WesternFood_price_dictionary[choiceFood] <= 15000 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPrice(listnum, ChoicePriceNum)
    elif listnum == 6 and ChoicePriceNum == 3 :
        choiceFood = random.choice(WesternFood_list)
        if WesternFood_price_dictionary[choiceFood] > 15000 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPrice(listnum, ChoicePriceNum)
    elif listnum == 7 and ChoicePriceNum == 1 :
        choiceFood = random.choice(FastFood_list)
        if 0 <= FastFood_price_dictionary[choiceFood] <= 8000 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPrice(listnum, ChoicePriceNum)
    elif listnum == 7 and ChoicePriceNum == 2 :
        choiceFood = random.choice(FastFood_list)
        if 8000 < FastFood_price_dictionary[choiceFood] <= 15000 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPrice(listnum, ChoicePriceNum)
    elif listnum == 7 and ChoicePriceNum == 3 :
        choiceFood = random.choice(FastFood_list)
        if FastFood_price_dictionary[choiceFood] > 15000 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPrice(listnum, ChoicePriceNum)
    elif listnum == 8 and ChoicePriceNum == 1 :
        choiceFood = random.choice(AsianFood_list)
        if 0 <= AsianFood_price_dictionary[choiceFood] <= 8000 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPrice(listnum, ChoicePriceNum)
    elif listnum == 8 and ChoicePriceNum == 2 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif listnum == 8 and ChoicePriceNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    else :
        print("숫자를 잘못 입력했습니다. 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")

#1.음식종류 & 3.칼로리를 기준으로 랜덤 추출하는 함수
def ChooseListCalory(listnum, ChoiceCaloryNum) :
    if listnum == 1 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(ChineseFood_list)
        if 0 <= ChineseFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListCalory(listnum, ChoiceCaloryNum)
    elif listnum == 1 and ChoiceCaloryNum == 2 :
        choiceFood = random.choice(ChineseFood_list)
        if 500 < ChineseFood_calory_dictionary[choiceFood] <= 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListCalory(listnum, ChoiceCaloryNum)
    elif listnum == 1 and ChoiceCaloryNum == 3 :
        choiceFood = random.choice(ChineseFood_list)
        if ChineseFood_calory_dictionary[choiceFood] > 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListCalory(listnum, ChoiceCaloryNum)
    elif listnum == 2 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(JapaneseFood_list)
        if 0 <= JapaneseFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListCalory(listnum, ChoiceCaloryNum)
    elif listnum == 2 and ChoiceCaloryNum == 2 :
        choiceFood = random.choice(JapaneseFood_list)
        if 500 < JapaneseFood_calory_dictionary[choiceFood] <= 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListCalory(listnum, ChoiceCaloryNum)
    elif listnum == 2 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif listnum == 3 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(KoreanFood_list)
        if 0 <= KoreanFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListCalory(listnum, ChoiceCaloryNum)
    elif listnum == 3 and ChoiceCaloryNum == 2 :
        choiceFood = random.choice(KoreanFood_list)
        if 500 < KoreanFood_calory_dictionary[choiceFood] <= 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListCalory(listnum, ChoiceCaloryNum)
    elif listnum == 3 and ChoiceCaloryNum == 3 :
        choiceFood = random.choice(KoreanFood_list)
        if KoreanFood_calory_dictionary[choiceFood] > 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListCalory(listnum, ChoiceCaloryNum)
    elif listnum == 4 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(FlourbasedFood_list)
        if 0 <= FlourbasedFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListCalory(listnum, ChoiceCaloryNum)
    elif listnum == 4 and ChoiceCaloryNum == 2 :
        choiceFood = random.choice(FlourbasedFood_list)
        if 500 < FlourbasedFood_calory_dictionary[choiceFood] <= 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListCalory(listnum, ChoiceCaloryNum)
    elif listnum == 4 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif listnum == 5 and ChoiceCaloryNum == 1 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif listnum == 5 and ChoiceCaloryNum == 2 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif listnum == 5 and ChoiceCaloryNum == 3 :
        choiceFood = random.choice(Chicken_list)
        if Chicken_calory_dictionary[choiceFood] > 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListCalory(listnum, ChoiceCaloryNum)
    elif listnum == 6 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(WesternFood_list)
        if 0 <= WesternFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListCalory(listnum, ChoiceCaloryNum)
    elif listnum == 6 and ChoiceCaloryNum == 2 :
        choiceFood = random.choice(WesternFood_list)
        if 500 < WesternFood_calory_dictionary[choiceFood] <= 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListCalory(listnum, ChoiceCaloryNum)
    elif listnum == 6 and ChoiceCaloryNum == 3 :
        choiceFood = random.choice(WesternFood_list)
        if WesternFood_calory_dictionary[choiceFood] > 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListCalory(listnum, ChoiceCaloryNum)
    elif listnum == 7 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(FastFood_list)
        if 0 <= FastFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListCalory(listnum, ChoiceCaloryNum)
    elif listnum == 7 and ChoiceCaloryNum == 2 :
        choiceFood = random.choice(FastFood_list)
        if 500 < FastFood_calory_dictionary[choiceFood] <= 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListCalory(listnum, ChoiceCaloryNum)
    elif listnum == 7 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif listnum == 8 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(AsianFood_list)
        if 0 <= AsianFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListCalory(listnum, ChoiceCaloryNum)
    elif listnum == 8 and ChoiceCaloryNum == 2 :
        choiceFood = random.choice(AsianFood_list)
        if 500 < AsianFood_calory_dictionary[choiceFood] <= 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListCalory(listnum, ChoiceCaloryNum)
    elif listnum == 8 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    else :
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")

#2.가격대 & 3.칼로리를 기준으로 랜덤 추출하는 함수
def ChoosePriceCalory(ChoicePriceNum, ChoiceCaloryNum) :
    choiceFood = random.choice(AllFood_list) 
    if ChoicePriceNum == 1 :
        if ChoiceCaloryNum == 1 :
            if 0 <= AllFood_price[choiceFood] <= 8000 and 0 <= AllFood_calory[choiceFood] <= 500 :
                print(choiceFood, ":", AllFood_price[choiceFood], "원 , ", AllFood_calory[choiceFood], "칼로리")
            else :
                ChoosePriceCalory(ChoicePriceNum, ChoiceCaloryNum)

        elif ChoiceCaloryNum == 2 :
            if  0 <= AllFood_price[choiceFood] <= 8000 and 500 < AllFood_calory[choiceFood] <= 900 :
                print(choiceFood, ":", AllFood_price[choiceFood], "원 , ", AllFood_calory[choiceFood], "칼로리")
            else :
                ChoosePriceCalory(ChoicePriceNum, ChoiceCaloryNum)

        elif ChoiceCaloryNum == 3 :
            print("조건에 맞는 음식이 존재하지 않거나 잘못 선택하셨습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")

        else:
            print("조건에 맞는 음식이 존재하지 않거나 잘못 선택하셨습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")

    elif ChoicePriceNum == 2 :
        if ChoiceCaloryNum == 1 :
            if 8000 < AllFood_price[choiceFood] <= 15000 and 0 <= AllFood_calory[choiceFood] <= 500 :
                print(choiceFood, ":", AllFood_price[choiceFood], "원 , ", AllFood_calory[choiceFood], "칼로리")
            else :
                ChoosePriceCalory(ChoicePriceNum, ChoiceCaloryNum)

        elif ChoiceCaloryNum == 2 :
            if  8000 < AllFood_price[choiceFood] <= 15000 and 500 < AllFood_calory[choiceFood] <= 900 :
                print(choiceFood, ":", AllFood_price[choiceFood], "원 , ", AllFood_calory[choiceFood], "칼로리")
            else :
                ChoosePriceCalory(ChoicePriceNum, ChoiceCaloryNum)

        elif ChoiceCaloryNum == 3 :
            if 8000 < AllFood_price[choiceFood] <= 15000 and AllFood_calory[choiceFood] > 900 :
                print(choiceFood, ":", AllFood_price[choiceFood], "원 , ", AllFood_calory[choiceFood], "칼로리")
            else :
                ChoosePriceCalory(ChoicePriceNum, ChoiceCaloryNum)

        else:
            print("조건에 맞는 음식이 존재하지 않거나 잘못 선택하셨습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")

    elif ChoicePriceNum == 3 :
        if ChoiceCaloryNum == 1 :
            if  AllFood_price[choiceFood] > 15000 and 0 <= AllFood_calory[choiceFood] <= 500 :
                print(choiceFood, ":", AllFood_price[choiceFood], "원 , ", AllFood_calory[choiceFood], "칼로리")
            else :
                ChoosePriceCalory(ChoicePriceNum, ChoiceCaloryNum)

        elif ChoiceCaloryNum == 2 :
            if  AllFood_price[choiceFood] > 15000 and 500 < AllFood_calory[choiceFood] <= 900 :
                print(choiceFood, ":", AllFood_price[choiceFood], "원 , ", AllFood_calory[choiceFood], "칼로리")
            else :
                ChoosePriceCalory(ChoicePriceNum, ChoiceCaloryNum)

        elif ChoiceCaloryNum == 3 :
            if AllFood_price[choiceFood] > 15000 and AllFood_calory[choiceFood] > 900 :
                print(choiceFood, ":", AllFood_price[choiceFood], "원 , ", AllFood_calory[choiceFood], "칼로리")
            else :
                ChoosePriceCalory(ChoicePriceNum, ChoiceCaloryNum)

        else:
            print("조건에 맞는 음식이 존재하지 않거나 잘못 선택하셨습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    else:
        print("조건에 맞는 음식이 존재하지 않거나 잘못 선택하셨습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")

#1.음식종류 & 2.가격대 & 3.칼로리를 기준으로 랜덤 추출하는 함수
def ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum) :
    if ChoiceListNum == 1 and ChoicePriceNum == 1 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(ChineseFood_list)
        if 0 <= ChineseFood_price_dictionary[choiceFood] <= 8000 and 0 <= ChineseFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 1 and ChoicePriceNum == 1 and ChoiceCaloryNum == 2 :
        choiceFood = random.choice(ChineseFood_list)
        if 0 <= ChineseFood_price_dictionary[choiceFood] <= 8000 and 500 < ChineseFood_calory_dictionary[choiceFood] <= 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 1 and ChoicePriceNum == 1 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 1 and ChoicePriceNum == 2 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(ChineseFood_list)
        if 8000 < ChineseFood_price_dictionary[choiceFood] <= 15000 and 0 <= ChineseFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 1 and ChoicePriceNum == 2 and ChoiceCaloryNum == 2 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 1 and ChoicePriceNum == 2 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 1 and ChoicePriceNum == 3 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(ChineseFood_list)
        if ChineseFood_price_dictionary[choiceFood] > 15000 and 0 <= ChineseFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 1 and ChoicePriceNum == 3 and ChoiceCaloryNum == 2 :
        choiceFood = random.choice(ChineseFood_list)
        if ChineseFood_price_dictionary[choiceFood] > 15000 and 500 < ChineseFood_calory_dictionary[choiceFood] <= 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 1 and ChoicePriceNum == 3 and ChoiceCaloryNum == 3 :
        choiceFood = random.choice(ChineseFood_list)
        if ChineseFood_price_dictionary[choiceFood] > 15000 and ChineseFood_calory_dictionary[choiceFood] > 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 2 and ChoicePriceNum == 1 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(JapaneseFood_list)
        if 0 <= JapaneseFood_price_dictionary[choiceFood] <= 8000 and 0 <= JapaneseFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 2 and ChoicePriceNum == 1 and ChoiceCaloryNum == 2 :
        choiceFood = random.choice(JapaneseFood_list)
        if 0 <= JapaneseFood_price_dictionary[choiceFood] <= 8000 and 500 < JapaneseFood_calory_dictionary[choiceFood] <= 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 2 and ChoicePriceNum == 1 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 2 and ChoicePriceNum == 2 and ChoiceCaloryNum == 1 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 2 and ChoicePriceNum == 2 and ChoiceCaloryNum == 2 :
        choiceFood = random.choice(JapaneseFood_list)
        if 8000 < JapaneseFood_price_dictionary[choiceFood] <= 15000 and 500 < JapaneseFood_calory_dictionary[choiceFood] <= 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 2 and ChoicePriceNum == 2 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 2 and ChoicePriceNum == 3 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(JapaneseFood_list)
        if JapaneseFood_price_dictionary[choiceFood] > 15000 and 0 <= JapaneseFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 2 and ChoicePriceNum == 3 and ChoiceCaloryNum == 2 :
        choiceFood = random.choice(JapaneseFood_list)
        if JapaneseFood_price_dictionary[choiceFood] > 15000 and 500 < JapaneseFood_calory_dictionary[choiceFood] <= 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 2 and ChoicePriceNum == 3 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 3 and ChoicePriceNum == 1 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(KoreanFood_list)
        if 0 <= KoreanFood_price_dictionary[choiceFood] <= 8000 and 0 <= KoreanFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 3 and ChoicePriceNum == 1 and ChoiceCaloryNum == 2 :
        choiceFood = random.choice(KoreanFood_list)
        if 0 <= KoreanFood_price_dictionary[choiceFood] <= 8000 and 500 < KoreanFood_calory_dictionary[choiceFood] <= 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 3 and ChoicePriceNum == 1 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 3 and ChoicePriceNum == 2 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(KoreanFood_list)
        if 8000 < KoreanFood_price_dictionary[choiceFood] <= 15000 and 0 <= KoreanFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 3 and ChoicePriceNum == 2 and ChoiceCaloryNum == 2 :
        choiceFood = random.choice(KoreanFood_list)
        if 8000 < KoreanFood_price_dictionary[choiceFood] <= 15000 and 500 < KoreanFood_calory_dictionary[choiceFood] <= 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 3 and ChoicePriceNum == 2 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 3 and ChoicePriceNum == 3 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(KoreanFood_list)
        if KoreanFood_price_dictionary[choiceFood] > 15000 and 0 <= KoreanFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 3 and ChoicePriceNum == 3 and ChoiceCaloryNum == 2 :
        choiceFood = random.choice(KoreanFood_list)
        if KoreanFood_price_dictionary[choiceFood] > 15000 and 500 < KoreanFood_calory_dictionary[choiceFood] <= 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 3 and ChoicePriceNum == 3 and ChoiceCaloryNum == 3 :
        choiceFood = random.choice(KoreanFood_list)
        if KoreanFood_price_dictionary[choiceFood] > 15000 and KoreanFood_calory_dictionary[choiceFood] > 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 4 and ChoicePriceNum == 1 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(FlourbasedFood_list)
        if 0 <= FlourbasedFood_price_dictionary[choiceFood] <= 8000 and 0 <= FlourbasedFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 4 and ChoicePriceNum == 1 and ChoiceCaloryNum == 2 :
        choiceFood = random.choice(FlourbasedFood_list)
        if 0 <= FlourbasedFood_price_dictionary[choiceFood] <= 8000 and 500 < FlourbasedFood_calory_dictionary[choiceFood] <= 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 4 and ChoicePriceNum == 1 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 4 and ChoicePriceNum == 2 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(FlourbasedFood_list)
        if 8000 < FlourbasedFood_price_dictionary[choiceFood] <= 15000 and 0 <= FlourbasedFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 4 and ChoicePriceNum == 2 and ChoiceCaloryNum == 2 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 4 and ChoicePriceNum == 2 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 4 and ChoicePriceNum == 3 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(FlourbasedFood_list)
        if FlourbasedFood_price_dictionary[choiceFood] > 15000 and 0 <= FlourbasedFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 4 and ChoicePriceNum == 3 and ChoiceCaloryNum == 2 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 4 and ChoicePriceNum == 3 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 5 and ChoicePriceNum == 1 and ChoiceCaloryNum == 1 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 5 and ChoicePriceNum == 1 and ChoiceCaloryNum == 2 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 5 and ChoicePriceNum == 1 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 5 and ChoicePriceNum == 2 and ChoiceCaloryNum == 1 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 5 and ChoicePriceNum == 2 and ChoiceCaloryNum == 2 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 5 and ChoicePriceNum == 2 and ChoiceCaloryNum == 3 :
        choiceFood = random.choice(Chicken_list)
        if 8000 < Chicken_price_dictionary[choiceFood] <= 15000 and Chicken_calory_dictionary[choiceFood] > 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 5 and ChoicePriceNum == 3 and ChoiceCaloryNum == 1 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 5 and ChoicePriceNum == 3 and ChoiceCaloryNum == 2 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 5 and ChoicePriceNum == 3 and ChoiceCaloryNum == 3 :
        choiceFood = random.choice(Chicken_list)
        if Chicken_price_dictionary[choiceFood] > 15000 and Chicken_calory_dictionary[choiceFood] > 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 6 and ChoicePriceNum == 1 and ChoiceCaloryNum == 1 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 6 and ChoicePriceNum == 1 and ChoiceCaloryNum == 2 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 6 and ChoicePriceNum == 1 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 6 and ChoicePriceNum == 2 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(WesternFood_list)
        if 8000 < WesternFood_price_dictionary[choiceFood] <= 15000 and 0 <= WesternFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 6 and ChoicePriceNum == 2 and ChoiceCaloryNum == 2 :
        choiceFood = random.choice(WesternFood_list)
        if 8000 < WesternFood_price_dictionary[choiceFood] <= 15000 and 500 < WesternFood_calory_dictionary[choiceFood] <= 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 6 and ChoicePriceNum == 2 and ChoiceCaloryNum == 3 :
        choiceFood = random.choice(WesternFood_list)
        if 8000 < WesternFood_price_dictionary[choiceFood] <= 15000 and WesternFood_calory_dictionary[choiceFood] > 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 6 and ChoicePriceNum == 3 and ChoiceCaloryNum == 1 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 6 and ChoicePriceNum == 3 and ChoiceCaloryNum == 2 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 6 and ChoicePriceNum == 3 and ChoiceCaloryNum == 3 :
        choiceFood = random.choice(WesternFood_list)
        if WesternFood_price_dictionary[choiceFood] > 15000 and WesternFood_calory_dictionary[choiceFood] > 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 7 and ChoicePriceNum == 1 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(FastFood_list)
        if 0 <= FastFood_price_dictionary[choiceFood] <= 8000 and 0 <= FastFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 7 and ChoicePriceNum == 1 and ChoiceCaloryNum == 2 :
        choiceFood = random.choice(FastFood_list)
        if 0 <= FastFood_price_dictionary[choiceFood] <= 8000 and 500 < FastFood_calory_dictionary[choiceFood] <= 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 7 and ChoicePriceNum == 1 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 7 and ChoicePriceNum == 2 and ChoiceCaloryNum == 1 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 7 and ChoicePriceNum == 2 and ChoiceCaloryNum == 2 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 7 and ChoicePriceNum == 2 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 7 and ChoicePriceNum == 3 and ChoiceCaloryNum == 1 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 7 and ChoicePriceNum == 3 and ChoiceCaloryNum == 2 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 7 and ChoicePriceNum == 3 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 8 and ChoicePriceNum == 1 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(AsianFood_list)
        if 0 <= AsianFood_price_dictionary[choiceFood] <= 8000 and 0 <= AsianFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 8 and ChoicePriceNum == 1 and ChoiceCaloryNum == 2 :
        choiceFood = random.choice(AsianFood_list)
        if 0 <= AsianFood_price_dictionary[choiceFood] <= 8000 and 500 < AsianFood_calory_dictionary[choiceFood] <= 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 8 and ChoicePriceNum == 1 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 8 and ChoicePriceNum == 2 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(AsianFood_list)
        if 8000 < AsianFood_price_dictionary[choiceFood] <= 15000 and 0 <= AsianFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 8 and ChoicePriceNum == 2 and ChoiceCaloryNum == 2 :
        choiceFood = random.choice(AsianFood_list)
        if 8000 < AsianFood_price_dictionary[choiceFood] <= 15000 and 500 < AsianFood_calory_dictionary[choiceFood] <= 900 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 8 and ChoicePriceNum == 2 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 8 and ChoicePriceNum == 3 and ChoiceCaloryNum == 1 :
        choiceFood = random.choice(AsianFood_list)
        if AsianFood_price_dictionary[choiceFood] > 15000 and 0 <= AsianFood_calory_dictionary[choiceFood] <= 500 :
            print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
        else :
            ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    elif ChoiceListNum == 8 and ChoicePriceNum == 3 and ChoiceCaloryNum == 2 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    elif ChoiceListNum == 8 and ChoicePriceNum == 3 and ChoiceCaloryNum == 3 :
        print("존재하지 않습니다. 대신 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    else :
        print("숫자를 잘못 입력했습니다. 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")

#변수 모음
ChoiceListNum = 0       #1.음식 종류 기준 함수에서 쓰이는 변수
ChoiceCaloryNum = 0     #2.칼로리 기준 함수에서 쓰이는 변수
ChoicePriceNum = 0      #3.가격 기준 함수에서 쓰이는 변수

#메인 코드
#choice_list에 랜덤 음식 추출 기준을 한 숫자씩 , 이용해서 개별적으로 저장
guideline = '''
랜덤으로 음식을 뽑는 기준 : 1. 음식 종류, 2. 가격대 3. 칼로리, 4. 아무거나
이 중에서 어떤 기준으로 음식을 랜덤으로 정할지 고르세요. 중복으로 고를 수 있어요.
,를 사용해서 구분해 주세요. 예) 1 또는 1,2 또는 1,2,3 또는 1,2,3,4 등. 여러 개의 숫자를 입력 시 ","를 쓰고 띄어쓰면 안돼요.
기준을 고르세요 : '''
choice_list = [x for x in input(guideline).split(",")]
choice_list.sort()

#입력한 숫자에 따라 랜덤 음식 뽑기
if len(choice_list) > 4 :
    print("숫자를 잘못 입력했습니다. 랜덤으로 음식을 뽑겠습니다.")
    choiceFood = random.choice(AllFood_list)
    print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
if len(choice_list) == 4 :
    #"1.음식종류"와 "2.가격대"와 "3.칼로리"와 "4.아무거나"를  동시에 선택했을 때, 랜덤 뽑기
    if choice_list[0] == '1' and choice_list[1] == '2' and choice_list[2] == '3' and choice_list[3] == '4':
        print("4.아무거나를 선택했습니다. 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    #숫자를 잘못 입력했을 때, 랜덤 음식 뽑기
    else :
        print("숫자를 잘못 입력했습니다. 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
if len(choice_list) == 3 :    
    #"1.음식종류"와 "2.가격대"와 "3.칼로리"를  동시에 선택했을 때, 랜덤 뽑기
    if choice_list[0] == '1' and choice_list[1] == '2' and choice_list[2] == '3' :
        ChoiceListNum = int(input("어떤 종류의 음식을 드실건가요? (1.중식 2.일식 3.한식 4. 분식 5.치킨 6.양식 7.패스트푸드 8.아시안) *숫자를 잘못입력하면 무작위로 추출됩니다!!!* : "))
        ChoicePriceNum = int(input("원하시는 가격 범위를 선택하세요.(0~8000 : 1, 8001~15000 : 2, 15001~ : 3) *숫자를 잘못입력하면 무작위로 추출됩니다!!!* : "))
        ChoiceCaloryNum = int(input("원하시는 칼로리 범위를 선택하세요.(0~500 : 1, 501~900 : 2, 901~ : 3) *숫자를 잘못입력하면 무작위로 추출됩니다!!!* : "))
        ChooseListPriceCalory(ChoiceListNum, ChoicePriceNum, ChoiceCaloryNum)
    #"1.음식종류"와 "2.가격대"와 "4.아무거나"를  동시에 선택했을 때, 랜덤 뽑기
    elif choice_list[0] == '1' and choice_list[1] == '2' and choice_list[2] == '4' :
        print("4.아무거나를 선택했습니다. 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    #"1.음식종류"와 "3.칼로리"와 "4.아무거나"를  동시에 선택했을 때, 랜덤 뽑기
    elif choice_list[0] == '1' and choice_list[1] == '3' and choice_list[2] == '4' :
        print("4.아무거나를 선택했습니다. 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    #"2.가격대"와 "3.칼로리"와 "4.아무거나"를  동시에 선택했을 때, 랜덤 뽑기
    elif choice_list[0] == '2' and choice_list[1] == '3' and choice_list[2] == '4' :
        print("4.아무거나를 선택했습니다. 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    #숫자를 잘못 입력했을 때, 랜덤 음식 뽑기
    else :
        print("숫자를 잘못 입력했습니다. 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
if len(choice_list) == 2 :    
    #"1.음식종류"와 "2.가격대"를  동시에 선택했을 때, 랜덤 뽑기
    if choice_list[0] == '1' and choice_list[1] == '2' :
        ChoiceListNum = int(input("어떤 종류의 음식을 드실건가요? (1.중식 2.일식 3.한식 4. 분식 5.치킨 6.양식 7.패스트푸드 8.아시안) *숫자를 잘못입력하면 무작위로 추출됩니다!!!* : "))
        ChoicePriceNum = int(input("원하시는 가격 범위를 선택하세요.(0~8000 : 1, 8001~15000 : 2, 15001~ : 3) *숫자를 잘못입력하면 무작위로 추출됩니다!!!* : "))  
        ChooseListPrice(ChoiceListNum, ChoicePriceNum)
    #"1.음식종류"와 "3.칼로리"를  동시에 선택했을 때, 랜덤 뽑기
    elif choice_list[0] == '1' and choice_list[1] == '3' :
        ChoiceListNum = int(input("어떤 종류의 음식을 드실건가요? (1.중식 2.일식 3.한식 4. 분식 5.치킨 6.양식 7.패스트푸드 8.아시안) *숫자를 잘못입력하면 무작위로 추출됩니다!!!* : "))
        ChoiceCaloryNum = int(input("원하시는 칼로리 범위를 선택하세요.(0~500 : 1, 501~900 : 2, 901~ : 3) *숫자를 잘못입력하면 무작위로 추출됩니다!!!* : "))
        ChooseListCalory(ChoiceListNum, ChoiceCaloryNum)
    #"1.음식종류"와 "2.가격대"와 "3.칼로리"와 "4.아무거나"를  동시에 선택했을 때, 랜덤 뽑기
    elif choice_list[0] == '1' and choice_list[1] == '4' :
        print("4.아무거나를 선택했습니다. 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    #"2.가격대"와 "3.칼로리"를  동시에 선택했을 때, 랜덤 뽑기
    elif choice_list[0] == '2' and choice_list[1] == '3' :
        ChoicePriceNum = int(input("원하시는 가격 범위를 선택하세요.(0~8000 : 1, 8001~15000 : 2, 15001~ : 3) *숫자를 잘못입력하면 무작위로 추출됩니다!!!* : "))
        ChoiceCaloryNum = int(input("원하시는 칼로리 범위를 선택하세요.(0~500 : 1, 501~900 : 2, 901~ : 3) *숫자를 잘못입력하면 무작위로 추출됩니다!!!* : "))
        ChoosePriceCalory(ChoicePriceNum, ChoiceCaloryNum)
    #"2.가격대"와 "4.아무거나"를  동시에 선택했을 때, 랜덤 뽑기
    elif choice_list[0] == '2' and choice_list[1] == '4' :
        print("4.아무거나를 선택했습니다. 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    #"3.칼로리"와 "4.아무거나"를  동시에 선택했을 때, 랜덤 뽑기
    elif choice_list[0] == '3' and choice_list[1] == '4' :
        print("4.아무거나를 선택했습니다. 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    #숫자를 잘못 입력했을 때, 랜덤 음식 뽑기
    else :
        print("숫자를 잘못 입력했습니다. 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
if len(choice_list) == 1 :    
    # "1.음식종류"를 선택했을 때, 랜덤 뽑기
    if choice_list[0] == '1' :
        ChoiceListNum = int(input("어떤 종류의 음식을 드실건가요? (1.중식 2.일식 3.한식 4. 분식 5.치킨 6.양식 7.패스트푸드 8.아시안) *숫자를 잘못입력하면 무작위로 추출됩니다!!!* : "))
        ChooseList(ChoiceListNum)
    # "2.가격대"를 선택했을 때, 랜덤 뽑기
    elif choice_list[0] == '2' :
        ChoicePriceNum = int(input("원하시는 가격 범위를 선택하세요.(0~8000 : 1, 8001~15000 : 2, 15001~ : 3) *숫자를 잘못입력하면 무작위로 추출됩니다!!!* : "))
        ChoosePrice(ChoicePriceNum)
    # "3.칼로리"를 선택했을 때, 랜덤 뽑기
    elif choice_list[0] == '3' :
        ChoiceCaloryNum = int(input("원하시는 칼로리 범위를 선택하세요.(0~500 : 1, 501~900 : 2, 901~ : 3) *숫자를 잘못입력하면 무작위로 추출됩니다!!!* : "))
        ChooseCalory(ChoiceCaloryNum)
    #"4.아무거나"를 선택했을 때, 랜덤 뽑기
    elif choice_list[0] == '4' :
        print("4.아무거나를 선택했습니다. 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")
    #숫자를 잘못 입력했을 때, 랜덤 음식 뽑기
    else :
        print("숫자를 잘못 입력했습니다. 랜덤으로 음식을 뽑겠습니다.")
        choiceFood = random.choice(AllFood_list)
        print(choiceFood, ":", AllFood_price[choiceFood],"원 , ", AllFood_calory[choiceFood], "칼로리")