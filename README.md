# BotCoronaNews

Bot que pega notícias sobre coronavírus na região de Bauru e posta em comunidades e redes sociais.

O objetivo deste projeto é criar um bot que possa pesquisar notícias relacionadas ao novo coronavírus e centralizar em comunidades para manter as pessoas informadas sobre como a região da cidade de Bauru esta sendo afetada por esta pandemia.

Atualmente as notícias são providas pela api de busca personalizada do google e postadas em dois lugares, uma comunidade do [Reddit](https://www.reddit.com/r/Bauru) e em um perfil do [Twitter](https://twitter.com/CoronaNewsBauru).

As fontes utilizadas na busca do google são o [JCNet](https://www.jcnet.com.br/) e o [g1 bauru e região](https://g1.globo.com/sp/bauru-marilia/)

O projeto ainda esta em desenvolvimento, o objetivo é melhorá-lo, acrecentando mais sites para monitorar e também mais comunidades que possam atingir mais pessoas, como Facebook e outros. Também é preciso criar um serverless na aws ou google cloud com um scheduler para chamar o bot periodicamente e talvez um processo de deploy automatizado.


## to-do

* Melhorar o readme
  * Informações de como instalar e rodar o bot
* Criar serverless na aws