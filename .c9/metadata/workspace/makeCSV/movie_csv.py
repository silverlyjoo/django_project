{"filter":false,"title":"movie_csv.py","tooltip":"/makeCSV/movie_csv.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":7,"column":4},"end":{"row":7,"column":7},"action":"insert","lines":[" []"],"id":281,"ignore":true}],[{"start":{"row":7,"column":7},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":282,"ignore":true}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"insert","lines":["L"],"id":283,"ignore":true}],[{"start":{"row":8,"column":1},"end":{"row":8,"column":3},"action":"insert","lines":["3 "],"id":284,"ignore":true}],[{"start":{"row":8,"column":3},"end":{"row":8,"column":7},"action":"insert","lines":["= []"],"id":285,"ignore":true}],[{"start":{"row":18,"column":25},"end":{"row":19,"column":12},"action":"insert","lines":["","            "],"id":286,"ignore":true}],[{"start":{"row":19,"column":12},"end":{"row":19,"column":13},"action":"insert","lines":["L"],"id":287,"ignore":true}],[{"start":{"row":19,"column":13},"end":{"row":19,"column":14},"action":"insert","lines":["2"],"id":288,"ignore":true}],[{"start":{"row":19,"column":14},"end":{"row":19,"column":15},"action":"insert","lines":["."],"id":289,"ignore":true}],[{"start":{"row":19,"column":15},"end":{"row":19,"column":18},"action":"insert","lines":["app"],"id":290,"ignore":true}],[{"start":{"row":19,"column":18},"end":{"row":19,"column":21},"action":"insert","lines":["end"],"id":291,"ignore":true}],[{"start":{"row":19,"column":21},"end":{"row":19,"column":23},"action":"insert","lines":["()"],"id":292,"ignore":true}],[{"start":{"row":19,"column":22},"end":{"row":19,"column":25},"action":"insert","lines":["req"],"id":293,"ignore":true}],[{"start":{"row":19,"column":25},"end":{"row":19,"column":26},"action":"insert","lines":["1"],"id":294,"ignore":true}],[{"start":{"row":19,"column":26},"end":{"row":20,"column":12},"action":"insert","lines":["","            "],"id":295,"ignore":true}],[{"start":{"row":19,"column":26},"end":{"row":20,"column":12},"action":"remove","lines":["","            "],"id":296,"ignore":true}],[{"start":{"row":19,"column":27},"end":{"row":20,"column":13},"action":"insert","lines":["","            L"],"id":297,"ignore":true}],[{"start":{"row":20,"column":13},"end":{"row":20,"column":15},"action":"insert","lines":["3."],"id":298,"ignore":true}],[{"start":{"row":20,"column":15},"end":{"row":20,"column":23},"action":"insert","lines":["append()"],"id":299,"ignore":true}],[{"start":{"row":20,"column":22},"end":{"row":20,"column":26},"action":"insert","lines":["req2"],"id":300,"ignore":true},{"start":{"row":20,"column":27},"end":{"row":21,"column":12},"action":"insert","lines":["","            "]}],[{"start":{"row":8,"column":7},"end":{"row":9,"column":1},"action":"insert","lines":["","L"],"id":301,"ignore":true}],[{"start":{"row":9,"column":1},"end":{"row":9,"column":2},"action":"insert","lines":["4"],"id":302,"ignore":true}],[{"start":{"row":9,"column":2},"end":{"row":9,"column":4},"action":"insert","lines":[" ="],"id":303,"ignore":true}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":7},"action":"insert","lines":[" []"],"id":304,"ignore":true}],[{"start":{"row":21,"column":27},"end":{"row":22,"column":12},"action":"insert","lines":["","            "],"id":305,"ignore":true}],[{"start":{"row":22,"column":12},"end":{"row":22,"column":13},"action":"insert","lines":["L"],"id":306,"ignore":true}],[{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"insert","lines":["4"],"id":307,"ignore":true}],[{"start":{"row":22,"column":14},"end":{"row":22,"column":15},"action":"insert","lines":["."],"id":308,"ignore":true}],[{"start":{"row":22,"column":15},"end":{"row":22,"column":16},"action":"insert","lines":["a"],"id":309,"ignore":true}],[{"start":{"row":22,"column":16},"end":{"row":22,"column":21},"action":"insert","lines":["ppend"],"id":310,"ignore":true}],[{"start":{"row":22,"column":21},"end":{"row":22,"column":23},"action":"insert","lines":["()"],"id":311,"ignore":true}],[{"start":{"row":22,"column":22},"end":{"row":22,"column":23},"action":"insert","lines":["r"],"id":312,"ignore":true}],[{"start":{"row":22,"column":23},"end":{"row":22,"column":25},"action":"insert","lines":["eq"],"id":313,"ignore":true}],[{"start":{"row":22,"column":25},"end":{"row":22,"column":26},"action":"insert","lines":["3"],"id":314,"ignore":true}],[{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"remove","lines":["2"],"id":315,"ignore":true},{"start":{"row":18,"column":15},"end":{"row":18,"column":16},"action":"insert","lines":["3"]}],[{"start":{"row":24,"column":31},"end":{"row":25,"column":4},"action":"insert","lines":["","    "],"id":316,"ignore":true}],[{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"remove","lines":["    "],"id":317,"ignore":true}],[{"start":{"row":25,"column":0},"end":{"row":39,"column":31},"action":"insert","lines":["","with open('movielist.txt','w') as f:","    for page_num in range(1,16):","        movie_url = f\"https://api.themoviedb.org/3/movie/popular?api_key={movie_key}&language=ko-KR&page={page_num}\"","        for i in range(20):","            req = requests.get(movie_url).json()['results'][i]['title']","            req1 = requests.get(movie_url).json()['results'][i]['popularity']","            req2 = requests.get(movie_url).json()['results'][i]['overview']","            req3 = requests.get(movie_url).json()['results'][i]['release_date']","            L.append(req)","            L2.append(req1)","            L3.append(req2)","            L4.append(req3)","            ","    f.write(','.join(L)+'\\r\\n')"],"id":318,"ignore":true}],[{"start":{"row":39,"column":31},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":319,"ignore":true}],[{"start":{"row":40,"column":0},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":320,"ignore":true}],[{"start":{"row":41,"column":0},"end":{"row":54,"column":31},"action":"insert","lines":["with open('movielist.txt','w') as f:","    for page_num in range(1,16):","        movie_url = f\"https://api.themoviedb.org/3/movie/popular?api_key={movie_key}&language=ko-KR&page={page_num}\"","        for i in range(20):","            req = requests.get(movie_url).json()['results'][i]['title']","            req1 = requests.get(movie_url).json()['results'][i]['popularity']","            req2 = requests.get(movie_url).json()['results'][i]['overview']","            req3 = requests.get(movie_url).json()['results'][i]['release_date']","            L.append(req)","            L2.append(req1)","            L3.append(req2)","            L4.append(req3)","            ","    f.write(','.join(L)+'\\r\\n')"],"id":321,"ignore":true}],[{"start":{"row":54,"column":31},"end":{"row":55,"column":4},"action":"insert","lines":["","    "],"id":322,"ignore":true}],[{"start":{"row":55,"column":0},"end":{"row":55,"column":4},"action":"remove","lines":["    "],"id":323,"ignore":true},{"start":{"row":55,"column":0},"end":{"row":56,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":56,"column":0},"end":{"row":70,"column":4},"action":"insert","lines":["with open('movielist.txt','w') as f:","    for page_num in range(1,16):","        movie_url = f\"https://api.themoviedb.org/3/movie/popular?api_key={movie_key}&language=ko-KR&page={page_num}\"","        for i in range(20):","            req = requests.get(movie_url).json()['results'][i]['title']","            req1 = requests.get(movie_url).json()['results'][i]['popularity']","            req2 = requests.get(movie_url).json()['results'][i]['overview']","            req3 = requests.get(movie_url).json()['results'][i]['release_date']","            L.append(req)","            L2.append(req1)","            L3.append(req2)","            L4.append(req3)","            ","    f.write(','.join(L)+'\\r\\n')","    "],"id":324,"ignore":true}],[{"start":{"row":70,"column":0},"end":{"row":70,"column":4},"action":"remove","lines":["    "],"id":325,"ignore":true}],[{"start":{"row":70,"column":0},"end":{"row":84,"column":31},"action":"insert","lines":["","with open('movielist.txt','w') as f:","    for page_num in range(1,16):","        movie_url = f\"https://api.themoviedb.org/3/movie/popular?api_key={movie_key}&language=ko-KR&page={page_num}\"","        for i in range(20):","            req = requests.get(movie_url).json()['results'][i]['title']","            req1 = requests.get(movie_url).json()['results'][i]['popularity']","            req2 = requests.get(movie_url).json()['results'][i]['overview']","            req3 = requests.get(movie_url).json()['results'][i]['release_date']","            L.append(req)","            L2.append(req1)","            L3.append(req2)","            L4.append(req3)","            ","    f.write(','.join(L)+'\\r\\n')"],"id":326,"ignore":true}],[{"start":{"row":15,"column":71},"end":{"row":17,"column":75},"action":"remove","lines":["","            req1 = requests.get(movie_url).json()['results'][i]['popularity']","            req2 = requests.get(movie_url).json()['results'][i]['overview']"],"id":327,"ignore":true}],[{"start":{"row":15,"column":71},"end":{"row":16,"column":79},"action":"remove","lines":["","            req3 = requests.get(movie_url).json()['results'][i]['release_date']"],"id":328,"ignore":true},{"start":{"row":16,"column":25},"end":{"row":20,"column":12},"action":"remove","lines":["","            L2.append(req1)","            L3.append(req2)","            L4.append(req3)","            "]}],[{"start":{"row":22,"column":27},"end":{"row":23,"column":71},"action":"remove","lines":["","            req = requests.get(movie_url).json()['results'][i]['title']"],"id":329,"ignore":true}],[{"start":{"row":23,"column":77},"end":{"row":26,"column":25},"action":"remove","lines":["","            req2 = requests.get(movie_url).json()['results'][i]['overview']","            req3 = requests.get(movie_url).json()['results'][i]['release_date']","            L.append(req)"],"id":330,"ignore":true},{"start":{"row":24,"column":27},"end":{"row":26,"column":27},"action":"remove","lines":["","            L3.append(req2)","            L4.append(req3)"]}],[{"start":{"row":11,"column":20},"end":{"row":11,"column":21},"action":"insert","lines":["1"],"id":331,"ignore":true}],[{"start":{"row":11,"column":16},"end":{"row":11,"column":21},"action":"remove","lines":["list1"],"id":332,"ignore":true},{"start":{"row":11,"column":16},"end":{"row":11,"column":17},"action":"insert","lines":["t"]}],[{"start":{"row":11,"column":17},"end":{"row":11,"column":21},"action":"insert","lines":["itle"],"id":333,"ignore":true}],[{"start":{"row":19,"column":16},"end":{"row":19,"column":20},"action":"remove","lines":["list"],"id":334,"ignore":true},{"start":{"row":19,"column":16},"end":{"row":19,"column":17},"action":"insert","lines":["p"]}],[{"start":{"row":19,"column":17},"end":{"row":19,"column":19},"action":"insert","lines":["op"],"id":335,"ignore":true}],[{"start":{"row":24,"column":27},"end":{"row":25,"column":12},"action":"remove","lines":["","            "],"id":336,"ignore":true},{"start":{"row":25,"column":22},"end":{"row":25,"column":23},"action":"insert","lines":["2"]}],[{"start":{"row":27,"column":16},"end":{"row":27,"column":20},"action":"remove","lines":["list"],"id":337,"ignore":true},{"start":{"row":27,"column":16},"end":{"row":27,"column":17},"action":"insert","lines":["o"]}],[{"start":{"row":27,"column":17},"end":{"row":27,"column":21},"action":"insert","lines":["verv"],"id":338,"ignore":true}],[{"start":{"row":27,"column":21},"end":{"row":27,"column":22},"action":"insert","lines":["i"],"id":339,"ignore":true}],[{"start":{"row":27,"column":22},"end":{"row":27,"column":24},"action":"insert","lines":["ew"],"id":340,"ignore":true},{"start":{"row":30,"column":27},"end":{"row":32,"column":77},"action":"remove","lines":["","            req = requests.get(movie_url).json()['results'][i]['title']","            req1 = requests.get(movie_url).json()['results'][i]['popularity']"]},{"start":{"row":31,"column":75},"end":{"row":32,"column":79},"action":"remove","lines":["","            req3 = requests.get(movie_url).json()['results'][i]['release_date']"]}],[{"start":{"row":31,"column":75},"end":{"row":33,"column":27},"action":"remove","lines":["","            L.append(req)","            L2.append(req1)"],"id":341,"ignore":true},{"start":{"row":32,"column":27},"end":{"row":34,"column":12},"action":"remove","lines":["","            L4.append(req3)","            "]},{"start":{"row":33,"column":22},"end":{"row":33,"column":23},"action":"insert","lines":["3"]}],[{"start":{"row":35,"column":16},"end":{"row":35,"column":20},"action":"remove","lines":["list"],"id":342,"ignore":true},{"start":{"row":35,"column":16},"end":{"row":35,"column":17},"action":"insert","lines":["d"]}],[{"start":{"row":35,"column":17},"end":{"row":35,"column":20},"action":"insert","lines":["ate"],"id":343,"ignore":true},{"start":{"row":38,"column":27},"end":{"row":41,"column":75},"action":"remove","lines":["","            req = requests.get(movie_url).json()['results'][i]['title']","            req1 = requests.get(movie_url).json()['results'][i]['popularity']","            req2 = requests.get(movie_url).json()['results'][i]['overview']"]},{"start":{"row":39,"column":79},"end":{"row":42,"column":27},"action":"remove","lines":["","            L.append(req)","            L2.append(req1)","            L3.append(req2)"]}],[{"start":{"row":42,"column":22},"end":{"row":42,"column":23},"action":"insert","lines":["4"],"id":344,"ignore":true}],[{"start":{"row":40,"column":27},"end":{"row":41,"column":12},"action":"remove","lines":["","            "],"id":345,"ignore":true}],[{"start":{"row":41,"column":32},"end":{"row":57,"column":22},"action":"remove","lines":["","","with open('movielist.txt','w') as f:","    for page_num in range(1,16):","        movie_url = f\"https://api.themoviedb.org/3/movie/popular?api_key={movie_key}&language=ko-KR&page={page_num}\"","        for i in range(20):","            req = requests.get(movie_url).json()['results'][i]['title']","            req1 = requests.get(movie_url).json()['results'][i]['popularity']","            req2 = requests.get(movie_url).json()['results'][i]['overview']","            req3 = requests.get(movie_url).json()['results'][i]['release_date']","            L.append(req)","            L2.append(req1)","            L3.append(req2)","            L4.append(req3)","            ","    f.write(','.join(L)+'\\r\\n')","    print('finish', L)"],"id":346,"ignore":true}],[{"start":{"row":41,"column":32},"end":{"row":42,"column":4},"action":"insert","lines":["","    "],"id":347,"ignore":true}],[{"start":{"row":41,"column":32},"end":{"row":43,"column":4},"action":"insert","lines":["","    ","    "],"id":348,"ignore":true}],[{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"remove","lines":["    "],"id":349,"ignore":true},{"start":{"row":43,"column":0},"end":{"row":49,"column":31},"action":"insert","lines":["with open('movietitle.txt','w') as f:","    for page_num in range(1,16):","        movie_url = f\"https://api.themoviedb.org/3/movie/popular?api_key={movie_key}&language=ko-KR&page={page_num}\"","        for i in range(20):","            req = requests.get(movie_url).json()['results'][i]['title']","            L.append(req)","    f.write(','.join(L)+'\\r\\n')"]}],[{"start":{"row":10,"column":0},"end":{"row":12,"column":0},"action":"insert","lines":["L4 = []","L4 = []",""],"id":350,"ignore":true}],[{"start":{"row":10,"column":0},"end":{"row":12,"column":0},"action":"remove","lines":["L4 = []","L4 = []",""],"id":351,"ignore":true},{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["L5 = []",""]}],[{"start":{"row":50,"column":22},"end":{"row":50,"column":23},"action":"insert","lines":["5"],"id":352,"ignore":true}],[{"start":{"row":48,"column":15},"end":{"row":48,"column":16},"action":"insert","lines":["4"],"id":353,"ignore":true}],[{"start":{"row":49,"column":24},"end":{"row":49,"column":25},"action":"insert","lines":["4"],"id":354,"ignore":true}],[{"start":{"row":49,"column":13},"end":{"row":49,"column":14},"action":"insert","lines":["5"],"id":355,"ignore":true}],[{"start":{"row":48,"column":65},"end":{"row":48,"column":70},"action":"remove","lines":["title"],"id":356,"ignore":true},{"start":{"row":48,"column":65},"end":{"row":48,"column":66},"action":"insert","lines":["v"]}],[{"start":{"row":48,"column":66},"end":{"row":48,"column":68},"action":"insert","lines":["ot"],"id":357,"ignore":true}],[{"start":{"row":48,"column":68},"end":{"row":48,"column":69},"action":"insert","lines":["e"],"id":358,"ignore":true}],[{"start":{"row":48,"column":69},"end":{"row":48,"column":70},"action":"insert","lines":["_"],"id":359,"ignore":true}],[{"start":{"row":48,"column":70},"end":{"row":48,"column":71},"action":"insert","lines":["a"],"id":360,"ignore":true}],[{"start":{"row":48,"column":71},"end":{"row":48,"column":74},"action":"insert","lines":["ver"],"id":361,"ignore":true}],[{"start":{"row":48,"column":74},"end":{"row":48,"column":77},"action":"insert","lines":["age"],"id":362,"ignore":true}],[{"start":{"row":44,"column":16},"end":{"row":44,"column":21},"action":"remove","lines":["title"],"id":363,"ignore":true},{"start":{"row":44,"column":16},"end":{"row":44,"column":17},"action":"insert","lines":["v"]}],[{"start":{"row":44,"column":17},"end":{"row":44,"column":20},"action":"insert","lines":["ote"],"id":364,"ignore":true}],[{"start":{"row":17,"column":21},"end":{"row":17,"column":22},"action":"insert","lines":["s"],"id":365,"ignore":true}],[{"start":{"row":17,"column":22},"end":{"row":17,"column":24},"action":"insert","lines":["tr"],"id":366,"ignore":true}],[{"start":{"row":17,"column":24},"end":{"row":17,"column":25},"action":"insert","lines":["("],"id":367,"ignore":true}],[{"start":{"row":17,"column":29},"end":{"row":17,"column":30},"action":"insert","lines":[")"],"id":368,"ignore":true},{"start":{"row":25,"column":22},"end":{"row":25,"column":23},"action":"insert","lines":["s"]}],[{"start":{"row":25,"column":23},"end":{"row":25,"column":26},"action":"insert","lines":["tr("],"id":369,"ignore":true}],[{"start":{"row":25,"column":31},"end":{"row":25,"column":32},"action":"insert","lines":[")"],"id":370,"ignore":true},{"start":{"row":33,"column":22},"end":{"row":33,"column":23},"action":"insert","lines":["s"]}],[{"start":{"row":33,"column":23},"end":{"row":33,"column":26},"action":"insert","lines":["tr("],"id":371,"ignore":true}],[{"start":{"row":33,"column":30},"end":{"row":33,"column":31},"action":"insert","lines":[")"],"id":372,"ignore":true},{"start":{"row":41,"column":22},"end":{"row":41,"column":23},"action":"insert","lines":["s"]}],[{"start":{"row":41,"column":23},"end":{"row":41,"column":25},"action":"insert","lines":["tr"],"id":373,"ignore":true}],[{"start":{"row":41,"column":25},"end":{"row":41,"column":26},"action":"insert","lines":["("],"id":374,"ignore":true}],[{"start":{"row":41,"column":30},"end":{"row":41,"column":31},"action":"insert","lines":[")"],"id":375,"ignore":true}],[{"start":{"row":49,"column":21},"end":{"row":49,"column":22},"action":"insert","lines":["s"],"id":376,"ignore":true}],[{"start":{"row":49,"column":22},"end":{"row":49,"column":24},"action":"insert","lines":["tr"],"id":377,"ignore":true}],[{"start":{"row":49,"column":21},"end":{"row":49,"column":24},"action":"remove","lines":["str"],"id":378,"ignore":true}],[{"start":{"row":49,"column":22},"end":{"row":49,"column":25},"action":"insert","lines":["str"],"id":379,"ignore":true}],[{"start":{"row":49,"column":25},"end":{"row":49,"column":26},"action":"insert","lines":["("],"id":380,"ignore":true}],[{"start":{"row":49,"column":31},"end":{"row":49,"column":32},"action":"insert","lines":[")"],"id":381,"ignore":true}]]},"ace":{"folds":[],"scrolltop":413.5,"scrollleft":0,"selection":{"start":{"row":48,"column":32},"end":{"row":48,"column":32},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":28,"state":"start","mode":"ace/mode/python"}},"timestamp":1557660023540,"hash":"e8f38b5d5f99590b02435ba62071295e196c9591"}