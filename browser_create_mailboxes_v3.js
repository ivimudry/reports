// ============================================
// СКРИПТ v3 — СТВОРЕННЯ ПОШТОВИХ СКРИНЬОК
// Вставте у консоль браузера (F12 → Console)
// будучи залогіненим у ISPmanager
// ============================================

const mailboxes = [
["alexander746","DC4b6P9JCzQAkWvx"],
["henderson15","ownov7kKF5AmAf3e"],
["l.reed","xXPD5pZSrR4S24Sx"],
["r.harris","vo8Beejt75TtZNYq"],
["dean550","qvCGE8wcXqTk3et5"],
["seanh","3icbKH3wQiuyo3TJ"],
["logan992","9yK8JzxE2Jh2q536"],
["martin.adams","JMvu7aPXwXFwYkiX"],
["wesley.bennett","JeR5SdpBvDVXfUKS"],
["adrians","9vGr4zFG3gSSUcH9"],
["d.henderson","uzXPsvihk8BGn4Jf"],
["anthonyw","WebXPkyTGpEiU3Dz"],
["grahamm","m6UUuqNbTqPuwJS2"],
["powell77","kR6HwZZ3qsnUpHrJ"],
["ward1","GQPP44BNDLN9vYSB"],
["holland19","BGBu7CAghtpLC5X2"],
["frank.johnson","5UJ6aqkkxaXEDv9Z"],
["keith430","7HMV7Kd4NAsL9h5f"],
["wood57","HYr76E2fyrwsmPYy"],
["colinh","6kEtsLFbjsurTu8q"],
["johnnyc","bD3w8aWAMHFy7PiJ"],
["dean967","dRNMf4p8kdbhzQvE"],
["graham.williams","PeNdRSbdVeaFyQjY"],
["zachary.kim","EvkmVRNvz7otV2CM"],
["mateop","Q8NCd2p2kHf3MPb8"],
["blake.norton","bumHdJVii7KV7qMP"],
["parkerr","RuN4ZZPVuoScagtm"],
["chandler59","vsS4utgZPLz7s72r"],
["nicholas727","RsfKFPb4brG3pnMq"],
["colton.davis","BfFeu64wZn8FCMLe"],
["lance.anderson","69q4oNn54ouyR8LW"],
["l.coleman","4koY3Dfz6LGBBbm6"],
["zachary188","QPLmhHubpUdqqCuu"],
["a.cooper","9gUNLCCjSm6XutDu"],
["grant.perez","sBQKf5j4Q6fqHk2e"],
["logan358","GBh3iNQwhZTAqjqg"],
["billy390","9odShVXzgRmbvNVo"],
["garcia84","o4pCZxq2oomMMQsG"],
["turner51","78G8mhDjHXSJbuCB"],
["fleming71","EMoQHP2nbafW8LWN"],
["anthony108","pWzVGugrUtK7aGbM"],
["chandler.roberts","hn8MVeWRAj4P7Sv2"],
["dylan.sullivan","VEUsuXJy44FomUZB"],
["troy.kelly","QjPtGNG9GoFAL82L"],
["robert.lynch","tKzLY4Z5DieFCcKP"],
["noah.nelson","U9iEopL2cJcDMu4u"],
["v.scott","a34s7RxdPrTQF6h4"],
["hart41","sXPPUU2ofgd3e2iL"],
["jonathan527","fB8ym7UXodiVGUJu"],
["steven.morrison","tH8haN5TUXw5htLx"],
["l.allen","iwaRNq4xUofdmsuR"],
["pault","ntxpjjrFFbhK373h"],
["finleyl","dGwT2BkTQAHw2BFP"],
["jeffrey.rodriguez","XU7ePfuivPK8v7ub"],
["clay.cox","UaAKg6Wo5Nx5itwL"],
["graham.doyle","r2EivrwajB7SwEWF"],
["ivans","TfjFDYSTpDUZ43WQ"],
["max.porter","3hqtLVYEYFB8fJEa"],
["dalton525","RzUd3fpz4S76BRvL"],
["david292","YKUMUdHtYjrHM7Fj"],
["julian.porter","VTMCnQYyawdASS7k"],
["peter.cook","HCqChtxisrFgzQVr"],
["mason37","yems4TUDtqJmusYr"],
["trentg","VUMWPvCXu888dky7"],
["gonzalez73","ESbMAUZC85YM4ELb"],
["adam.walsh","aYiV4QAHWKHNfS5B"],
["leonard234","PczkGr4gXRA8x2wv"],
["jimenez73","jmvHWHTyucqUSakc"],
["dawsonc","RzEjJwseDETfdsFz"],
["stanley169","D2iTokixyVKmM6bE"],
["tuckerp","8TQhdNhaTqiARYt2"],
["warrenk","EseXXK6mzDDSoMWC"],
["timothy705","GeqfTyE8PS5QPfjz"],
["c.ford","b5if6rFdCaSQSTWf"],
["foster831","xh2MBXFKnCca2GLo"],
["martinw","hCyTvBJQ7cJCSXcf"],
["foster.scott","ctbgGq3EfTrxxEaU"],
["dawson468","vYAZysev2gbEYDgW"],
["keith.robinson","pHMMJM4e7cKWhSE8"],
["grant.wilson","jYii2dCn7ga5NSB7"],
["victor524","hc7J5u6FbjuiMWW7"],
["graham.bailey","jTFcW3D8AewrPout"],
["victor.walker","g8MMvru4NhFeWbqE"],
["s.hernandez","pz3FRYCH3ndEtTDZ"],
["ortiz15","kHbJX4bisTLnSpM3"],
["gabriel.rodriguez","RPkUeMd8wR8BsBJk"],
["jamesw","ZbwdM3ApiiTgovRF"],
["oliverf","wBjyY3oBFdXcgQoP"],
["r.parker","KxDo2UgvNkppxFhK"],
["r.walker","twg9jGZh5SDPqphd"],
["richard510","yK7ELd7sVsVyaGSF"],
["carterh","dkzKinPHqEViQgka"],
["brandonp","JgMBweXPkVHpkhX3"],
["robert.roberts","Wa3Rxgn5EzqfUdgZ"],
["paul.long","3MiGWqHTinkfzTrw"],
["felixa","FGqLZvoTjoHGwtYH"],
["holland83","PR4MYrzuwT7Gym3j"],
["j.cooper","p9e2VN7ZrB6tWp6E"],
["brycec","sqM7ebkjRS3aZQHF"],
["caleb.bowen","mgHggM3ptxtk7tSv"],
["k.fuller","vMqbmeBWSiBdKt35"],
["liam258","Yen7HXbKyCFWJwBA"],
["wesley.diaz","i78KQbTjv69k8eWW"],
["r.sullivan","j75DXD9VNqpWchS5"],
["gomez3","M3tVGWMzcpetRQTT"],
["pierce.rogers","swXaKNBKkSQQJQWp"],
["trevorg","A8wtTCooKmfnbFSd"],
["clarence.clark","ihyVrYCSuhQcKXpb"],
["walter532","zFVNjdAMs3KnCyKj"],
["bennett6","WwiJmMpcMFLTDrvH"],
["vance947","Dk7Q9GoQpGbRSAKS"],
["wayne147","tLLZ3B2xLZobBFD2"],
["v.burke","jr3sFoN6SNRM5qaB"],
["grantw","kd5KeQG2qLLBPahC"],
["hernandez29","4N9r7ZxFfgMNEGmH"],
["mateo.williams","56gkCLpvyq25NMwm"],
["coleman34","zk4RYzJc5QQgfyja"],
["phillip686","YghneGHduMkJm9zg"],
["shane.palmer","8X3rn3LyBydAt86F"],
["wells36","WMB7j9riopf2nkaq"],
["vincent.gray","xcjmyhgRhPFUwwEq"],
["chandler149","4A4JdP8Rrf2bC5ne"],
["mark.bailey","m7gqhKXyziYqtxVG"],
["deanb","7hv4q5FFNj3Wf2Le"],
["wesleyk","yY8dgKNyyrLfVGT3"],
["dylanw","JZXXyvdogrCT3LpZ"],
["norton89","kNDfZ8Q9XvmAYfSa"],
["gerald.williams","RWnGB7v852XD9Ww5"],
["reed.white","tf9FGgo4T7NhaiLA"],
["douglas.norton","9fTzrAs3qHPdU23q"],
["jesse.gomez","RDroMXkFDATxNkXZ"],
["edward.duncan","LT8wxxqAoYPHzxco"],
["victor.alexander","eiAhFYdrFTPjCFLP"],
["alan.gutierrez","WRque3iJEQfu8DAq"],
["eric.johnson","bj3vsv6uoQmG9bti"],
["david.jones","EZdNA6fJfQ9iTTDD"],
["phillip.ruiz","RjmB6TY7HwNNeTAy"],
["dawson.russell","KH3QzbNQDYakfAHN"],
["simmons12","2sZ4UAz3EoRu6WXp"],
["albert833","V92XHywCq2HWzL48"],
["larry995","JBpR5gaJ2NxWCut8"],
["terry318","WQj6JsRjd9vKEzTT"],
["kyle169","gvBesPcVWXjagqia"],
["codyw","ccrZttVr75ZPG3TC"],
["colin.sanchez","WUSFUPv5G5pjLV2h"],
["richard168","Lw4tbSFhnijtJY29"],
["brooks7","6FdvG4RaWHEzc9sX"],
["ralph339","joGXJx5YD8GcQXrF"],
["nash861","W4E6Z5iwNGLuekjr"],
["gregory87","mGbptgSsH4d76Z9z"],
["jack.parker","NuMHRLW6p24kJvFE"],
["h.peterson","bmsCgzXfzurFXu5R"],
["eugeneb","Esrt2QhDJKPPcQt8"],
["timothy.smith","Bk3f4hQ69jQJsvkB"],
["jack.ortiz","j9nBx5TFyi5P83zK"],
["g.hunt","p2YoytD2zC5g8dLv"],
["reid.gibson","uHWvyedvwL2XeTEL"],
["j.campbell","T9SjcTpKdwoGuhqP"],
["georgem","sT47hTmHriy4BvmK"],
["john.mills","WiVjLfoscGWADAQT"],
["albert399","4GjDtVnS5ogreVqv"],
["nashw","Ga2roLv6pJrCfpvX"],
["r.hart","Jypmq3KGtZgcsCr2"],
["ronaldc","Bti4faEFFhVcDJEe"],
["foster.harris","vcbBzCw5tqN2jq6o"],
["t.morales","EPow3wBhZ8LGzjQs"],
["g.barnes","7ujSDRUgUizMVmaA"],
["russellc","69rd3f5Ec4RB4vao"],
["bowen75","rFCKYKrUx4sUVtvm"],
["johnny991","knS4ufgd2kEQSWmi"],
["justin438","YkYEFxduvAgKZiQo"],
["paul.gutierrez","xyBFRih4ZpSmyPPd"],
["nash.hughes","CWshE3SeFnjRXdKf"],
["s.turner","8zarQktiu6c26eD9"],
["david.cruz","3WvzuhfmTeiUgB2T"],
["adrianf","RgKaTdyUK3vvrGqe"],
["jeffrey.morgan","8tzyr2jSX4hFrhoW"],
["cole.nelson","LHsrGH9dJVPNxMba"],
["howard279","qoupRGYS767hA33c"],
["rodriguez57","FZ436oHRW8a8fWcy"],
["charles.king","tXN4KF22DgWCZTWP"],
["waynet","QquMMXRodvFN2v3s"],
["cole494","dtbkQRtMRwFnChRZ"],
["maxp","dsXjVLJRW9Hjax6w"],
["miles833","EH2eANZUcTtB7Euh"],
["joshua.morris","zXVvxbcJqxZemJ4X"],
["edwards47","9hom3LeutWMJFeGX"],
["graham28","2nUKKAh3bQp7JvNF"],
["marco821","uE9UwCnbT7sa8pxy"],
["carter44","8ut8rbU8MxbCU9Bh"],
["k.simmons","qnv4wta63HrqQguj"],
["coreys","Bk3AP3jak5ZiAEDb"],
["flores79","SJR9LfuEZx59jpT2"],
["scott730","5ivbWx96sJkib6w8"],
["c.stewart","4jEpmQP4zgQkhNrN"],
["earl.hughes","5eRmhf8PHj6CzJwJ"],
["bryce.gray","WQSF5NR2Wbv63JgV"],
["adrian.foster","HCqw9MJogUFqAB8m"],
["kevin286","MrbA4CLxtPPMo3ew"],
["samuel.patel","3k4NwAt9kJCTVSDk"],
["r.roberts","RhcPotioejDw5gT8"],
["spencer242","z35ahfrAGZTWnsnF"],
["howard.jackson","T5yiBtKr2U9deNNe"],
["vincent.rivera","eDRfz8VNRrPzivnb"],
["gary624","DHDTb8hkNoQCmtuA"],
["raymondb","MyKx5pdJfnmShwKv"],
["louis.bennett","KPjnL764EFKjAEfS"],
["norton51","gdNpbH5ENgRNffSD"],
["victor.garcia","juVsE6EJTA8JbhVg"],
["marco.bennett","v5ZdnjC3yVmdw9X4"],
["raymondr","d28W5dmDBbcuEqjk"],
["lane.gomez","WJFzcFqsc3URMHBP"],
["garrett214","TsGfxhv5LNuMBLkB"],
["reesef","P6MU5J58MpuBfSq6"],
["stephen415","mytETfLQtZnUMxXE"],
["d.phillips","b246YuxmUkNt6oVm"],
["reed13","fHARa33GdQ67oZeX"],
["brock.flores","DmRhSxUFve8fTMmX"],
["warren.smith","ru2mZuhjKyPyrra7"],
["oscar.edwards","6yYgRf6UtBmB3nHJ"],
["d.wood","mgQnjqc8zEDvKy8n"],
["b.flores","46XZKsbfG83cYYxB"],
["h.porter","AuwgeNvnKZETcCtC"],
["nashc","MkRvoJdvBGtPy6Cq"],
["e.king","TXHFCmHZtwU8F8oj"],
["williamh","KC7AQ9hEKyZWLmT6"],
["jacob.porter","ssHhPUGPnie9geoa"],
["lambert19","FcxRfF4dsV4swvjp"],
["taylor34","C6VPoAQZFcJn8gax"],
["julian.lawson","WntEtLAwXoKMxCPx"],
["colin233","vLpY7XtU6DwNAJFj"],
["mateoc","Esyff3hX4NFx6EgB"],
["jesse.clark","BnqSV6hBt2chu3Nd"],
["barnes6","AKSUPJSRtsuyz8m4"],
["justin22","Kt9J5xAoK6sCDqhJ"],
["lucas709","3eeUgTkY4gUt6BW9"],
["zachary.adams","j2Y9H9dPLeLtyCyc"],
["d.cruz","ixwYREQgQSUJzJpp"],
["lawrence805","iRBAiRzKsWm4Cerj"],
["jason.morris","prtJG5uMFCFyA69T"],
["b.lawson","767rxhXouSH2z6Hh"],
["timothyb","NmpnxXbb92nsGL8P"],
["dawsona","TQJ2CsHcjkHSM5Hw"],
["victor.ward","QMekFsFKZZsZvvEi"],
["lopez34","t2AXJ9EhdAdNUMLK"],
["alan820","gDFkWPUr2cxRpZfi"],
["peterw","wsY22p682KAWMyxD"],
["jacob.kim","NRPnhspC2TKDKvXk"],
["nathan.jackson","mCE8TA2TgL4M4VsT"],
["ruiz95","p9TMQBiG6ZSFp8AM"],
["davis61","pwh4EuF5V5i98ToS"],
["paul524","KHbFw4DQjjN5TBiC"],
["leonard.walsh","NtD4oGc4BVkTJK5J"],
["robert.brooks","fnRfpUADUbHWz2M5"],
["w.spencer","kFhpJuXCQrwUwKsc"],
["king67","ATiEKqj63TBUxBwG"],
["gomez40","MW2pZCvwnyEas82v"],
["jace.chambers","hQBBmBxGAGDuBJXp"],
["simmons67","64fWikk4DXCvmdvX"],
["c.ramos","kb26xV6sgZFoHDxH"],
["stephen.fisher","DdotgjZJPFzF7JVg"],
["b.murphy","G8pKZGKaxZJr6w9w"],
["williams88","VfPF8RZUscGZ8tt8"],
["vincent.wilson","QrmyZcv9VG9gGJSK"],
["kevin.ruiz","BiTBhZJqteRMR7wN"],
["adrian467","ujRZ8XuYanjjghRL"],
["miller65","3atcqn9V5QsV4jTT"],
["gabriel20","ot4Mqr4cGLmZWXbY"],
["kevin164","7onTpEzYT9yp2p4E"],
["dylanl","49Un3xM3WHKGhrKV"],
["pierce.phillips","6bziJsE5okm56yNC"],
["bobby.grant","np7BDHHTZpm8cjNX"],
["ivan.hughes","PVLsZejnSnD8duEQ"],
["james438","m3B4f3zkGsP4Ad5n"],
["jeffrey.ward","xpwFFpecCi8Uaam4"],
["s.smith","7VgwQnDbGMSKpY99"],
["t.phillips","uvpYcKynmRrC4v4i"],
["markg","nPFAsymehQWCYbCH"],
["t.campbell","rDMUxrShnyeHBRxm"],
["d.lambert","TxFe49vrEvSPabfv"],
["colinc","VjpvTJRxJchph4RG"],
["fisher38","FeULprHqUJCEzyUj"],
["samuelr","dcRUsDLDezdXx5sv"],
["lynch86","MPA9BLkHECundUeZ"],
["bryce.brooks","Trddt3b6XN525qov"],
["leonard.gutierrez","NCxVJcSCE8fGAXQ4"],
["nicholas.martin","UvmjgvopUZSpRWMm"],
["campbell71","m6HQh6Y7yBbTaTQ9"],
["owen.rivera","wqXANbU5nmF4FAkR"],
["matthew.burke","eyVKsPMCyJBVAWh3"],
["murphy4","fuNgXGkEqzycnMbb"],
["lynch70","V7pWd9nQN2wRtDcE"],
["joseph908","NqJzHbg2fgdA5ffQ"],
["elijah704","n3mJfKkgboLS9QRf"],
["r.long","P52zw8Up6MrsGyEK"],
["carl327","WBgFJnfEAvQcpLFz"],
["sean.brown","ZPutwiUnXLMZ3qC3"],
["craig.nguyen","PSttXXxYyWPzmKhm"],
["jacob343","skPNh3WBMn27a3Rh"],
["miles.bowen","eNQQY5JJAQT5HLrW"],
["edwards26","vEo7UbXZdSnC8YqW"],
["david.thomas","Xt4ZhR4ZfLECygUg"],
["daniel.alexander","Ao6KMZXdiJGgqiqM"],
["brian.watson","EzkVzh7GbVrXG5Pu"],
["aaron47","jkg7fdzbJjc8SmXc"],
["shane.rogers","w8Z7fMYUEsydYX2N"],
["roberts95","E4A6KaaeeZoUHU4y"],
["douglas832","6GRDuXuCpgxQquyY"],
["lee55","GyFYgQmDc29jvFQK"],
["peterson88","kiJgQVijMBvJkubm"],
["marcod","GhYY5q92nmDmHGN2"],
["pierceh","YJYHxLfkLTuhQuNH"],
["albert736","s2pv5tf94twLnsBt"],
["f.barnes","BVVNceaEJMetdtfN"],
["jerry.sanders","kkdgfqyxL7oDLvcA"],
["jesse.meyer","ghvAnt4ruyHbHyVJ"],
["paul.perry","yckGP4yEJDHEZQpC"],
["nathans","emM7f38m8rNG6bcS"],
["jimenez3","EcAYgcuy3adD8VMJ"],
["donald135","ewjC4iRTWFb6Xgob"],
["parker.barnes","jxAoLx7hd3bGkmfU"],
["moore72","D8NKZLoLGm4vHQGr"],
["roy621","QNYpxL5kbdoFj3va"],
["tyler.barnes","i6nkrgdHoQnzMdpL"],
["joe514","jdAVCp7uxWHB9gWH"],
["beckett801","mchDSa4XjtDc2K3T"],
["j.davis","ZJ7Fb7mDDHYHE9uX"],
["stanley416","At3DTGhUqxUMHnc6"],
["becker46","TE5ex8zmf7Zs5zoK"],
["lucas.rivera","3FLwZ6scjK6zruvg"],
["henry.chambers","uUfFTLXfYoAqfiFJ"],
["p.harris","pkLCas4SdHK43ZvV"],
["sullivan88","TU73MumpxPndxdoF"],
["wood21","DU3yGBBwKqhqTjtw"],
["dennisc","3T98aFuRdEkJU5LJ"],
["gabriel.campbell","JQEd6niNMzqQEPdf"],
["julian441","67uJtDPVUzNPgZMJ"],
["watson54","mrtrN6eDX8x8r8e2"],
["adam.peterson","pwSKPjrQXZVcmhqK"],
["l.lewis","ejbTA6akqnMQL8uY"],
["c.alexander","rjMsc98rTdE7Y4Ju"],
["carl964","5oKstBG5LU5vM7kB"],
["nicholasp","D8N7Znm8h6TZebdT"],
["leo.ruiz","TZSCZLowLFQ7MRZc"],
["lawson69","LTWhAZybeGLFzmGA"],
["austin.henderson","65HBUW6wLqjD2akD"],
["max.howard","27YDTGAi28GuwJrF"],
["garya","v8YiPjxQGQz8ymjU"],
["philip.turner","cC9phwboDYDKce3V"],
["patrick296","zEJaSS5SnXXU7DLw"],
["clarence.stewart","rTfWBWigTYtaxF7Z"],
["gabriel730","dQ4o26M6UtdGaNec"],
["lane.lynch","HoBJr9NQnX6q4Fy2"],
["grahamh","38yJSNgHHRJdseR7"],
["adam.hicks","GUiiR9PyaDYdtNsY"],
["edward.patel","wQZzWacQrDSMaqK9"],
["k.richardson","4CAdxtXtrqFhrrcP"],
["colton.perez","DuC6fLAgZyBNTiF7"],
["ronaldh","PEN2356GabPZtaqX"],
["joe.hernandez","udqrt9QGG6P2UkgP"],
["harold.hamilton","9PMvUbTwJKG99zJV"],
["garcia24","moWL3ouXt8JLufRC"],
["r.cruz","s3PVmUUDvopqmCtb"],
["nicholas858","BsSAdn7VHdndkkHS"],
["charles.johnson","ZkEqgqeRtPW9FvfX"],
["vincent.wright","WCRPWzLGb2zwgxid"],
["c.wilson","jFVHeBcxe7bXPhgM"],
["phillip.reed","hS9ZQ6kDMgGrGMnX"],
["keith.davis","BfkvkWkGVsfD8E9W"],
["a.howard","GwZdzn4pLQnn52am"],
["jason412","GaEKcmz8uLWpgd8T"],
["philip.richardson","xgqywC6h7pKM6VYv"],
["jonathan.roberts","uMWXmP9tPKSUeCEH"],
["terry.williams","xMv7vXNAstjmtVAd"],
["paul449","HKBi2wiLXtEDnLNh"],
["sullivan17","MpHCUP4frmghgjnt"],
["spencer59","qy43LUSMdfpEbZhM"],
["cole79","TQZLbAWSouGVYkHG"],
["kyle696","zXjZwDb8yvUBd25H"],
["felix.scott","pCeuaQUzN4T3nuVF"],
["vasquez69","p7XbNbEiXWGneoZT"],
["grant253","Kne4N5kW9TY7TSuw"],
["elijahm","Dh3x4U2yGbg3T38C"],
["bruce421","kGQXYYnqX4Wf6KDR"],
["thomas494","GpYmRuAzvU2Ukpf7"],
["howard468","kxhti8sKzVLWY8Yf"],
["henry.gibson","D4HxmKiynq5zwVMb"],
["hicks47","x8uFMJiBxFqiuVcZ"],
["r.king","MSbqyCywMroyuhtT"],
["bobby.lewis","JSUz2zd3PCmTjVvi"],
["noah.mason","N8VePwM9MkxEm89w"],
["danielg","GXHdhpU65vDmoJqm"],
["robert.west","SjxemE2StJmbg9fp"],
["corey263","VKjP3Ftea3eziu4i"],
["christopher.patel","HGAJABy9apZRsikt"],
["carterm","ir9FvYVNmDEMpUE5"],
["j.cruz","H54aw9MkE3L5EuAt"],
["murphy84","n8ApLxnosXh9qEu7"],
["gibson34","DaBrXWLd9pAeUmHm"],
["s.chambers","DYU2pGobD3BcA7Gv"]
];

