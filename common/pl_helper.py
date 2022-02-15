import locale
from datetime import datetime


class PolishLocaleHelper:
    # stopwords source: https://github.com/bieli/stopwords/blob/master/polish.stopwords.txt

    stopwords = ['a', 'aby', 'ach', 'acz', 'aczkolwiek', 'aj', 'albo', 'ale', 'alez', 'ależ', 'ani', 'az', 'aż',
                 'bardziej', 'bardzo', 'beda', 'bedzie', 'bez', 'deda', 'będą', 'bede', 'będę', 'będzie', 'bo',
                 'bowiem', 'by', 'byc', 'być', 'byl', 'byla', 'byli', 'bylo', 'byly', 'był', 'była', 'było', 'były',
                 'bynajmniej', 'cala', 'cali', 'caly', 'cała', 'cały', 'ci', 'cie', 'ciebie', 'cię', 'co', 'cokolwiek',
                 'cos', 'coś', 'czasami', 'czasem', 'czemu', 'czy', 'czyli', 'daleko', 'dla', 'dlaczego', 'dlatego',
                 'do', 'dobrze', 'dokad', 'dokąd', 'dosc', 'dość', 'duzo', 'dużo', 'dwa', 'dwaj', 'dwie', 'dwoje',
                 'dzis', 'dzisiaj', 'dziś', 'gdy', 'gdyby', 'gdyz', 'gdyż', 'gdzie', 'gdziekolwiek', 'gdzies', 'gdzieś',
                 'go', 'i', 'ich', 'ile', 'im', 'inna', 'inne', 'inny', 'innych', 'iz', 'iż', 'ja', 'jak', 'jakas',
                 'jakaś', 'jakby', 'jaki', 'jakichs', 'jakichś', 'jakie', 'jakis', 'jakiś', 'jakiz', 'jakiż',
                 'jakkolwiek', 'jako', 'jakos', 'jakoś', 'ją', 'je', 'jeden', 'jedna', 'jednak', 'jednakze', 'jednakże',
                 'jedno', 'jego', 'jej', 'jemu', 'jesli', 'jest', 'jestem', 'jeszcze', 'jeśli', 'jezeli', 'jeżeli',
                 'juz', 'już', 'kazdy', 'każdy', 'kiedy', 'kilka', 'kims', 'kimś', 'kto', 'ktokolwiek', 'ktora',
                 'ktore', 'ktorego', 'ktorej', 'ktory', 'ktorych', 'ktorym', 'ktorzy', 'ktos', 'ktoś', 'która', 'które',
                 'którego', 'której', 'który', 'których', 'którym', 'którzy', 'ku', 'lat', 'lecz', 'lub', 'ma', 'mają',
                 'mało', 'mam', 'mi', 'miedzy', 'między', 'mimo', 'mna', 'mną', 'mnie', 'moga', 'mogą', 'moi', 'moim',
                 'moj', 'moja', 'moje', 'moze', 'mozliwe', 'mozna', 'może', 'możliwe', 'można', 'mój', 'mu', 'musi',
                 'my', 'na', 'nad', 'nam', 'nami', 'nas', 'nasi', 'nasz', 'nasza', 'nasze', 'naszego', 'naszych',
                 'natomiast', 'natychmiast', 'nawet', 'nia', 'nią', 'nic', 'nich', 'nie', 'niech', 'niego', 'niej',
                 'niemu', 'nigdy', 'nim', 'nimi', 'niz', 'niż', 'no', 'o', 'obok', 'od', 'około', 'on', 'ona', 'one',
                 'oni', 'ono', 'oraz', 'oto', 'owszem', 'pan', 'pana', 'pani', 'po', 'pod', 'podczas', 'pomimo',
                 'ponad', 'poniewaz', 'ponieważ', 'powinien', 'powinna', 'powinni', 'powinno', 'poza', 'prawie',
                 'przeciez', 'przecież', 'przed', 'przede', 'przedtem', 'przez', 'przy', 'roku', 'rowniez', 'również',
                 'sam', 'sama', 'są', 'sie', 'się', 'skad', 'skąd', 'soba', 'sobą', 'sobie', 'sposob', 'sposób',
                 'swoje', 'ta', 'tak', 'taka', 'taki', 'takie', 'takze', 'także', 'tam', 'te', 'tego', 'tej', 'ten',
                 'teraz', 'też', 'to', 'toba', 'tobą', 'tobie', 'totez', 'toteż', 'totobą', 'trzeba', 'tu', 'tutaj',
                 'twoi', 'twoim', 'twoj', 'twoja', 'twoje', 'twój', 'twym', 'ty', 'tych', 'tylko', 'tym', 'u', 'w',
                 'wam', 'wami', 'was', 'wasz', 'wasza', 'wasze', 'we', 'według', 'wiele', 'wielu', 'więc', 'więcej',
                 'wlasnie', 'właśnie', 'wszyscy', 'wszystkich', 'wszystkie', 'wszystkim', 'wszystko', 'wtedy', 'wy',
                 'z', 'za', 'zaden', 'zadna', 'zadne', 'zadnych', 'zapewne', 'zawsze', 'ze', 'zeby', 'zeznowu', 'zł',
                 'znow', 'znowu', 'znów', 'zostal', 'został', 'żaden', 'żadna', 'żadne', 'żadnych', 'że', 'żeby',
                 '.', ',', '-', '–', '—', '1', '2', '3', '12', '4', '11', '13', '2021', 'r.']

    months_lookup_table = {
        "stycznia": "styczeń", "lutego": "luty",
        "marca": "marzec", "kwietnia": "kwiecień",
        "maja": "maj", "czerwca": "czerwiec",
        "lipca": "lipiec", "sierpnia": "sierpień",
        "września": "wrzesień", "października": "październik",
        "listopada": "listopad", "grudnia": "grudzień"
    }

    # onet używa formatu daty %d %B %Y %H:%M z php 5.3+,
    # gdzie miesiące podlegają odmianie przez przypadki
    # źródło: https://stackoverflow.com/questions/21815788
    @classmethod
    def parse_pl_date_onet(cls, date_string):
        for k, v in cls.months_lookup_table.items():
            date_string = date_string.replace(k, v)

        locale.setlocale(locale.LC_ALL, "pl_PL.utf8")
        # locale.setlocale(locale.LC_TIME, "pl_PL.utf8")
        result = datetime.strptime(date_string, "%d %B %Y %H:%M")

        return result

    # tvn24 używa formatu daty %d %B %Y, %H:%M z php 5.3+,
    # gdzie miesiące podlegają odmianie przez przypadki
    # dodatkowy przecinek różni ten zapis od zapisu z onetu
    @classmethod
    def parse_pl_date_tvn24(cls, date_string):
        for k, v in cls.months_lookup_table.items():
            date_string = date_string.replace(k, v)

        locale.setlocale(locale.LC_ALL, "pl_PL.utf8")
        # locale.setlocale(locale.LC_TIME, "pl_PL.utf8")
        result = datetime.strptime(date_string, "%d %B %Y, %H:%M")

        return result

    # naszdziennik używa formatu daty %A, %d %B %Y (%H:%M) z php 5.3+,
    # gdzie miesiące podlegają odmianie przez przypadki
    # dodatkowo używana jest nazwa dnia
    @classmethod
    def parse_pl_date_naszdziennik(cls, date_string: str, short=False):
        for k, v in cls.months_lookup_table.items():
            date_string = date_string.replace(k, v)
        weekend_1 = 'Piątek-Niedziela,'
        weekend_2 = 'Sobota-Niedziela,'

        locale.setlocale(locale.LC_ALL, "pl_PL.utf8")
        # locale.setlocale(locale.LC_TIME, "pl_PL.utf8")
        if short:
            if weekend_1 in date_string or weekend_2 in date_string:
                return ''
            return datetime.strptime(date_string, "%A, %d %B %Y")
        else:
            return datetime.strptime(date_string, "%A, %d %B %Y (%H:%M)")
