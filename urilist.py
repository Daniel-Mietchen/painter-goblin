#!/usr/bin/python
# -*- coding: utf-8 -*-

wikilist = ["http://www.wikidata.org/entity/Q27940903",
            "http://www.wikidata.org/entity/Q36462498",
            "http://www.wikidata.org/entity/Q23948827",
            "http://www.wikidata.org/entity/Q23688133",
            "http://www.wikidata.org/entity/Q28060542",
            "http://www.wikidata.org/entity/Q16297453",
            "http://www.wikidata.org/entity/Q41251774",
            "http://www.wikidata.org/entity/Q29545293",
            "http://www.wikidata.org/entity/Q27516246",
            "http://www.wikidata.org/entity/Q27516247",
            "http://www.wikidata.org/entity/Q19861793",
            "http://www.wikidata.org/entity/Q29535404",
            "http://www.wikidata.org/entity/Q28796449",
            "http://www.wikidata.org/entity/Q10315035",
            "http://www.wikidata.org/entity/Q28796526",
            "http://www.wikidata.org/entity/Q29635239",
            "http://www.wikidata.org/entity/Q28796441",
            "http://www.wikidata.org/entity/Q17141031",
            "http://www.wikidata.org/entity/Q17323866",
            "http://www.wikidata.org/entity/Q28796447",
            "http://www.wikidata.org/entity/Q17323862",
            "http://www.wikidata.org/entity/Q17319955",
            "http://www.wikidata.org/entity/Q36449823",
            "http://www.wikidata.org/entity/Q17319951",
            "http://www.wikidata.org/entity/Q23008884",
            "http://www.wikidata.org/entity/Q27513033",
            "http://www.wikidata.org/entity/Q17334748",
            "http://www.wikidata.org/entity/Q29642256",
            "http://www.wikidata.org/entity/Q28795942",
            "http://www.wikidata.org/entity/Q17627609",
            "http://www.wikidata.org/entity/Q28772809",
            "http://www.wikidata.org/entity/Q28796628",
            "http://www.wikidata.org/entity/Q29640678",
            "http://www.wikidata.org/entity/Q28796624",
            "http://www.wikidata.org/entity/Q29640675",
            "http://www.wikidata.org/entity/Q28796626",
            "http://www.wikidata.org/entity/Q18688242",
            "http://www.wikidata.org/entity/Q18688243",
            "http://www.wikidata.org/entity/Q17627376",
            "http://www.wikidata.org/entity/Q21614079",
            "http://www.wikidata.org/entity/Q20175110",
            "http://www.wikidata.org/entity/Q27954954",
            "http://www.wikidata.org/entity/Q27513109",
            "http://www.wikidata.org/entity/Q18627419",
            "http://www.wikidata.org/entity/Q3788158",
            "http://www.wikidata.org/entity/Q29641998",
            "http://www.wikidata.org/entity/Q27513104",
            "http://www.wikidata.org/entity/Q29855494",
            "http://www.wikidata.org/entity/Q29550504",
            "http://www.wikidata.org/entity/Q18686020",
            "http://www.wikidata.org/entity/Q20440516",
            "http://www.wikidata.org/entity/Q28837089",
            "http://www.wikidata.org/entity/Q18719670",
            "http://www.wikidata.org/entity/Q18627849",
            "http://www.wikidata.org/entity/Q27505831",
            "http://www.wikidata.org/entity/Q27766332",
            "http://www.wikidata.org/entity/Q41251959",
            "http://www.wikidata.org/entity/Q29582752",
            "http://www.wikidata.org/entity/Q18748849",
            "http://www.wikidata.org/entity/Q23039033",
            "http://www.wikidata.org/entity/Q22085258",
            "http://www.wikidata.org/entity/Q24039982",
            "http://www.wikidata.org/entity/Q27576290",
            "http://www.wikidata.org/entity/Q18573337",
            "http://www.wikidata.org/entity/Q18551900",
            "http://www.wikidata.org/entity/Q18627852",
            "http://www.wikidata.org/entity/Q33701431",
            "http://www.wikidata.org/entity/Q6057356",
            "http://www.wikidata.org/entity/Q29549917",
            "http://www.wikidata.org/entity/Q29549696",
            "http://www.wikidata.org/entity/Q28043622",
            "http://www.wikidata.org/entity/Q29582604",
            "http://www.wikidata.org/entity/Q29384077",
            "http://www.wikidata.org/entity/Q29644874",
            "http://www.wikidata.org/entity/Q22274376",
            "http://www.wikidata.org/entity/Q18627381",
            "http://www.wikidata.org/entity/Q19913913",
            "http://www.wikidata.org/entity/Q21703185",
            "http://www.wikidata.org/entity/Q18627387",
            "http://www.wikidata.org/entity/Q29642478",
            "http://www.wikidata.org/entity/Q17324590",
            "http://www.wikidata.org/entity/Q18689402",
            "http://www.wikidata.org/entity/Q18689401",
            "http://www.wikidata.org/entity/Q17341255",
            "http://www.wikidata.org/entity/Q3535485",
            "http://www.wikidata.org/entity/Q18689536",
            "http://www.wikidata.org/entity/Q29863369",
            "http://www.wikidata.org/entity/Q29642670",
            "http://www.wikidata.org/entity/Q20198062",
            "http://www.wikidata.org/entity/Q25714729",
            "http://www.wikidata.org/entity/Q19912462",
            "http://www.wikidata.org/entity/Q19912467",
            "http://www.wikidata.org/entity/Q29535328",
            "http://www.wikidata.org/entity/Q29642836",
            "http://www.wikidata.org/entity/Q17189257",
            "http://www.wikidata.org/entity/Q27862472",
            "http://www.wikidata.org/entity/Q11801539",
            "http://www.wikidata.org/entity/Q17321733",
            "http://www.wikidata.org/entity/Q18339640",
            "http://www.wikidata.org/entity/Q28796570",
            "http://www.wikidata.org/entity/Q27513072",
            "http://www.wikidata.org/entity/Q27513073",
            "http://www.wikidata.org/entity/Q28796478",
            "http://www.wikidata.org/entity/Q17334578",
            "http://www.wikidata.org/entity/Q36463368",
            "http://www.wikidata.org/entity/Q23936127",
            "http://www.wikidata.org/entity/Q21645956",
            "http://www.wikidata.org/entity/Q28795878",
            " http://www.wikidata.org/entity/Q24136530",
            "http://www.wikidata.org/entity/Q18605938",
            "http://www.wikidata.org/entity/Q28795873",
            "http://www.wikidata.org/entity/Q29630316",
            "http://www.wikidata.org/entity/Q17320881",
            "http://www.wikidata.org/entity/Q29642696",
            "http://www.wikidata.org/entity/Q9375308",
            "http://www.wikidata.org/entity/Q20173206",
            "http://www.wikidata.org/entity/Q17320888",
            "http://www.wikidata.org/entity/Q27574266",
            "http://www.wikidata.org/entity/Q29549721",
            "http://www.wikidata.org/entity/Q19826812",
            "http://www.wikidata.org/entity/Q17323863",
            "http://www.wikidata.org/entity/Q28796351",
            "http://www.wikidata.org/entity/Q18683045",
            "http://www.wikidata.org/entity/Q18598467",
            "http://www.wikidata.org/entity/Q23641353",
            "http://www.wikidata.org/entity/Q31202751",
            "http://www.wikidata.org/entity/Q27513153",
            "http://www.wikidata.org/entity/Q18627447",
            "http://www.wikidata.org/entity/Q18627446",
            "http://www.wikidata.org/entity/Q18627445",
            "http://www.wikidata.org/entity/Q18627444",
            "http://www.wikidata.org/entity/Q28795802",
            "http://www.wikidata.org/entity/Q29509004",
            "http://www.wikidata.org/entity/Q18599629",
            "http://www.wikidata.org/entity/Q20087072",
            "http://www.wikidata.org/entity/Q20087071",
            "http://www.wikidata.org/entity/Q29591750",
            "http://www.wikidata.org/entity/Q29535145",
            "http://www.wikidata.org/entity/Q19165528",
            "http://www.wikidata.org/entity/Q576239",
            "http://www.wikidata.org/entity/Q18602450",
            "http://www.wikidata.org/entity/Q18602452",
            "http://www.wikidata.org/entity/Q18602455",
            "http://www.wikidata.org/entity/Q3546969",
            "http://www.wikidata.org/entity/Q18890807",
            "http://www.wikidata.org/entity/Q24049250",
            "http://www.wikidata.org/entity/Q29881716",
            "http://www.wikidata.org/entity/Q19912425",
            "http://www.wikidata.org/entity/Q27696878",
            "http://www.wikidata.org/entity/Q18687857",
            "http://www.wikidata.org/entity/Q29582736",
            "http://www.wikidata.org/entity/Q20179455",
            "http://www.wikidata.org/entity/Q18683789",
            "http://www.wikidata.org/entity/Q29535369",
            "http://www.wikidata.org/entity/Q22914523",
            "http://www.wikidata.org/entity/Q19930626",
            "http://www.wikidata.org/entity/Q29565402",
            "http://www.wikidata.org/entity/Q24694977",
            "http://www.wikidata.org/entity/Q17329662",
            "http://www.wikidata.org/entity/Q28796434",
            "http://www.wikidata.org/entity/Q18689275",
            "http://www.wikidata.org/entity/Q28796432",
            "http://www.wikidata.org/entity/Q18689176",
            "http://www.wikidata.org/entity/Q23906751",
            "http://www.wikidata.org/entity/Q28059974",
            "http://www.wikidata.org/entity/Q29642266",
            "http://www.wikidata.org/entity/Q22915359",
            "http://www.wikidata.org/entity/Q20182142",
            "http://www.wikidata.org/entity/Q28665891",
            "http://www.wikidata.org/entity/Q23681758",
            "http://www.wikidata.org/entity/Q20175280",
            "http://www.wikidata.org/entity/Q18688258",
            "http://www.wikidata.org/entity/Q23936467",
            "http://www.wikidata.org/entity/Q20772006",
            "http://www.wikidata.org/entity/Q12032120",
            "http://www.wikidata.org/entity/Q29545803",
            "http://www.wikidata.org/entity/Q28038491",
            "http://www.wikidata.org/entity/Q21614060",
            "http://www.wikidata.org/entity/Q28796548",
            "http://www.wikidata.org/entity/Q19961443",
            "http://www.wikidata.org/entity/Q18689399",
            "http://www.wikidata.org/entity/Q18627409",
            "http://www.wikidata.org/entity/Q18627404",
            "http://www.wikidata.org/entity/Q27513112",
            "http://www.wikidata.org/entity/Q19883416",
            "http://www.wikidata.org/entity/Q19883419",
            "http://www.wikidata.org/entity/Q29621924",
            "http://www.wikidata.org/entity/Q26224030",
            "http://www.wikidata.org/entity/Q26220234",
            "http://www.wikidata.org/entity/Q27574280",
            "http://www.wikidata.org/entity/Q28796642",
            "http://www.wikidata.org/entity/Q29630055",
            "http://www.wikidata.org/entity/Q20022415",
            "http://www.wikidata.org/entity/Q18683361",
            "http://www.wikidata.org/entity/Q29904372",
            "http://www.wikidata.org/entity/Q29535065",
            "http://www.wikidata.org/entity/Q17340547",
            "http://www.wikidata.org/entity/Q27513169",
            "http://www.wikidata.org/entity/Q28945682",
            "http://www.wikidata.org/entity/Q29623418",
            "http://www.wikidata.org/entity/Q17322796",
            "http://www.wikidata.org/entity/Q27513166",
            "http://www.wikidata.org/entity/Q18602463",
            "http://www.wikidata.org/entity/Q19904631",
            "http://www.wikidata.org/entity/Q20808326",
            "http://www.wikidata.org/entity/Q29642330",
            "http://www.wikidata.org/entity/Q18627391",
            "http://www.wikidata.org/entity/Q18627390",
            "http://www.wikidata.org/entity/Q18627396",
            "http://www.wikidata.org/entity/Q21723204",
            "http://www.wikidata.org/entity/Q19883381",
            "http://www.wikidata.org/entity/Q20167086",
            "http://www.wikidata.org/entity/Q17329830",
            "http://www.wikidata.org/entity/Q29535192",
            "http://www.wikidata.org/entity/Q17341531",
            "http://www.wikidata.org/entity/Q11824918",
            "http://www.wikidata.org/entity/Q29581580",
            "http://www.wikidata.org/entity/Q17319983",
            "http://www.wikidata.org/entity/Q29634372",
            "http://www.wikidata.org/entity/Q24136530",
            "http://www.wikidata.org/entity/Q29881723",
            "http://www.wikidata.org/entity/Q3997721",
            "http://www.wikidata.org/entity/Q27514784",
            "http://www.wikidata.org/entity/Q19912525",
            "http://www.wikidata.org/entity/Q18627442",
            "http://www.wikidata.org/entity/Q19925574",
            "http://www.wikidata.org/entity/Q29635653",
            "http://www.wikidata.org/entity/Q4212198",
            "http://www.wikidata.org/entity/Q29545273",
            "http://www.wikidata.org/entity/Q17275871",
            "http://www.wikidata.org/entity/Q27697586",
            "http://www.wikidata.org/entity/Q29549395",
            "http://www.wikidata.org/entity/Q18688219",
            "http://www.wikidata.org/entity/Q19262623",
            "http://www.wikidata.org/entity/Q42298153",
            "http://www.wikidata.org/entity/Q19162685",
            "http://www.wikidata.org/entity/Q27513060",
            "http://www.wikidata.org/entity/Q27513062",
            "http://www.wikidata.org/entity/Q23008897",
            "http://www.wikidata.org/entity/Q28796468",
            "http://www.wikidata.org/entity/Q29582952",
            "http://www.wikidata.org/entity/Q29509642",
            "http://www.wikidata.org/entity/Q27038735",
            "http://www.wikidata.org/entity/Q20165836",
            "http://www.wikidata.org/entity/Q22915388",
            "http://www.wikidata.org/entity/Q28654270",
            "http://www.wikidata.org/entity/Q27574273",
            "http://www.wikidata.org/entity/Q28796606",
            "http://www.wikidata.org/entity/Q20064495",
            "http://www.wikidata.org/entity/Q28803793",
            "http://www.wikidata.org/entity/Q18627413",
            "http://www.wikidata.org/entity/Q36466806",
            "http://www.wikidata.org/entity/Q27513121",
            "http://www.wikidata.org/entity/Q29509546",
            "http://www.wikidata.org/entity/Q9370562",
            "http://www.wikidata.org/entity/Q28796514",
            "http://www.wikidata.org/entity/Q18684890",
            "http://www.wikidata.org/entity/Q26221271",
            "http://www.wikidata.org/entity/Q18627421",
            "http://www.wikidata.org/entity/Q20891251",
            "http://www.wikidata.org/entity/Q11451054",
            "http://www.wikidata.org/entity/Q20776141",
            "http://www.wikidata.org/entity/Q28073467",
            "http://www.wikidata.org/entity/Q18684738",
            "http://www.wikidata.org/entity/Q17329972",
            "http://www.wikidata.org/entity/Q27576275",
            "http://www.wikidata.org/entity/Q27576277",
            "http://www.wikidata.org/entity/Q18684730",
            "http://www.wikidata.org/entity/Q17329873",
            "http://www.wikidata.org/entity/Q19859031",
            "http://www.wikidata.org/entity/Q19766300",
            "http://www.wikidata.org/entity/Q20187081",
            "http://www.wikidata.org/entity/Q23928863",
            "http://www.wikidata.org/entity/Q14849952",
            "http://www.wikidata.org/entity/Q29642402",
            "http://www.wikidata.org/entity/Q28771793",
            "http://www.wikidata.org/entity/Q18687847",
            "http://www.wikidata.org/entity/Q29384057",
            "http://www.wikidata.org/entity/Q18683131",
            "http://www.wikidata.org/entity/Q7485590",
            "http://www.wikidata.org/entity/Q18683255",
            "http://www.wikidata.org/entity/Q19912117",
            "http://www.wikidata.org/entity/Q20880358",
            "http://www.wikidata.org/entity/Q19912445",
            "http://www.wikidata.org/entity/Q29642494",
            "http://www.wikidata.org/entity/Q19912449",
            "http://www.wikidata.org/entity/Q19912448",
            "http://www.wikidata.org/entity/Q17340714",
            "http://www.wikidata.org/entity/Q6485127",
            "http://www.wikidata.org/entity/Q6485128",
            "http://www.wikidata.org/entity/Q37117194",
            "http://www.wikidata.org/entity/Q18573819",
            "http://www.wikidata.org/entity/Q2453980",
            "http://www.wikidata.org/entity/Q11771568",
            "http://www.wikidata.org/entity/Q18689261",
            "http://www.wikidata.org/entity/Q43247781",
            "http://www.wikidata.org/entity/Q41135980",
            "http://www.wikidata.org/entity/Q23590398",
            "http://www.wikidata.org/entity/Q29642658",
            "http://www.wikidata.org/entity/Q29636643",
            "http://www.wikidata.org/entity/Q17346894",
            "http://www.wikidata.org/entity/Q27616510",
            "http://www.wikidata.org/entity/Q29642270",
            "http://www.wikidata.org/entity/Q1300406",
            "http://www.wikidata.org/entity/Q28795894",
            "http://www.wikidata.org/entity/Q22340085",
            "http://www.wikidata.org/entity/Q29642376",
            "http://www.wikidata.org/entity/Q28831555",
            "http://www.wikidata.org/entity/Q29642787",
            "http://www.wikidata.org/entity/Q21523425",
            "http://www.wikidata.org/entity/Q27574335",
            "http://www.wikidata.org/entity/Q2925123",
            "http://www.wikidata.org/entity/Q28796553",
            "http://www.wikidata.org/entity/Q29549750",
            "http://www.wikidata.org/entity/Q23611541",
            "http://www.wikidata.org/entity/Q29646152",
            "http://www.wikidata.org/entity/Q27513054",
            "http://www.wikidata.org/entity/Q29543117",
            "http://www.wikidata.org/entity/Q27513056",
            "http://www.wikidata.org/entity/Q3221348",
            "http://www.wikidata.org/entity/Q19858726",
            "http://www.wikidata.org/entity/Q20267966",
            "http://www.wikidata.org/entity/Q29634919",
            "http://www.wikidata.org/entity/Q18627437",
            "http://www.wikidata.org/entity/Q28822736",
            "http://www.wikidata.org/entity/Q18627439",
            "http://www.wikidata.org/entity/Q29534050",
            "http://www.wikidata.org/entity/Q17505798",
            "http://www.wikidata.org/entity/Q28795850",
            "http://www.wikidata.org/entity/Q28795917",
            "http://www.wikidata.org/entity/Q29630193",
            "http://www.wikidata.org/entity/Q28795859",
            "http://www.wikidata.org/entity/Q20487895",
            "http://www.wikidata.org/entity/Q22809405",
            "http://www.wikidata.org/entity/Q19924804",
            "http://www.wikidata.org/entity/Q28912422",
            "http://www.wikidata.org/entity/Q17321112",
            "http://www.wikidata.org/entity/Q30067996",
            "http://www.wikidata.org/entity/Q20064449",
            "http://www.wikidata.org/entity/Q28796678",
            "http://www.wikidata.org/entity/Q20054562",
            "http://www.wikidata.org/entity/Q28796600",
            "http://www.wikidata.org/entity/Q28797959",
            "http://www.wikidata.org/entity/Q23936299",
            "http://www.wikidata.org/entity/Q27574299",
            "http://www.wikidata.org/entity/Q24090417",
            "http://www.wikidata.org/entity/Q29610271",
            "http://www.wikidata.org/entity/Q22912347",
            "http://www.wikidata.org/entity/Q20797422",
            "http://www.wikidata.org/entity/Q20706775",
            "http://www.wikidata.org/entity/Q29384016",
            "http://www.wikidata.org/entity/Q28938506",
            "http://www.wikidata.org/entity/Q31201203",
            "http://www.wikidata.org/entity/Q30096006",
            "http://www.wikidata.org/entity/Q18688354",
            "http://www.wikidata.org/entity/Q24049055",
            "http://www.wikidata.org/entity/Q20735378",
            "http://www.wikidata.org/entity/Q17320884",
            "http://www.wikidata.org/entity/Q17320885",
            "http://www.wikidata.org/entity/Q18684775",
            "http://www.wikidata.org/entity/Q3937622",
            "http://www.wikidata.org/entity/Q28802761",
            "http://www.wikidata.org/entity/Q28945778",
            "http://www.wikidata.org/entity/Q18601931",
            "http://www.wikidata.org/entity/Q28945784",
            "http://www.wikidata.org/entity/Q17341229",
            "http://www.wikidata.org/entity/Q21725241",
            "http://www.wikidata.org/entity/Q616159",
            "http://www.wikidata.org/entity/Q29881714",
            "http://www.wikidata.org/entity/Q29582710",
            "http://www.wikidata.org/entity/Q17330660",
            "http://www.wikidata.org/entity/Q29642625",
            "http://www.wikidata.org/entity/Q22047725",
            "http://www.wikidata.org/entity/Q26493322",
            "http://www.wikidata.org/entity/Q18683193",
            "http://www.wikidata.org/entity/Q11918704",
            "http://www.wikidata.org/entity/Q20880819",
            "http://www.wikidata.org/entity/Q18683194",
            "http://www.wikidata.org/entity/Q29973418",
            "http://www.wikidata.org/entity/Q19882675",
            "http://www.wikidata.org/entity/Q28796513",
            "http://www.wikidata.org/entity/Q18689351",
            "http://www.wikidata.org/entity/Q18689216",
            "http://www.wikidata.org/entity/Q29534460",
            "http://www.wikidata.org/entity/Q17323479",
            "http://www.wikidata.org/entity/Q20178795",
            "http://www.wikidata.org/entity/Q23008937",
            "http://www.wikidata.org/entity/Q28796686",
            "http://www.wikidata.org/entity/Q20188403",
            "http://www.wikidata.org/entity/Q33990452",
            "http://www.wikidata.org/entity/Q25710737",
            "http://www.wikidata.org/entity/Q18627456",
            "http://www.wikidata.org/entity/Q29645084",
            "http://www.wikidata.org/entity/Q17491014",
            "http://www.wikidata.org/entity/Q21614000",
            "http://www.wikidata.org/entity/Q23199649",
            "http://www.wikidata.org/entity/Q29565771",
            "http://www.wikidata.org/entity/Q28796336",
            "http://www.wikidata.org/entity/Q28798197",
            "http://www.wikidata.org/entity/Q22912656",
            "http://www.wikidata.org/entity/Q20891212",
            "http://www.wikidata.org/entity/Q27513131",
            "http://www.wikidata.org/entity/Q22915286",
            "http://www.wikidata.org/entity/Q19925732",
            "http://www.wikidata.org/entity/Q27980399",
            "http://www.wikidata.org/entity/Q22915280",
            "http://www.wikidata.org/entity/Q20087119",
            "http://www.wikidata.org/entity/Q7960534",
            "http://www.wikidata.org/entity/Q20087117",
            "http://www.wikidata.org/entity/Q28043442",
            "http://www.wikidata.org/entity/Q19925036",
            "http://www.wikidata.org/entity/Q28796492",
            "http://www.wikidata.org/entity/Q20188018",
            "http://www.wikidata.org/entity/Q27576283",
            "http://www.wikidata.org/entity/Q18683024",
            "http://www.wikidata.org/entity/Q23700588",
            "http://www.wikidata.org/entity/Q3209564",
            "http://www.wikidata.org/entity/Q29384079",
            "http://www.wikidata.org/entity/Q29641968",
            "http://www.wikidata.org/entity/Q17320879",
            "http://www.wikidata.org/entity/Q29384167",
            "http://www.wikidata.org/entity/Q27572735",
            "http://www.wikidata.org/entity/Q27572737",
            "http://www.wikidata.org/entity/Q29384044",
            "http://www.wikidata.org/entity/Q21725118",
            "http://www.wikidata.org/entity/Q29384048",
            "http://www.wikidata.org/entity/Q20198419",
            "http://www.wikidata.org/entity/Q19912476",
            "http://www.wikidata.org/entity/Q23648121",
            "http://www.wikidata.org/entity/Q28790535",
            "http://www.wikidata.org/entity/Q19924428",
            "http://www.wikidata.org/entity/Q17329699",
            "http://www.wikidata.org/entity/Q19912471",
            "http://www.wikidata.org/entity/Q28796555",
            "http://www.wikidata.org/entity/Q17329691",
            "http://www.wikidata.org/entity/Q19925420",
            "http://www.wikidata.org/entity/Q29565426",
            "http://www.wikidata.org/entity/Q19960835",
            "http://www.wikidata.org/entity/Q17319968",
            "http://www.wikidata.org/entity/Q17319964",
            "http://www.wikidata.org/entity/Q23008898",
            "http://www.wikidata.org/entity/Q17327475",
            "http://www.wikidata.org/entity/Q12858354",
            "http://www.wikidata.org/entity/Q11869499",
            "http://www.wikidata.org/entity/Q17334673",
            "http://www.wikidata.org/entity/Q17334676",
            "http://www.wikidata.org/entity/Q29592321",
            "http://www.wikidata.org/entity/Q19660506",
            "http://www.wikidata.org/entity/Q29535047",
            "http://www.wikidata.org/entity/Q12079797",
            "http://www.wikidata.org/entity/Q18602217",
            "http://www.wikidata.org/entity/Q18683800",
            "http://www.wikidata.org/entity/Q29635176",
            "http://www.wikidata.org/entity/Q28796566",
            "http://www.wikidata.org/entity/Q3815174",
            "http://www.wikidata.org/entity/Q28796480",
            "http://www.wikidata.org/entity/Q10541152",
            "http://www.wikidata.org/entity/Q28796482",
            "http://www.wikidata.org/entity/Q18627424",
            "http://www.wikidata.org/entity/Q18686019",
            "http://www.wikidata.org/entity/Q18686018",
            "http://www.wikidata.org/entity/Q29642515",
            "http://www.wikidata.org/entity/Q29383039",
            "http://www.wikidata.org/entity/Q28795904",
            "http://www.wikidata.org/entity/Q28795907",
            "http://www.wikidata.org/entity/Q29908875",
            "http://www.wikidata.org/entity/Q29621531",
            "http://www.wikidata.org/entity/Q29535015",
            "http://www.wikidata.org/entity/Q18601638",
            "http://www.wikidata.org/entity/Q26221326",
            "http://www.wikidata.org/entity/Q28796664",
            "http://www.wikidata.org/entity/Q20178705",
            "http://www.wikidata.org/entity/Q17331175",
            "http://www.wikidata.org/entity/Q29645873",
            "http://www.wikidata.org/entity/Q19825948",
            "http://www.wikidata.org/entity/Q18686266",
            "http://www.wikidata.org/entity/Q28796342",
            "http://www.wikidata.org/entity/Q29549256",
            "http://www.wikidata.org/entity/Q19609369",
            "http://www.wikidata.org/entity/Q18627451",
            "http://www.wikidata.org/entity/Q18627452",
            "http://www.wikidata.org/entity/Q18685961",
            "http://www.wikidata.org/entity/Q28584657",
            "http://www.wikidata.org/entity/Q19899783",
            "http://www.wikidata.org/entity/Q27981885",
            "http://www.wikidata.org/entity/Q27513141",
            "http://www.wikidata.org/entity/Q29914187",
            "http://www.wikidata.org/entity/Q29644941",
            "http://www.wikidata.org/entity/Q29578945",
            "http://www.wikidata.org/entity/Q29621890",
            "http://www.wikidata.org/entity/Q20179330",
            "http://www.wikidata.org/entity/Q24306839",
            "http://www.wikidata.org/entity/Q19904615",
            "http://www.wikidata.org/entity/Q27766024"]
