import time
import random

keppeseg_porgetes = 5
faj_porgetes = 5
aranytaller = 0
ero = 0
faj = ['Hős(+3000 erő)', 'Félember(+1500 erő)', 'Ember(0 erő)', 'Ember (0 erő)', 'Ember(0 erő)',
       'Ember(0 erő)', 'Ember(0 erő)', 'Ember(0 erő)', 'Ember(0 erő)', 'Ember(0 erő)',]
Kepesseg = ['Infinite Tsukuyomi(+5000)', 'Mangekyō Sharingan(3000+)', 'domain expansion(+1500 erő)', 'nincs szerencsed',
            'nincs szerencsed', 'nincs szerencsed', 'nincs szerencsed', 'nincs szerencsed', 'nincs szerencsed', 'nincs szerencsed',]


def meghaltal():
    while True:
        print("\nMEGHALTÁL\n")
        time.sleep(10000)


def vege():
    while True:
        print("\nGratulálnak a fejlesztők: Váradi Zsolt, Papp Bulcsú\nhttps://www.youtube.com/watch?v=aLdQA9PVPQw\nhttps://www.youtube.com/watch?v=tLTB0jcAPBo\n")
        time.sleep(10000)


def fajprogetesek():
    print(f"{nev} Most a karaktered testreszabhatósága következik Faj és Képesség pörgetés\n")
    global ero
    enter = input("Nyomj egy ENTERT a fajod kipörgetéséhez: ")
    alap_progetesed = faj_porgetes
    while enter != "":
        enter = input("Nyomj egy ENTERT a fajod kipörgetéséhez: ")
    while alap_progetesed > 0:
        fajod = random.choice(faj)
        print(f"Faj pörgetésed: {fajod}")
        print(f"Pörgetéseid száma: {alap_progetesed}")
        marad = input("Marad ez a faj? (igen/nem): ")
        while marad != "igen" and marad != "nem":
            marad = input("Marad ez a faj? (igen/nem): ")
        if marad == "igen":
            print(f"Elfogadod a fajod: {fajod}")
            if fajod == faj[0]:
                ero = ero + 3000
            elif fajod == faj[1]:
                ero = ero + 3000
            elif fajod == faj[2]:
                ero = ero + 1500
            kepessegporgetes()
        else:
            alap_progetesed -= 1
            print("Pörgetés következik...\n")
            time.sleep(1)
        while marad != "nem" and marad != "igen":
            marad = input("Marad ez a faj? (igen/nem): ")

    if alap_progetesed == 0:
        print("Már nincs pörgetésed.")
        time.sleep(0.5)
        print(f"faj: {fajod}")
        kepessegporgetes()

    print("erőd: ", ero, "\nMost a Képpességed jön\n")


def kepessegporgetes():
    global ero
    enter = input("Nyomj egy ENTERT a képpeséged kipörgetéséhez: ")
    alap_progetesed = keppeseg_porgetes
    while enter != "":
        enter = input("Nyomj egy ENTERT a képességed kipörgetéséhez: ")
    while alap_progetesed > 0:
        kepeseg = random.choice(Kepesseg)
        print(f"Képpesség pörgetésed: {kepeseg}")
        print(f"Pörgetéseid száma: {alap_progetesed}")
        marad = input("Marad ez a képesség? (igen/nem): ")
        while marad != "igen" and marad != "nem":
            marad = input("Marad ez a képesség? (igen/nem): ")
        if marad == "igen":
            print(f"Elfogadod a képességet: {kepeseg}")
            if kepeseg == Kepesseg[0]:
                ero = ero + 5000
            elif kepeseg == Kepesseg[1]:
                ero = ero + 1500
            jatekelsoresz()
        else:
            alap_progetesed -= 1
            print("Pörgetés következik...\n")
            time.sleep(1)
        while marad != "nem" and marad != "igen":
            marad = input("Marad ez a képesség? (igen/nem): ")

    if alap_progetesed == 0:
        print("Már nincs pörgetésed.")
        time.sleep(0.5)
        print(f"faj: {kepeseg}")
        jatekelsoresz()
    print("erőd: ", ero)


