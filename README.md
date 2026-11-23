# Meme generator

Spletna aplikacija za ustvarjanje memov. V brskalniku uporabnik naloži sliko, vnese zgornje in spodnje besedilo, aplikacija pa ustvari meme in ga prikaže v brskalniku.

## Uporabljene tehnologije

-	Python
-	Flask – ogrodje za spletni strežnik
-	Pillow – knjižnica za obdelavo slik
-	HTML – obrazec za nalaganje slike in vnos besedila
-	Docker – kontejnerizacija aplikacije
-	GitHub

## Kako aplikacije deluje

1.	Uporabnik v HTML obrazcu naloži sliko in vpiše zgornje in spodnje besedilo
2.	Brskalnik z HTTP zahtevkom pošlje sliko in besedilo Flask aplikaciji
3.	Pillow odpre sliko in nanjo napiše besedilo
4.	Aplikacija shrani ta meme in ga prikaže v brskalniku

## Zagon z Dockerjem

Potrebujete nameščen Docker Desktop.

Gradnja Docker image v korenski mapi:
```bash
docker build -t meme-generator .
```
Zagon kontejnerja:
```bash
docker run --name meme-generator -p 5001:5001 meme-generator
```
Zaustavitev in odstranitev kontejnerja:
```bash
docker stop meme-generator
```
```bash
docker rm meme-generator
```