const DOMAIN = "newarento.ru";
let created = 0, failed = 0, skipped = 0, errors = [];

async function createMailbox(name, password, index) {
  const params = new URLSearchParams();
  params.append("out", "json");
  params.append("func", "email.edit");
  params.append("name", name);
  params.append("domain", DOMAIN);
  params.append("passwd", password);
  params.append("confirm", password);
  params.append("sok", "ok");

  try {
    const res = await fetch("/ispmgr?" + params.toString(), {
      method: "GET",
      credentials: "same-origin"
    });
    const text = await res.text();

    if (text.startsWith("<!") || text.startsWith("<html") || text.startsWith("<HTML")) {
      // Try POST as fallback
      const res2 = await fetch("/ispmgr", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: params.toString(),
        credentials: "same-origin"
      });
      const text2 = await res2.text();
      if (text2.startsWith("<!") || text2.startsWith("<html")) {
        failed++;
        errors.push(name + ": HTML response (session expired?)");
        console.log("\u274c " + (index+1) + "/400 FAIL: " + name + "@" + DOMAIN + " \u2014 HTML response");
        return;
      }
      handleResponse(text2, name, index);
    } else {
      handleResponse(text, name, index);
    }
  } catch(e) {
    failed++;
    errors.push(name + ": " + e.message);
    console.log("\u274c " + (index+1) + "/400 ERROR: " + name + "@" + DOMAIN + " \u2014 " + e.message);
  }
}