def jatekelsoresz():
    global ero
    print("")
    print("A világ még mindig emlékezett a nagy ütközet zúgására, amely egyszerre rengette meg az eget és a földet.")
    print("A végső csata, ahol vér és verejték árán dőlt el az emberiség sorsa, egyetlen hős nevét véste bele az idő végtelen szövetébe.")
    print("Ez a hős nem más volt, mint a nagyapád.")
    print("Ő volt az, aki puszta akaraterejével térdre kényszerítette az ellenséget, megmentve a világot az elkerülhetetlen végzettől.")
    print("A népek oly nagy hálával tartoztak neki, hogy diadalának pillanatától kezdték számolni az éveket.")
    print("De még a legnagyobb hősöket sem kíméli az idő könyörtelen keze.")
    print("Végül a nagyapád is elment, ám története, neve és tettei egyetlen halhatatlan legendává váltak.")

    print("")
    print("\n... .. .")
    print("\nKét év telt el a hős halála óta..")
    print("Te most nyolcéves vagy, a kíváncsiságod pedig egy napon nagyapád régi holmijaihoz vezetett.")

    print("")
    print("Miközben régi kardok, páncélok és emlékek között kutattál, kezed egy poros, régimódi tekercsre akadt.")
    print("Az idő szárította pergamen megreccsent, ahogy kinyitottad, rajta ősi, rejtélyes szimbólumok tűntek fel, amelyek olyanok voltak, mintha lélegeznének a bőröd alatt.")
    print("A tekercs szavai életre keltek, és ekkor döbbentél rá: ez nem csak egy ősi ereklye.")
    print("Ez a tekercs a nagyapád titka volt – benne állt, hogy te vagy a 'Tökéletes Harcos', az a kiválasztott, aki az ő erejét örökli.")
    print("A világ még nem sejti, de a te sorsod most kezdődik...\n")
    print("")

    input("Nyomj egy entert a story folyatatásához\n")

    print("")
    print("A nap már alacsonyan járt, mikor a naplemente lángoló fénye aranyszínűre festette az eget.")
    print("A levegőben érezni lehetett valami különleges vibrálást, mintha maga a világ is készülne valamire.")
    print("Ma nem volt egy átlagos nap. Ez a nap, a 18. születésnapod volt,")
    print("ami nemcsak egy egyszerű mérföldkő az életedben, hanem az a pillanat, amikor végre beteljesítheted a sorsodat.")
    print("Egész gyerekkorod óta erre a napra vártál, amikor végre kalandornak regisztrálhatsz,")
    print("és megkezdheted saját utadat, amelyről érezted, hogy egyedülálló és különleges lesz.")
    print("\nAmikor kinyitottad a szemed ezen a reggelen, valami különös érzés kavargott benned.")
    print("Mintha egy titkos energia lüktetett volna a bőröd alatt,")
    print("és a világ minden apró részlete – a madarak dala, a szél halk susogása, a fák árnyékának tánca – mind rád várt volna.")
    print("Az elmúlt tíz év sokkal több volt, mint puszta gyerekkor.")
    print("Azóta, hogy felfedezted nagyapád titkos tekercsét, az életed soha nem volt már ugyanaz.")
    print("A tekercs szavai még mindig élénken égtek az elmédben, mintha valami ősrégi mágia suttogott volna:")
    print("„Te vagy a Tökéletes Harcos.”")
    print("Ezek a szavak olyan mélyen vésődtek beléd, hogy minden lépésedet irányították.")
    print("Nemcsak a nagyapád örökségét hordoztad magadban, hanem a világ jövőjét is.")
    print("\nAz elmúlt évek kemény edzésekkel, áldozatokkal és titokzatos utasításokkal teltek,")
    print("amelyek nagyapád hagyatékából szivárogtak elő.")
    print("Most pedig itt álltál, 18 évesen, a kapuban, amelyen túl a világ új kalandokkal és kihívásokkal vár rád.")
    print("A falu legnagyobb eseményére készültél, hiszen ma regisztrálhattál hivatalosan kalandornak,")
    print("amire gyerekkorod óta készültél.")
    print("\nA városka központjában felállított kalandorok céhháza előtt izgatottan gyülekeztek a helyiek.")
    print("Minden szempár rád szegeződött, hiszen tudták, hogy nem vagy átlagos jelentkező.")
    print("Mióta a nagyapád nevét suttogták a széllel, az emberek mindig is érezték, hogy valami rendkívüli vár rád.")
    print("Ahogy beléptél a céhház masszív, faragott kapuin, megcsapott a régi fa illata,")
    print("és a rengeteg történet nyoma, amelyeket itt őriztek.")
    print("Az évek során sokan érkeztek ide ugyanígy, ám a te lépteid mások voltak.")
    print("Az ajtón túli jövő ismeretlen és veszélyekkel teli volt,")
    print("de egyúttal tele volt lehetőségekkel, melyek még csak most kezdtek megmutatkozni előtted.")
    print("\nAhogy közeledtél a hatalmas pult felé, ahol a kalandorok mesterénél regisztrálhattál,")
    print("érzed, hogy a testedben felpezsdül a vér. Ez az a pillanat, amiről álmodoztál, amit felépítettél magadban.")
    print("A mester, egy hosszú ősz hajú, komoly tekintetű férfi, figyelmesen rád nézett.")
    print("A tekintete egyszerre volt barátságos és kihívást jelentő,")
    print("mintha pontosan tudta volna, hogy benned több van, mint az, amit első pillantásra bárki gondolna.")
    print("\n– Üdvözöllek a kalandorok céhében – mondta mély, dörgő hangján.")
    print("– Eljött a napod, ugye? Azt mondják, hogy a vér nem hazudik. Lássuk, milyen kalandok várnak rád!")
    print("\nMiközben aláírtad a neved, mintha egy láthatatlan lánc pattant volna el benned.")
    print("Mintha ezzel az egyszerű mozdulattal feloldódott volna az a nyomás, amit az elmúlt évek során éreztél.")
    print("Most már hivatalosan is kalandor lettél, de ez csak a kezdet volt.")
    print("A világ hatalmas volt, tele titkokkal, rejtett veszélyekkel és óriási lehetőségekkel,")
    print("de te készen álltál szembenézni mindazzal, amit eléd vet.")
    print("A nagyapád emléke most már nemcsak egy távoli legenda volt, hanem az út, amelyet neked kellett folytatnod.")
    print("\nMielőtt kiléptél volna az épületből, és megkezdted volna utadat, valami megragadta a figyelmed.")
    print("Egy titokzatos üzenet érkezett a céhház asztalára, amelyen csupán ennyi állt:")
    print("\n„A vér köteléke erősebb, mint bármi más. A harcos sorsa beteljesedik.")
    print("Készülj fel, a világ hamarosan rád vár.”")

    print("")

    print("\nMost már tudtad, hogy nemcsak egyszerű kalandok várnak rád.")
    print("A nagyapád öröksége, a világ sorsa, és a tekercs titkai mind rád nehezednek,")
    print("és csak rajtad múlik, hogyan alakítod ezt az új fejezetet.")
    print("")

    input("Nyomj egy entert a story folyatatásához\n")
    kuldetesreszek()


def kuldetesreszek():

    print("\nMásnap\n")
    print("Öt küldetést kell végrehajtanod hogy Felmenj S-rangba")
    kerdes = input("Elindulsz az utadon?(igen/nem): ")
    while kerdes != "igen" and kerdes != "nem":
        print("Alszol egyet és gondolkodsz rajta")
        kerdes = input("Elindulsz az utadon?(igen/nem): ")
    if kerdes == "igen":
        print("\nBelevágtál\n")
        kuldetes1()

    while kerdes == "nem":
        print("Alszol egyet és átgondolod")
        kerdes = input("Elindulsz az utadon?(igen/nem): ")


