from django.db import models

# Create your models here.


STATUS = (
    (1, 'Studiuję'),
    (2, 'Pracuję'),
    (3, 'Zajmuję się domem'),
    (4, 'Jestem na emeryturze lub rencie')
)

YES_NO = (
    (1, 'Tak'),
    (2, 'Nie')
)

HOME_TYPE = (
    (1, 'Blok'),
    (2, 'Kamienica'),
    (3, 'Dom')
)


class AdoptionForm(models.Model):
    address = models.CharField(max_length=255, verbose_name="Adres")
    phone_number = models.IntegerField(verbose_name="Numer telefonu")
    status = models.IntegerField(choices=STATUS, verbose_name="Aktualne zajęcie")
    question_1 = models.IntegerField(verbose_name="Ile osób mieszka w domu/mieszkaniu?")
    question_2 = models.IntegerField(choices=YES_NO, verbose_name="Czy wszystkie osoby zgadzają się na adopcję?")
    question_3 = models.IntegerField(choices=YES_NO, verbose_name="Czy w domu są dzieci?")
    question_4 = models.TextField(null=True, blank=True,
                                  verbose_name="Jeśli tak prosimy podać w jakim są wieku i jaki mają stosunek do zwierząt.")
    question_5 = models.IntegerField(choices=YES_NO, verbose_name="Czy w ciągu dnia ktoś jest obecny w domu?")
    question_6 = models.IntegerField(choices=YES_NO, verbose_name="Czy ktoś w domu ma alergię na zwierzęta?")
    question_7 = models.IntegerField(choices=YES_NO, verbose_name="Czy w domu są już jakieś zwierzęta?")
    question_8 = models.TextField(null=True, blank=True,
                                  verbose_name="Jeśli tak, proszę wpisać jakie i jaki jest ich stosunek do innych zwierząt.")
    question_9 = models.IntegerField(choices=YES_NO, verbose_name="Czy miała Pani/Pan wcześniej już jakieś zwierzęta?")
    question_10 = models.TextField(null=True, blank=True,
                                   verbose_name="Jeśli tak to prosimy o kilka słów o nich oraz jak potoczyły się ich losy.")
    question_11 = models.IntegerField(choices=YES_NO, verbose_name="Czy adoptowała Pani/Pan już kiedyś zwierzę?")
    question_12 = models.TextField(verbose_name="Skąd pomysł na adopcję?")
    question_13 = models.IntegerField(choices=HOME_TYPE, verbose_name="Gdzie Pani/Pan mieszka?")
    question_14 = models.IntegerField(verbose_name="Jaki metraż mieszkania/domu(mkw)?")
    question_15 = models.IntegerField(null=True, verbose_name="Które piętro?")
    question_16 = models.IntegerField(choices=YES_NO, verbose_name="Czy jest winda?")
    question_17 = models.TextField(null=True,
                                   verbose_name="Czym ogrodzona jest posesja? Czy posesja jest dokładnie ogrodzona?")
    question_18 = models.CharField(max_length=255, verbose_name="Jak często zwierzę będzie chodzić na spacery?")
    question_19 = models.TextField(verbose_name="Co będzie się działo ze zwierzęciem podczas Pani/Pana wyjazdów, wakacji?")
    question_20 = models.CharField(max_length=255, verbose_name="Jak często i jak długo zwierzę będzie zostawać samo?")
    question_21 = models.IntegerField(choices=YES_NO,
                                      verbose_name="""Posiadanie zwierzęcia wiąże się z obowiązkiem regularnych 
                                                      szczepień ochronnych, odrobaczania, zabezpieczania przeciwko 
                                                      kleszczom. Czy jest Pani/Pan przygotowana na tego typu wydatki?""")
    question_22 = models.IntegerField(choices=YES_NO,
                                      verbose_name="""Zwierzęta, jak i ludzie czasem chorują i takie leczenie bywa 
                                                      kosztowne. Czy jest Pani/ Pan przygotowana na tego typu wydatki?""")
    question_23 = models.IntegerField(choices=YES_NO,
                                      verbose_name="""Czy planuje Pani/Pan wydatki związane z zakupem akcesoriów dla 
                                                      zwierzęcia?""")
    question_24 = models.IntegerField(choices=YES_NO,
                                      verbose_name="""Żywienie to kolejny spory wydatek. Czy jest Pani/Pan na to 
                                                      przygotowana?""")
    question_25 = models.CharField(max_length=255, verbose_name="Czym zamierza Pani/Pan żywić zwierzę?")
    question_26 = models.IntegerField(choices=YES_NO,
                                      verbose_name="""W pierwszym okresie po adopcji zwierzę może sprawiać kłopoty, 
                                                      np.: zniszczyć coś w domu lub w ogrodzie, załatwić się w domu, 
                                                      mieć biegunkę. Czy jest Pani/Pan gotowa na zmierzenie się z tymi 
                                                      problemami?""")
    question_27 = models.IntegerField(choices=YES_NO,
                                      verbose_name="""Zwierzęta ze schroniska mogą mieć różne nawyki (bać się krzyku, 
                                                      szczotki itp.), których zmiana może wymagać dużo czasu, pracy 
                                                      i cierpliwości. Czy jest Pani/Pan na to gotowy?""")
    question_28 = models.TextField(verbose_name="""Jeśli wybrane zwierzę nie będzie posłuszne, jak zamierza Pani/Pan 
                                                   skorygować jego błędne zachowania?""")
    question_29 = models.IntegerField(choices=YES_NO,
                                      verbose_name="""Zwierzę może żyć kilkanaście lat. Czy przewidziane jest miejsce 
                                                      dla zwierzęcia w życiu rodziny?""")
    question_30 = models.CharField(max_length=255,
                                   verbose_name="Jaki jest Pani/Pana stosunek do kastracji/sterylizacji?")
    question_31 = models.IntegerField(choices=YES_NO,
                                      verbose_name="Czy wyraża Pani/Pan zgodę na wizytę przed adopcyjną i po adopcyjną?")
    question_32 = models.IntegerField(choices=YES_NO,
                                      verbose_name="""Opiekun zobowiązuje się do:
                                                      - leczenia psa wg. zaleceń przekazanych przy odbiorze psa,
                                                      - opłacenia podatku za posiadanie psa (jeśli jest to wymagane 
                                                        w miejscu zamieszkania),
                                                      - corocznego szczepienia psa przeciw wściekliźnie i innym chorobom 
                                                        wraz z poddaniem psa badaniu ogólnego stanu zdrowia u lekarza 
                                                        weterynarii z wpisem do książeczki i karty badań,
                                                      - nie wypuszczania psa w miejscach otwartych bez dozoru,
                                                      - spełniania wszelkich obowiązków wynikających z prawa miejscowego.
                                                      - minimum jednej, obowiązkowej, corocznej wizyty u lekarza 
                                                        weterynarii w miesiącu kwietniu (każdego roku)
                                                      Czy zgadza się Pani/Pan na te warunki?""")
    agreement = models.IntegerField(choices=YES_NO,
                                    verbose_name="""Wyrażam zgodę na przetwarzanie moich danych osobowych, zgodnie 
                                                    z treścią ustawy o ochronie danych osobowych. Administratorem danych 
                                                    jest Schronisko z siedzibą w Schronisku ul. Schroniskowa. 
                                                    Dane przetwarzane są wyłącznie w celach statystycznych oraz w celu 
                                                    przekazywania zamówionych przez Państwa informacji lub innych 
                                                    działań zgłaszanych w przekazywanych formularzach elektronicznych 
                                                    lub zgłoszeniach. Dane nie będą udostępniane innym, nieuprawnionym 
                                                    podmiotom. Informujemy, że Państwa zgoda może zostać cofnięta 
                                                    w dowolnym momencie przez wysłanie wiadomości e-mail na adres 
                                                    naszego ABI spod adresu, którego zgoda dotyczy. Informujemy, że nie 
                                                    jesteście Państwo profilowani.""")

