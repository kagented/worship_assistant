import pandas as pd

#entry = input('bible | book | ch | verse1 | verse 2 \n')
entry = input('bible(gae/kjv) | book | ch | verse 1 \n')

d1 = entry.split()[0]
d2 = entry.split()[1]
d3 = entry.split()[2]
d4 = entry.split()[3]
#d5 = entry.split()[4]

try:

    bible = d1

    df = pd.read_csv(bible+'.csv', encoding='CP949')

    biblechp = {
        '창세기': '1',
        '출애굽기': '2',
        '레위기': '3',
        '민수기': '4',
        '신명기': '5',
        '여호수아': '6',
        '사사기': '7',
        '룻기': '8',
        '사무엘상': '9',
        '사무엘하': '10',
        '열왕기상': '11',
        '열왕기하': '12',
        '역대상': '13',
        '역대하': '14',
        '에스라': '15',
        '느헤미야': '16',
        '에스더': '17',
        '욥기': '18',
        '시편': '19',
        '잠언': '20',
        '전도서': '21',
        '아가': '22',
        '이사야': '23',
        '예레미야': '24',
        '예레미야애가': '25',
        '에스겔': '26',
        '다니엘': '27',
        '호세아': '28',
        '요엘': '29',
        '아모스': '30',
        '오바댜': '31',
        '요나': '32',
        '미가': '33',
        '나훔': '34',
        '하박국': '35',
        '스바냐': '36',
        '학개': '37',
        '스가랴': '38',
        '말라기': '39',
        '마태복음': '40',
        '마가복음': '41',
        '누가복음': '42',
        '요한복음': '43',
        '사도행전': '44',
        '로마서': '45',
        '고린도전서': '46',
        '고린도후서': '47',
        '갈라디아서': '48',
        '에베소서': '49',
        '빌립보서': '50',
        '골로새서': '51',
        '데살로니가전서': '52',
        '데살로니가후서': '53',
        '디모데전서': '54',
        '디모데후서': '55',
        '디도서': '56',
        '빌레몬서': '57',
        '히브리서': '58',
        '야고보서': '59',
        '베드로전서': '60',
        '베드로후서': '61',
        '요한일서': '62',
        '요한이서': '63',
        '요한삼서': '64',
        '유다서': '65',
        '요한계시록': '66',
        '창': '1',
        '출': '2',
        '레': '3',
        '민': '4',
        '신': '5',
        '수': '6',
        '삿': '7',
        '룻': '8',
        '삼상': '9',
        '삼하': '10',
        '왕상': '11',
        '왕하': '12',
        '대상': '13',
        '대하': '14',
        '스': '15',
        '느': '16',
        '에': '17',
        '욥': '18',
        '시': '19',
        '잠': '20',
        '전': '21',
        '아': '22',
        '사': '23',
        '렘': '24',
        '애': '25',
        '겔': '26',
        '단': '27',
        '호': '28',
        '욜': '29',
        '암': '30',
        '옵': '31',
        '욘': '32',
        '미': '33',
        '나': '34',
        '합': '35',
        '습': '36',
        '학': '37',
        '슥': '38',
        '말': '39',
        '마': '40',
        '막': '41',
        '눅': '42',
        '요': '43',
        '행': '44',
        '롬': '45',
        '고전': '46',
        '고후': '47',
        '갈': '48',
        '엡': '49',
        '빌': '50',
        '골': '51',
        '살전': '52',
        '살후': '53',
        '딤전': '54',
        '딤후': '55',
        '딛': '56',
        '빌': '57',
        '히': '58',
        '약': '59',
        '벧전': '60',
        '벧후': '61',
        '요1': '62',
        '요2': '63',
        '요3': '64',
        '유': '65',
        '계': '66',

    }

    v1 = d2

    v1 = biblechp[v1]

    v2 = d3

    if len(str(v2)) == 1:
        v2 = '00'+str(v2)
    elif len(str(v2)) == 2:
        v2 = '0'+str(v2)

    v3 = d4

    if len(str(v3)) == 1:
        v3 = '00'+str(v3)
    elif len(str(v3)) == 2:
        v3 = '0'+str(v3)

    value = v1+v2+v3

    scripture = df[df['id'] == int(value)]['t'].values[0]

    print(scripture)

except:
    print('No result, Please check the book, chapter, or verse.')