def kuldetes1():
    global ero
    global aranytaller
    print("")
    print("Ahogy beléptél a kalandorok céhébe, a levegő vibráló izgalma szinte érezhető volt.")
    print("A falakon különféle dicsérő oklevelek és győzelmi zászlók lógtak,")
    print("amelyek hirdették a legyőzött szörnyeket és a végrehajtott küldetéseket.")
    print("A céh tagjai körülötted sürögtek-forogtak, néhányan felfegyverkezve,")
    print("mások térképeket tanulmányozva készültek a következő kalandra.")

    print("")
    print("\nTe azonban nem időzhettél el. A nekromanta testébe való átköltözésed óta eltöltött idő arra ösztönzött,")
    print("hogy feljebb lépj a ranglétrán, és ezt csak a démonok legyőzésével érheted el.")
    print("A céh vezetője, egy bölcs, ráncos arcú varázsló, azonnal észrevette a sötét energiát,")
    print("amely körülvett téged.")

    print("")
    print("\n– Fiatal kalandor – szólt hozzád – érzem, hogy különleges erő lakozik benned.")
    print("De tudnod kell, hogy a sötétség nem csupán hatalom, hanem veszély is.")
    print("Mielőtt még elérhetnéd az S rangot, négy démonnal kell megküzdened,")
    print("akik a sötétség különböző aspektusait képviselik. Készen állsz a kihívásra?")

    print("")
    print("\nKétkedve bólintottál, hiszen a nekromanta emlékei és sötét tudása segítségedre lehetett.")
    print("A vezető elmondta, hogy a démonok nevei: Kharath, Akara, Xylar, és Zarok.")
    print("És te elindultal a küldetésedre")

    elso_demon_ereje = random.randint(1500, 3000)

    time.sleep(2)
    print("\nTalálkozol az első démonnal akinek az ereje:", elso_demon_ereje)

    input("A támadáshoz nyomj egy entert:")

    if elso_demon_ereje <= ero:
        ero = elso_demon_ereje + ero
        time.sleep(2)
        print("Sikeresen legyőzted a démont, az ereje hozzá adodott a tiedhez, jelenlegi erőd: ", ero, "\n")

    elif elso_demon_ereje > ero:
        time.sleep(2)
        print("megölt a Démon\n")
        meghaltal()

    masodik_demon_ereje = random.randint(3000, 5000)

    time.sleep(2)
    print("\nTalálkozol a második démonnal akinek az ereje:", masodik_demon_ereje)

    input("A támadáshoz nyomj egy entert:")

    if masodik_demon_ereje <= ero:
        ero = masodik_demon_ereje + ero
        time.sleep(2)
        print("Sikeresen legyőzted a démont, az ereje hozzá adodott a tiedhez, jelenlegi erőd: ", ero, "\n")

    elif masodik_demon_ereje > ero:
        time.sleep(2)
        print("megölt a Démon\n")
        meghaltal()

    harmadik_demon_ereje = random.randint(5000, 9100)

    time.sleep(2)
    print("\nTalálkozol a harmadik démonnal akinek az ereje:", harmadik_demon_ereje)

    input("A támadáshoz nyomj egy entert:")

    if harmadik_demon_ereje <= ero:
        ero = harmadik_demon_ereje + ero
        time.sleep(2)
        print("Sikeresen legyőzted a démont, az ereje hozzá adodott a tiedhez, jelenlegi erőd: ", ero, "\n")

    elif harmadik_demon_ereje > ero:
        time.sleep(2)
        print("megölt a Démon\n")
        meghaltal()

    negyedik_demon_ereje = random.randint(9100, 14500)

    time.sleep(2)
    print("\nTalálkozol a negyedik démonnal akinek az ereje:", negyedik_demon_ereje)

    input("A támadáshoz nyomj egy entert:")

    if negyedik_demon_ereje <= ero:
        ero = negyedik_demon_ereje + ero
        time.sleep(2)
        print("Sikeresen legyőzted a 4.démont, az ereje hozzá adodott a tiedhez, jelenlegi erőd: ", ero, "\n")
        penz = random.randint(3500, 12000)
        aranytaller += penz
        print("\nAhogy a céhhez visszatértél, a tagok ujjongva fogadtak.")
        print("hanem egy új hős születését is jelentette.")
        print("\nAz emberek a hős nevét ismét el kezdték mondani,")
        print("Jutalamad")
        print("Aranytallérod: ", aranytaller)
        print("jellenlegi erod: ", ero)
        kuldetes2()

    elif negyedik_demon_ereje > ero:
        time.sleep(2)
        print("megölt a Démon\n")
        meghaltal()


def kuldetes2():
    global ero
    global aranytaller
    helytelen_valaszok = 5
    print("A kalandorok céhének legújabb tagjaként egy újabb küldetésre készültél, "
          "amely a sötétség és a fény határvonalán zajlott. A céh vezetője, a bölcs varázsló, "
          "egy titkos barlangról mesélt, amely tele volt kincsekkel és veszélyekkel. "
          "Az értesülések szerint a barlangban rejtőzködött egy hatalmas erő, "
          "amelyet csak a legbátrabbak képesek voltak megszerezni.\n")
    kerdes = input("Elindulsz az utadon?(igen/nem): ")
    while kerdes != "igen" and kerdes != "nem":
        print("Alszol egyet és gondolkodsz rajta")
        kerdes = input("Elindulsz az utadon?(igen/nem): ")
    if kerdes == "igen":
        print("\nBelevágtál\n")

    print("sötétségből Meghallasz egy hAngot a barlangba lépve és már nem Tudsz visszafordulni")
    print("Valaki:'E-embernek mint CSAk te egy ValOdi találoskérdés árán harcolhatsz meg velem és csak 5 tipped lehet'")
    print("")
    input("Nyomj egy entert a találoskérdés elkezdéséhez:")

    kerdes_megfejtese = "MATECSAVO"
    valaszod = input("Szerinted mi a válasz?:")
    while valaszod != kerdes_megfejtese and helytelen_valaszok != 0:
        print("ennyiszer probalkozhatsz: ", helytelen_valaszok)
        helytelen_valaszok = helytelen_valaszok - 1
        valaszod = input("Szerinted mi a válasz?:")

    if helytelen_valaszok == 0:
        print("A titkozatos ember gáz engedett rád")
        meghaltal()

    if valaszod == "MATECSAVO":
        print(
            "Sikeresen megfejtetedted a rejtvényt, legyenszives tanárúr ne irjon be egy szaktanarit:(")
        sotet_alak_ereje = random.randint(17000, 22000)

        time.sleep(2)
        print("\nTalálkozol a Sötét Alakkal akinek az ereje:", sotet_alak_ereje)

        input("A támadáshoz nyomj egy entert:")

        if sotet_alak_ereje <= ero:
            ero = sotet_alak_ereje + ero
            time.sleep(2)
            print("Sikeresen legyőzted a Sötét Alakot, az ereje hozzá adodott a tiedhez, jelenlegi erőd: ", ero, "\n")
            penz = random.randint(3500, 12000)
            aranytaller += penz
            print("\nAhogy a céhhez visszatértél, a tagok ujjongva fogadtak.")
            print("hanem egy új hős születését is jelentette.")
            print("\nAz emberek a hős nevét ismét el kezdték mondani,")
            print("Jutalamad")
            print("Aranytallérod: ", aranytaller)
            print("jellenlegi erod: ", ero)
            kuldetes3()

        elif sotet_alak_ereje > ero:
            time.sleep(2)
            print("megölt a Sötét Alak\n")
            meghaltal()


