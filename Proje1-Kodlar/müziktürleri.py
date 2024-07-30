konu="Müzik Türleri"
print("╔"+"══════════════════════════════"+"╗")
print("║ Müzik Türleri Hakkında Bilgi ║")
print("║  1- Klasik Müzik             ║")
print("║  2- Pop Müzik                ║")
print("║  3- Rock Müzik               ║")
print("║  4- Rap/ Hip-Hop             ║")
print("║  5- Elektronik Müzik         ║")
print("║  6- Country Müzik            ║")
print("║  7- Caz Müzik                ║")
print("║  8- Raggae                   ║")
print("║  9- Metal Müzik              ║")
print("║  10- Blues                   ║")
print("║  11- Latin Müziği            ║")
print("║        Seçimini yap:         ║")
print("╚"+"══════════════════════════════"+"╝")
soru=int(input("Seçimini yap:")) 

def m_tür("soru"):
    
if soru==1 :
    print("Klasik müzik bestelerinde keman, viyola, çello, kontrbas, piyano, klavsen, obua, kormen, zil ve üçgen gibi enstrümanlar kullanılıyor. Klasik müzik besteleri, yalnızca enstrümantal konçerto ve senfonilerden oluşmuyor. Opera ve operetlerde söylenen aryalar da klasik müzik eseri olarak kabul ediliyor.")
elif soru==2 :
    print("Pop müziğin temel özellikleri, enstrümantal kısmın sadeliği, ritim, vokal vurgusudur. Pop müzikteki ana ve pratik olarak tek beste biçimi şarkıdır. Şarkılar mısra ve nakarat şemasına göre inşa edilmiştir. Bir pop şarkısı basit, okunması kolay melodiler gerektirir.")
elif soru==3 :
    print("Kökleri 1940'ların ve 1950'lerin rock and roll'una dayanır. Rock and roll ise blues, rhythm and blues ve country müzikten yoğun biçimde esinlenmiştir. Rock müzik; electric blues ve folk, caz, klasik müzik gibi diğer müzik kaynaklarından da esinlenir. 1950'lerden beri en fazla satış yapan müzik türü.")
elif soru==4 :
    print("Rap, sözlerin müziğin tempo ve ritmine uyarlanarak söylendiği bir yapıdadır. Rap yıllar boyunca değişim geçirmiştir ve rap içinde çeşitli alt türler oluşmuştur. Bunlara örnek olarak Gangsta, G-funk, Hardcore, Party ve Pesimist rap gibi örnekler gösterilebilir.")
elif soru==5 :
    print("Elektronik müzik, çağdaş teknoloji veya elektronik enstrümanlar aracılığıyla üretilen bir müzik türüdür ve yazılım programları da kullanılarak geliştirilebilir. Elektronik müziğin kökenleri 20. yüzyılın başlarına dayanmaktadır. 1920'lerde Lev Sergeyeviç Termen, ilk elektronik enstrüman olan 'Theremin'i icat etmiştir.")
elif soru==6 :
    print("Country tarzı, 1920'lerde ABD'nin güney eyaletlerindeki yoksul ve beyaz köylüler arasında ortaya çıktı. Country, ilk sömürgecilerin torunlarının kuşaktan kuşağa aktardıkları Galler, İskoçya ya da İrlanda'ya özgü eski halk şarkılarının ya da baladlarının Amerikan zevkine uyarlanmasıyla oluşturulmuştur.")
elif soru==7 :
    print("Caz müziği, mavi notalar, senkop, swing, çoklu ritim, atışma ve doğaçlama tekniklerini kullanır; Afrikalı-Amerikalı ve Batı müziği tekniklerinin harmanlanmasıdır. Bu müziğin dünya ile tanışması ise 1917 yılında Dixieland Jazz Band'in ilk plaklarının piyasaya çıkmasıyla olmuştur.")
elif soru==8:
    print("Reggae, Jamaika'ya özgü bir müzik türü. Ritmini kalp atışından aldığı söylenir. Jamaika usulü rock olarak da geçer. Kökleri calypso, ska/rocksteady, rock\n roll ve hatta rythm and blues\a dayanır.")
elif soru==9:
    print("Heavy metal (veya kısaca metal), 1960'lı yılların sonlarında 1970'li yılların başlarında İngiltere ve ABD'de gelişen bir rock müzik türüdür.[1][2] Kökenleri blues rock, psikedelik rock ve acid rock'a dayanan heavy metal grupları; kalın ve ağır bir ses, distortion, uzun gitar soloları ve yüksek ses gibi kendine özgü elementler geliştirmiştir.")
elif soru==10:
    print("Blues, 400 yıllık geçmişi olan ve temeli Afrika'ya dayanan, bir müzik türüdür. Kökleri Afrika'da bulunan blues, 17. yüzyıldan itibaren Afrika'dan getirilen kölelerin tarlalarda çalışırken söyledikleri hüznü, umudu, özgürlüğü ve derin acıyı anlatan şarkılardan doğmuştur.")
else:
    print("Latin müziği, Latin Amerika kültürlerinden etkilenen bir müzik türüdür. Salsa, rumba, tango gibi çeşitli dans türlerini içerir. Bu türler, müziğin sadece birkaç örneğidir ve her biri kendi içinde geniş alt türlere ayrılabilir.")
input()