function handleResponse(text, name, index) {
  let data;
  try {
    data = JSON.parse(text);
  } catch(e) {
    failed++;
    errors.push(name + ": Invalid JSON: " + text.substring(0, 100));
    console.log("\u274c " + (index+1) + "/400 FAIL: " + name + "@" + DOMAIN + " \u2014 bad JSON");
    return;
  }

  if (data.doc && data.doc.error) {
    const errMsg = JSON.stringify(data.doc.error);
    if (errMsg.includes("exist")) {
      skipped++;
      console.log("\u23ed\ufe0f " + (index+1) + "/400 EXISTS: " + name + "@" + DOMAIN);
    } else {
      failed++;
      errors.push(name + ": " + errMsg);
      console.log("\u274c " + (index+1) + "/400 FAIL: " + name + "@" + DOMAIN + " \u2014 " + errMsg);
    }
  } else {
    created++;
    console.log("\u2705 " + (index+1) + "/400 OK: " + name + "@" + DOMAIN);
  }
}

(async () => {
  // Test connection first
  console.log("\ud83d\udd0d Testing API connection...");
  try {
    const test = await fetch("/ispmgr?out=json&func=email", { credentials: "same-origin" });
    const testText = await test.text();
    if (testText.startsWith("<!")) {
      console.error("\u274c Session expired! Refresh the page and try again.");
      return;
    }
    const testData = JSON.parse(testText);
    console.log("\u2705 API works! Current mailboxes in panel:", testData.doc?.elem?.length || "unknown");
  } catch(e) {
    console.error("\u274c API test failed:", e.message);
    return;
  }

  console.log("\n\ud83d\ude80 Starting creation of " + mailboxes.length + " mailboxes for " + DOMAIN + "...\n");

  for (let i = 0; i < mailboxes.length; i++) {
    await createMailbox(mailboxes[i][0], mailboxes[i][1], i);
    await new Promise(r => setTimeout(r, 500));

    if ((i+1) % 50 === 0) {
      console.log("\n\ud83d\udcca Progress: " + (i+1) + "/400 (OK: " + created + ", FAIL: " + failed + ", EXISTS: " + skipped + ")\n");
    }
  }

  console.log("\n============================");
  console.log("\u2705 Created:  " + created);
  console.log("\u23ed\ufe0f Existed:  " + skipped);
  console.log("\u274c Failed:   " + failed);
  console.log("============================");
  if (errors.length > 0) {
    console.log("\nErrors (first 20):");
    errors.slice(0, 20).forEach(function(e) { console.log("  " + e); });
  }
})();