def kuldetes3():
    global ero
    global aranytaller
    print("")
    print("")
    print("A Tiltott Erdő Titkai")
    print("A faluban az ünnepség után megkeres téged egy titokzatos utazó, akiről hamar kiderül,"
          "hogy egy távoli, misztikus hegyekben lévő erődítmény őre. Elmondja, hogy a hegyekben lakó Démonkirály veszélyt"
          "jelent nemcsak a falura, hanem az egész vidékre.")
    kerdes = ""
    while kerdes != "igen":
        kerdes = input("Elvállalod a küldetést?:  ")
        if kerdes == "igen":
            print("")
            print("Az utazó elárulja, hogy a Démonkirály erejét egy varázslatos forrás táplálja, amely a Tiltott Erdő mélyén rejtőzik."
                  "Ahhoz, hogy megakadályozd a Démonkirály hatalmának növekedését, fel kell kutatnod és el kell pusztítanod ezt a titokzatos forrást."
                  "Az út azonban nem könnyű; az erdő elvarázsolt és tele van veszélyekkel, de szerencsére a térkép nálad van, amely segít kitalálni az útvesztőből,"
                  "hogy sikerrel járhass.")

            def labirintus_letrehoz():
                global aranytaller
                labirintus = [
                    ['#'] * 30,
                    ['#', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ',
                        ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#'],
                    ['#', ' ', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ',
                        '#', '#', ' ', '#', ' ', '#', '#', ' ', '#', ' ', '#', '#', ' ', '#'],
                    ['#', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ',
                        ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
                    ['#', ' ', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#',
                        ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#', '#', '#', '#', ' ', '#'],
                    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                        ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                    ['#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#',
                        '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#'],
                    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ',
                        ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                    ['#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#',
                        ' ', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', ' ', '#'],
                    ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', '#', ' ',
                        ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                    ['#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ',
                        '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#'],
                    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ',
                        ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                    ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', '#', '#', ' ',
                        '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
                    ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', ' ', ' ',
                        ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#',
                        ' ', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#'],
                    ['#', '#', '#', ' ', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#',
                        '#', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#'],
                    ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ',
                        '#', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
                    ['#', ' ', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#',
                        ' ', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', '#', ' ', '#', '#', '#'],
                    ['#', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ',
                        ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
                    ['#', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', '#',
                        ' ', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#'],
                    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' ', '#', ' ', '#',
                        '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                    ['#', '#', '#', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ',
                        '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#'],
                    ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ',
                        ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
                    ['#', ' ', '#', '#', ' ', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ',
                        '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', '#'],
                    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ',
                        ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
                    ['#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#',
                        ' ', '#', ' ', '#', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', '#', '#'],
                    ['#', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#',
                        ' ', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', '#'],
                    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#',
                        ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', 'X'],
                    ['#'] * 30,
                ]
                return labirintus

            def labirintus_megjelenit(labirintus, jatekos_poz):
                for i in range(len(labirintus)):
                    for j in range(len(labirintus[i])):
                        if (i, j) == jatekos_poz:
                            print('▼', end=' ')
                        else:
                            print(labirintus[i][j], end=' ')
                    print()
                print()

            def jatek():
                global aranytaller
                labirintus = labirintus_letrehoz()
                jatekos_poz = (1, 1)

                print("Üdv a Tiltott Erdő labirintusában! Találd meg a kijáratot (X)!")
                labirintus_megjelenit(labirintus, jatekos_poz)

                while True:
                    lepes = input(
                        "Merre szeretnél menni? (w: fel, s: le, a: balra, d: jobbra): ")
                    x, y = jatekos_poz

                    if lepes == 'w':
                        uj_poz = (x - 1, y)
                    elif lepes == 's':
                        uj_poz = (x + 1, y)
                    elif lepes == 'a':
                        uj_poz = (x, y - 1)
                    elif lepes == 'd':
                        uj_poz = (x, y + 1)
                    else:
                        print("Érvénytelen lépés! Használj w, s, a, vagy d-t.")
                        continue

                    if labirintus[uj_poz[0]][uj_poz[1]] != '#':
                        jatekos_poz = uj_poz
                    else:
                        print("Nem tudsz arra menni, fal van ott!")

                    labirintus_megjelenit(labirintus, jatekos_poz)

                    if labirintus[jatekos_poz[0]][jatekos_poz[1]] == 'X':
                        global ero
                        print(
                            "Gratulálok! Elérted a kijáratot és most megkell harcolj az őrzővel!")
                        orzo_ereje = random.randint(44000, 52000)
                        time.sleep(2)
                        print("Az erőd", ero)
                        print("\nTalálkozol az őrzővel akinek az ereje:", orzo_ereje)

                        input("A támadáshoz nyomj egy entert:")

                        if orzo_ereje <= ero:
                            global aranytaller
                            ero = orzo_ereje + ero
                            time.sleep(2)
                            print(
                                "Sikeresen legyőzted a Sötét Alakot, az ereje hozzá adodott a tiedhez, jelenlegi erőd: ", ero, "\n")
                            penz = random.randint(5200, 12000)
                            aranytaller += penz
                            print("Jutalamad")
                            print("Aranytallérod: ", aranytaller)
                            print("jellenlegi erod: ", ero)
                            kuldetes4()

                        elif orzo_ereje > ero:
                            time.sleep(2)
                            print("megölt a Sötét Alak\n")
                            meghaltal()
                        break

            jatek()
            break
        else:
            print("Csak 1 opciód van!!")


def kuldetes4():
    global aranytaller
    global ero
    print("")
    print("")
    print("A Tűz Hegye Küldetés:")
    print("A hegy belsejében egy ősi fegyver rejtőzik, amely képes legyőzni a Démonkirályt.")
    print("Az út azonban veszélyekkel teli; tűzóriások és lávafolyamok próbálnak megakadályozni.")
    print("Ahhoz, hogy eljuthass a különleges tűzfegyverhez, ki kell állnod néhány próbát.")
    print("Útközben találkozol különböző kihívásokkal, és csak a helyes válaszokkal tudsz továbbhaladni.")

    print("\nMiközben haladsz a sziklás úton, hirtelen egy tűzóriás állja el az utadat.")
    print("Felelned kell a kérdésére, hogy továbbengedjen.")

    valasz = ""

    while valasz != "a":
        print("")
        valasz = input(
            "Tűzóriás: Miből meríti a Démonkirály az erejét? (A: Varázslatos forrás, B: Tűzfegyver, C: Óriások ereje): ").lower()

        if valasz == "a":
            print(
                "A tűzóriás bólint, és félreáll az utadból. Egy lépéssel közelebb kerültél a célodhoz.")
        else:
            print(
                "A tűzóriás nem enged tovább, és pofon vág, ezért egy picit megsérülsz. Újra próbálkoznod kell.")
            ero -= 1000
            print("Erőd:", ero)

    print("\nTovábbhaladsz, és elérkezel egy lávafolyamhoz. Egy ősi kőoszlopon feliratot találsz, amelyen egy kérdés áll.")

    valasz2 = ""

    while valasz2 != "a":
        print("")
        valasz2 = input(
            "Kőoszlop: Mi lakik a hegy belsejében? (A: Tűzóriások, B: Jégóriások, C: Sárkányok): ").lower()

        if valasz2 == "a":
            print("A láva lassan csillapodik, és át tudsz kelni a folyamon. Egyre közelebb kerülsz a tűzfegyverhez.")
        else:
            print("A láva továbbra is zubog, nem tudsz átkelni, újra próbálkoznod kell.")
            ero -= 1000
            print("Erőd:", ero)

    print("\nTovábbhaladsz, és elérkezel egy dankóros ogréhez, aki kérdéseket tesz fel.")

    valasz4 = ""
    while valasz4 != 2019:
        valasz4 = int(
            input("Fortniteban mikor volt a chapter 2 season 1? (Évszámot írj): "))

        if valasz4 == 2019:
            print("Az ogre bólogat.")
        else:
            print("Az ogre rázza a fejét...")
            ero -= 1000
            print("Erőd:", ero)

    valasz5 = ""
    while valasz5 != "c":
        print("")
        valasz5 = input(
            "Levi milyen rankba van Rocket League-ben? (A: Diamond 1, B: Plat 3, C: Champ 2): ").lower()

        if valasz5 == "c":
            print("Az ogre bólogat.")
        else:
            print("Az ogre rázza a fejét...")
            ero -= 1000
            print("Erőd:", ero)

    valasz6 = ""
    while valasz6 != "a":
        print("")
        valasz6 = input(
            "Váradinak mennyi pontja van Akalival LOL-ban? (A: 256,054, B: 254,072 C: 254,054): ").lower()

        if valasz6 == "a":
            print("Az ogre bólogat.")
        else:
            print("Az ogre rázza a fejét...")
            ero -= 1000
            print("Erőd:", ero)

    valasz7 = ""
    while valasz7 != "c":
        print("")
        valasz7 = input(
            "Ki fog szaktanárit kapni? (A: Matecsavo, B: Palficsavo, C: Hideincinevég): ").lower()

        if valasz7 == "c":
            print("Az ogre bólogat.")
        else:
            print("Az ogre rázza a fejét...")
            ero -= 1000
            print("Erőd:", ero)

    valasz8 = ""
    while valasz8 != "b":
        print("")
        valasz8 = input(
            "Hogy lehet eltűnni, ha feltűntél? (A: Myspace, B: Ha zombi vagy, C: Ha demáciái vagy): ").lower()

        if valasz8 == "b":
            print("Az ogre bólogat.")
        else:
            print("Az ogre rázza a fejét...")
            ero -= 1000
            print("Erőd:", ero)

    valasz9 = ""
    while valasz9 != "a":
        print("")
        valasz9 = input(
            "What's mog mean? (A: Ha valakinél jobban nézel ki, B: Ha túl sokat játszottál egy játékkal, C: Sarka Levente): ").lower()

        if valasz9 == "a":
            print("Az ogre bólogat.")
        else:
            print("Az ogre rázza a fejét...")
            ero -= 1000
            print("Erőd:", ero)

    valasz10 = ""
    while valasz10 != "b":
        print("")
        valasz10 = input(
            "Folytasd a szöveget: 'meaw meaw' (A: meaw, B: meaw meaw, C: meaw meaw meaw): ").lower()

        if valasz10 == "b":
            print("Az ogre bólogat.")
        else:
            print("Az ogre rázza a fejét...")
            ero -= 1000
            print("Erőd:", ero)

    print("\nVégül elérsz egy hatalmas barlanghoz, ahol a tűzfegyver található.")
    print("Azonban az utolsó akadály előtt egy őrző szellem jelenik meg, és kérdést tesz fel.")

    valasz3 = ""
    while valasz3 != "b":
        print("")
        valasz3 = input(
            "Őrző szellem: Milyen fegyvert kell megszerezned, hogy legyőzd a Démonkirályt? (A: Fagycsapda, B: Tűzfegyver, C: Mennydörgés Íja): ").lower()

        if valasz3 == "b":
            print(
                "A szellem elmosolyodik, és eltűnik, utat engedve neked. Megszerzed a tűzfegyvert!")
            print("\nMinden kérdésre helyesen válaszoltál, megszerezted az ősi tűzfegyvert, és készen állsz a Démonkirály legyőzésére!")
            kuldetes5()
        else:
            print("A szellem elutasít, és nem enged tovább. Újra próbálkoznod kell.")
            ero -= 1000
            print("Erőd:", ero)


def kuldetes5():
    global aranytaller
    global ero
    print("")
    print("")
    print("A Démonkirály Szövetségesei")
    print("")
    print("A Démonkirály nem egyedül harcol; több szövetségese is van, akik titkos bázisokról irányítják az alvilági csapatokat."
          "A célod az, hogy megtaláld és legyőzd őket, mielőtt össze tudják hívni a teljes sereget. Ezek az ellenséges vezetők mindegyike egyedi képességekkel rendelkezik,"
          "és mindegyikük egy-egy kulcsot őriz, amely az erődítmény kapuját nyitja.")
    print("")
    print("Ahhoz, hogy le tudd győzni a Démonkirályt, először ki kell iktatnod a szövetségeseit.")
    kerdes = ""
    while kerdes != "igen":
        kerdes = input("Készen állsz a feladatra?:  ").lower()
        if kerdes == "igen":
            print("Ahogy elindulsz az utadon, már leszállt az éj, és egy sűrű erdőbe érsz. A fák között sötét árnyak mozognak,"
                  "és távolból egy titkos bázis fényei pislákolnak. A Vérfarkas, aki a csillagfényben rejtőzik, ott vár rád."
                  "Képes az árnyékokban közlekedni, és éjszaka félelmetes harcossá változik.")
            print("")
            print("")
            farkas_ereje = random.randint(90000, 102000)

            time.sleep(2)
            print("Az erőd:", ero)
            print("\nA sőtétből hírtelen rádtámad, erje:", farkas_ereje)

            input("A támadáshoz nyomj egy entert:")

            if farkas_ereje <= ero:
                time.sleep(2)
                print("Sikeresen legyőzted a vérfarkast Alakot!\n")
                penz = random.randint(5500, 12000)
                aranytaller += penz
                print("Jutalamad")
                print("Aranytallérod: ", aranytaller)
                print("jellenlegi erod: ", ero)
                kuldetes6()

            elif farkas_ereje > ero:
                time.sleep(2)
                print("Megölt a vérfarkas\n")
                meghaltal()

        elif kerdes == "nem":
            print(
                "Úgy tűnik, fáradt vagy, ezért alszol egyet, és újragondolod a válaszod.")
        else:
            print("igen vagy nem")


def kuldetes6():
    global aranytaller
    global ero
    print("")
    print("")
    print("Miután legyőzted a Vérfarkast, felfedezted az erdő mélyén rejtőző bázisának minden titkát, és elnyerted a kulcsot."
          "Most új cél vár rád: egy veszélyes vulkán belsejébe kell behatolnod, ahol a Tűzóriás őrzi a következő kulcsot."
          "A Tűzóriás egy tűzben edzett harcos, aki képes irányítani a lávát, és bármelyik pillanatban próbára teheti a bátorságodat.")
    kerdes = ""
    while kerdes != "igen":
        kerdes = input("Készen állsz a feladatra?:  ").lower()
        if kerdes == "igen":
            print("")
            print("")

            def vulkan_felfedezes():
                print("Továbbindulsz a vulkán belseje felé, ahol a Tűzóriás vár rád.")
                print(
                    "A lávafolyamok lassan hömpölyögnek, és vigyáznod kell, hogy ne lépj rájuk.")
                lava_kihivas()

            def lava_kihivas():
                global ero
                helyes_lepesek = ["bal", "előre", "jobb", "előre"]
                lepesek = []

                while lepesek != helyes_lepesek:
                    lepes = input(
                        "Merre lépsz? (bal/jobb/előre/hátra): ").lower()
                    lepesek.append(lepes)

                    if lepesek == helyes_lepesek:
                        print("Sikerült átjutnod a lávafolyamon!")
                        tűzorias_kihivas()
                        break
                    elif len(lepesek) > len(helyes_lepesek) or lepesek != helyes_lepesek[:len(lepesek)]:
                        print("Ráléptél a lávára és megsérültél! Próbáld újra.")
                        ero = ero-1000
                        print("Ennyi erőd maradt:", ero)
                        lepesek = []

            def tűzorias_kihivas():
                print(
                    "Elérted a Tűzóriás bázisát. Ő egy hatalmas, tűzben edzett harcos, aki irányítja a lávát.")
                print("A Tűzóriás próbára teszi bátorságodat.")
                fegyver_hasznalat()

            def fegyver_hasznalat():
                global ero
                global aranytaller
                valasz = input(
                    "Használod a tűzfegyvert a Tűzóriás ellen? (igen/nem): ").lower()
                if valasz == "igen":
                    print("A tűzfegyverrel sikeresen legyőzted a Tűzóriást!")
                    print(
                        "Megszerezted a kulcsot, amely a Démonkirály elleni végső csatához szükséges.")
                    penz = random.randint(5500, 12000)
                    aranytaller += penz
                    print("Jutalamad")
                    print("Aranytallérod: ", aranytaller)
                    print("jellenlegi erod: ", ero)
                    kuldetes7()
                else:

                    ero = ero-5000
                    print("Habozol, és a Tűzóriás újra sebzést okoz. Próbáld újra!")
                    print("Ennyi erőd maradt:", ero)
                    fegyver_hasznalat()

            vulkan_felfedezes()

        elif kerdes == "nem":
            print(
                "Úgy tűnik, fáradt vagy, ezért alszol egyet, és újragondolod a válaszod.")
        else:
            print("igen vagy nem")


def kuldetes7():

    def bevezetes():
        print("Miután legyőzted a Tűzóriást, elérsz egy különös helyet.")
        print("Előtted áll az Illúziókirálynő varázslatos tükörpalotája, ahol a valóság és az illúziók elmosódnak.")
        print("Csak egy valódi út vezet előre, a többi mind csapda. Vigyázz, és bízz az elmédben!\n")

    def tükörkombináció():
        print("Belépsz az első szobába, ahol több tükör sorakozik előtted.")
        print("Csak az egyik tükör mutatja a helyes utat.")
        helyes_tükör = random.randint(1, 3)

        for próbálkozás in range(3):
            while True:
                try:
                    választás = int(
                        input("Válaszd ki a tükröt (1-3) ({próbálkozás+1}/3 próbálkozás): "))
                    if választás == helyes_tükör:
                        print("Sikeresen megtaláltad a helyes tükröt, továbbjutsz!\n")
                        return True

                except ValueError:
                    print("Ez nem a helyes tükör. Próbáld újra!")

        print("Sajnos nem sikerült, vissza kell térned az elejére.\n")
        return False

    def fények_es_árnyékok():
        print("A következő szobában tükröket és fényforrásokat látsz.")
        print("Irányítsd a fényt, hogy kinyíljon az ajtó.")
        helyes_irány = random.choice(['balra', 'jobbra', 'középre'])

        for próbálkozás in range(2):
            választás = input(
                f"Válaszd ki a fény irányát (balra, jobbra, középen) ({próbálkozás+1}/2 próbálkozás): ").strip().lower()
            if választás == helyes_irány:
                print("Sikeresen kinyitottad az ajtót, továbbjutsz!\n")
                return True
            else:
                print("A fény nem nyitotta ki az ajtót. Próbáld újra!")

        print("Sajnos nem sikerült, vissza kell térned az elejére.\n")
        return False

    def emlékezetproba():
        print("Egy újabb szobába érkezel, ahol több ajtót látsz, mindegyikhez egy hangszín kapcsolódik.")
        print("Figyelj jól, és válaszd ki a megfelelő ajtót!")
        ajtók = ['vörös', 'kék', 'zöld']
        helyes_ajtó = random.choice(ajtók)

        print(f"Az elméd azt súgja hogy a helyes ajtó színe a: {helyes_ajtó}")
        print("de lehet csak át akar verni...")
        input("Nyomj Enter-t, hogy folytasd...")

        választás = input(
            "Melyik ajtón mész át? (vörös, kék, zöld): ").strip().lower()
        if választás == helyes_ajtó:
            print("Sikeresen megtaláltad a helyes ajtót, továbbjutsz!\n")
            return True
        else:
            print("Ez nem a helyes ajtó.\n")
            return False

    def képzelet_csapdái():
        print("Az Illúziókirálynő megjelenik előtted, és egy kérdést tesz fel.")
        kérdések = [
            ("Milyen színű volt az előző ajtó?", 'vörös'),
            ("Hány tükör volt az első szobában?", '3'),
            ("Merre irányítottad a fényt a második szobában?", 'balra, jobbra, középen')
        ]
        kérdés, helyes_válasz = random.choice(kérdések)

        válasz = input(f"{kérdés} ").strip().lower()
        if válasz in helyes_válasz:
            print("Helyes válasz, továbbjutsz!\n")
            return True
        else:
            print("Sajnos rossz válasz, vissza kell térned az elejére.\n")
            return False

    def tükörpalota_játék():
        while True:
            if not tükörkombináció():
                continue
            if not fények_es_árnyékok():
                continue
            if not emlékezetproba():
                continue
            if not képzelet_csapdái():
                continue

            print("Gratulálok! Sikeresen legyőzted az Illúziókirálynőt és megszerezted a kulcsot az erődítmény kapujához!\n")
            break

    tükörpalota_játék()
    shop()


def shop():
    global ero
    global aranytaller
    kerdes = input("Akarsz vásárolni pajszot?(igen,nem): ")
    while kerdes != "nem" and kerdes != "igen":
        kerdes = input("Akarsz vásárolni pajszot?(igen,nem): ")

    if kerdes == "igen":
        felszereles = [
            '1.susanoo pajzs(+5000erő),20000 aranytaller', '2.védelmezők védelmezője pajsz(+4000erő)15000 aranytaller', '3.kinder meglepetes pajsz(?erő)10000 aranytaller']

        for i in felszereles:
            print("Felszerelések: ", i)
        print("")
        melyiket_akarod = str(input(
            "írd be azt hogy mennyi aranytállérba került: "))

        if melyiket_akarod == "igen":
            melyiket_akarod = str(input(
                "írd be azt hogy mennyi aranytállérba került: "))

            while melyiket_akarod != "1" and melyiket_akarod != "2" and melyiket_akarod != "3":
                melyiket_akarod = str(input(
                    "írd be azt hogy mennyi aranytállérba került: "))

            if melyiket_akarod == "1" and aranytaller > 20000:
                aranytaller = aranytaller - 20000
                ero = ero + 5000
                print(
                    "Megvetted a kardot és az erőd nagyobb lett 200-al, jelenlegi erő szinted: ", ero)
                vegsoharc()

            elif melyiket_akarod == "2" and aranytaller > 15000:
                aranytaller = aranytaller - 15000
                ero = ero + 4000
                print(
                    "Megvetted a kardot és az erőd nagyobb lett 850-el, jelenlegi erő szinted: ", ero)
                vegsoharc()
            elif melyiket_akarod == "3" and aranytaller > 10000:
                aranytaller = aranytaller - 10000
                ero = ero + 10000
                print(
                    "Megvetted a kardot és az erőd nagyobb lett 1500-al, jelenlegi erő szinted: ", ero)
                vegsoharc()
            else:
                print("Nincs elegendő aranytallérod")
    elif kerdes == "nem":
        vegsoharc()


def vegsoharc():
    global ero
    global aranytaller
    print("A világot rettegés járta át. Egy ősi nekromanta ismét felbukkant, és a hírek szerint feltámasztotta a démonkirályt.")
    print("A nekromanta hatalmas zombi sereggel rejtőzködött valahol a hegyek mélyén.")
    print("A kalandorok céhe küldöttséget szervezett, hogy szembenézzenek a fenyegetéssel, és te is részt vettél a küldetésben.")
    print("Ahogy megközelítettétek a nekromanta rejtekhelyét, egy ódon kastélyt találtatok a sűrű ködben, amely körül zombik mozgolódtak.")
    print()

    print("A zombik serege körbevett titeket, és azonnal támadásba lendültek.")
    print("Nem volt más választásotok, mint harcba szállni velük.")
    print("Az összecsapás heves volt, de sikerült áttörni a zombi hordán, és belépni a kastélyba.")
    print()

    print("A kastély mélyén várt rátok a démonkirály, hatalmas alakja a trónon ült, vörösen izzó szemeivel figyelve titeket.")
    print("Mellette a nekromanta állt, gúnyos mosollyal az arcán.")
    print('Nekromanta: "Milyen vakmerő vagy, hogy azt hiszed, legyőzheted a démonok királyát és az én seregemet!"')
    print()
    print("A démonkirály felállt, és az egész kastély megrázkódott a léptei alatt. A harc kezdetét vette!")
    print("A démonkirály hatalmas kardjával csapott feléd, de te elugrottál előle, és próbáltál ellencsapást mérni.")
    print("A nekromanta közben zombikat idézett meg, akik akadályozták a mozgásodat.")
    print("A harc kemény volt, de a tudásod és gyorsaságod segítségével sikerült védekezni és támadni.")
    print()

    demon_kiraly = random.randint(95555, 115555)

    time.sleep(2)
    print("\nTalálkozol a Démonkirállyal:", demon_kiraly)

    input("A támadáshoz nyomj egy entert:")

    if demon_kiraly <= ero:
        ero = demon_kiraly + ero
        print("Sikeresen legyőzted a Démonkirályt, az ereje hozzá adodott a tiedhez, jelenlegi erőd: ", ero, "\n")
        print("Órákig tartó küzdelem után végül sikerült áttörni a démonkirály védelmét.")
        print("A kardod áthatolt a démon páncélján, és a démonkirály halálsikollyal rogyott össze.")
        print("A nekromanta kétségbeesetten próbált varázsolni, de túl későn. Egy utolsó csapással őt is legyőzted.")
        print("Ahogy a nekromanta holtteste a földre hullott, a sötét varázslatok szertefoszlottak, és a zombik serege egy pillanat alatt összeomlott.")
        print("A faluba visszatérve az emberek ujjongva fogadtak titeket.")
        print("Mindenki ünnepelt, hiszen a démonkirály és a nekromanta már nem fenyegette őket.")
        print("Te és a csapatod a céhben nagy ünnepségre számíthattok. A neved legendává vált.\n")
        megoldas()

    elif demon_kiraly > ero:
        print("Megölt a ZombiDémonKIRÁLY!\n")
        meghaltal()


def megoldas():
    time.sleep(3)
    print("Ötven évvel a hős halála után a világ látszólag békében élt, ám a sötétség mélyén egy titok lappangott.")
    print("A nekromanta, akit a démonkirály feltámasztott, nem halt meg, és elmenekült a harcok elől.")
    print("Te azonban, aki a hős örökségét viselted, nem vettél tudomást a fenyegetésről.")
    print("\nEgy napon, a halál küszöbén állva, a nekromanta hirtelen rád támadt.")
    print("Küzdened kellett az életedért, és ekkor új képességed, a „Lélek Vándor” aktiválódott.")
    print("Ezzel a hatalommal át tudtál szállni más testekbe,")
    print("és most, hogy a nekromanta közel volt, nem volt más választásod: megpróbáltad megmenteni magad.")
    print("\nA te lelked birtokába került a nekromanta teste, aki nem tudta, mi történik.")
    print("Hirtelen érezted, ahogy őt kilökted a testéből, és most te irányítottad a sötét varázsló testét.")
    print("De ahogy felfedezted ezt az új hatalmat, rájöttél, hogy a képesség csupán egyszer használható volt.")
    print("\nMost már a nekromanta bőrében kellett élned, és a sötétség,")
    print("amely eddig csak a lélek határvonalán leselkedett, most már a te lelkedet is meg akarta emészteni.")
    print("Ahogy egyre mélyebbre merültél a varázsló emlékeibe és érzéseibe,")
    print("kezdted érezni, hogy egyre inkább hasonlítasz hozzá, és a fény lassan kihunyt benned.")
    print("\nA világ, amelybe belépett a nekromanta, veszélyes és sötét volt,")
    print("és a te bátorságod próbára tétetett.")
    print("Az átalakulás nem csupán a testedet változtatta meg, hanem a lelkedet is,")
    print("és most már tudtad, hogy ha nem találsz kiutat ebből a sötétségből, örökre el fogsz veszni.")
    print("\nAz idő sürgetett, és a lélek harcának kezdete várt rád…")
    vege()


art = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⡶⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠲⠶⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⡿⣿⣦⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⣿⢏⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢎⠻⣿⣷⡄⠀⠀
⠀⠀⠀⠀⠀⣰⣿⣻⠃⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⢹⣿⣿⡄⠀
⠀⠀⠀⠀⢰⣿⣟⡗⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠐⣛⣿⣿⠀
⠀⠀⠀⠀⢸⣿⣿⡓⠀⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠠⢄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠇⠐⣻⣿⣿⡆
⠀⠀⠀⠀⢸⣿⣿⡷⠖⠋⠻⣄⠀⠀⣀⣤⠶⠚⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⢦⣄⡀⠀⢀⣴⠏⠈⠲⢿⣿⣿⠇
⠀⠀⠀⠀⠸⣿⣿⣿⣧⠞⠁⠈⠻⢾⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣻⡷⠋⡁⠈⢦⣾⣿⣿⣿⠀
⠀⠀⠀⠀⠀⠹⣿⣿⣷⣷⡴⠃⠀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠱⣴⣷⣯⣿⡿⠃⠀
⠀⠀⠀⠀⠀⠀⠙⢿⣿⣯⣾⣿⢗⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⢾⣿⣮⣿⣿⠟⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠳⣽⣿⣿⡍⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⢸⣇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠘⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⢄⣿⡰⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⢸⣇⠀⢀⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀ ⣿⠀⣾⣿⠇⠹⣶⣤⣀⣀⠀⠙⢶⣤⡀⠀⠀⠀⣠⣴⠖⠉⢀⣀⣠⣴⡾⠁⢿⣿⡆⢸⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⣿⠏⢠⣾⣿⣿⣿⣿⣿⣦⡀⠹⡿⠀⠀⠸⡿⠁⣤⣾⣿⣿⣿⣿⣷⣦⠀⢿⡇⡸⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⢿⡀⢸⣿⣿⣿⣿⣿⣿⣿⡟⠆⠀⠀⠀⠀⠀⠞⣿⣿⣿⣿⣿⣿⣿⣿⠀⣸⢧⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢈⡷⠈⢿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣠⣤⡀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠃⠀⣏⠈⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡆⠀⠀⠀⠙⠻⠿⠿⠿⠟⠁⠀⢠⣿⣿⣧⠀⠀⠙⠿⠿⠿⠿⠛⠁⠀⠀⠀⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⢻⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⡿⢸⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⢛⣿⣿⣿⡖⠦⡀⠀⠀⠉⠁⠀⠉⠁⠀⠀⢠⠖⣾⣿⣿⣿⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⣿⢻⣿⣴⣠⢀⠀⡄⠀⡀⢀⡄⢀⣀⣼⣼⣿⠹⡇⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠧⡇⢸⣿⣿⡇⢹⠒⡟⠙⡟⠉⡗⢹⠁⣿⣿⣿⠀⡧⠇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠘⢿⣹⠛⠼⣦⣿⣄⣧⣀⣷⣾⠴⢻⣸⠟⠀⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⡀⠀⠀⠊⠳⠧⣼⣠⣤⣧⣱⣸⡦⠷⠚⠃⠀⠀⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠲⣤⡀⠀⠀⠀⠈⠀⠀⠈⠀⠀⠀⠀⣠⡴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢷⣄⣠⣴⣶⣤⣄⣰⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

print(art)
print("KÖSZÖNTELEK A DÉMONKIRÁLY 2-BEN!")
nev = input("Mi a neved?: ")
while nev == "":
    nev = input("Mi a neved?: ")
elso_kerdes = input("kezdőthet?(igen/nem): ")
while elso_kerdes != "nem" and elso_kerdes != "igen":
    elso_kerdes = input("kezdőthet?(igen/nem): ")

if elso_kerdes == "igen":
    fajprogetesek()

elif elso_kerdes == "nem":
    print("köszönjük hogy velünk játszott")
# Váradi Zsolt,Papp Bulcsú
