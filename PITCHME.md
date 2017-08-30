#HSLIDE
<style>
    small {
        font-size: 0.7em;
    }
</style>
## Récupérer le tutoriel
- https://github.com/bdoin/jinja2-tutorial
- installer python
- installer jinja2
- installer pybabel

#HSLIDE
## Historique du site gcompris.net
- Site crée en 2003 avec le CMS SPIP
- difficultés avec les traductions
- difficulté pour les copies d'écran

#HSLIDE
## Que choisir
- Se rapprocher du modèle de développement de GCompris
- Utilisation des fichiers .po pour la traduction
- Langage python
- Site statique
- Génération du site avec un make

#HSLIDE
## Python
- Choix de Python car c'est utilisé dans Gcompris
- Mais nécessite un système de gabarit pour séparer la logique et la mise en forme

#HSLIDE
## Jinja2
- Moteur de gabarit basé python
- Très puissant et bien documenté
- Permet les traductions via pybabel ou gettext

#HSLIDE
## Hello jinja2

    #! /usr/bin/python

    import jinja2
    from jinja2 import Template

    template = Template('Hello {{ name }}!')
    print template.render(name='Toulibre')

#HSLIDE
## Jinja2 chargeur de gabarit

On peut préciser ou trouver les fichiers gabarits:

    templateLoader = jinja2.FileSystemLoader( searchpath="template" )
    templateEnv = jinja2.Environment( loader=templateLoader )
    template = templateEnv.get_template( "test.html" )

#HSLIDE
## Héritage Jinja2
- Il est possible de créer un gabarit de base qui définit des blocs cibles.
- Un gabarit peut en étendre un autre et remplir les blocs cibles.

#HSLIDE
## Site adaptatif
- Pour avoir un affichage optimal en fonction de la taille d'écran du visiteur
- Choix évident de partir sur bootstrap qui semble être le plus utilisé.

#HSLIDE
![BEER](https://blog.stephaniewalter.fr/wp-content/uploads/2013/06/content-is-like-water-12401.jpg)

#HSLIDE
## Twitter Bootstrap
- <small>Twitter Bootstrap est une collection d'outils utile à la création de sites web et applications web.</small>
- <small>C'est un ensemble qui contient des codes HTML et CSS, des formulaires, boutons, outils de navigation et autres éléments interactifs, ainsi que des extensions JavaScript en option. C'est l'un des projets les plus populaires sur la plate-forme de gestion de développement GitHub.</small>
- <small>Cette plate-forme a été conçue par deux développeurs faisant partie de la mouvance de développeurs qui gravitent autour de Twitter, Mark Otto et Jacob Thornton (@mdo et @fat).
<br/>
<br/>(source wikipedia)</small>

#HSLIDE
## La grille Bootstrap
- http://getbootstrap.com/css/#grid
- Basé sur une grille de 12 colonnes qui s'adaptent à la taille de l'écran.
- Le développeur spécifie pour chaque contenu le nombre de colonne à utiliser.
- Il peut spécifier un nombre différent selon la largeur de l'écran du visiteur.

#HSLIDE
## La grille Bootstrap (1)

    <div class="container">
        <div class="col-sm-6 col-lg-2">A</div>
        <div class="col-sm-6 col-lg-2">B</div>
        <div class="col-sm-6 col-lg-2">C</div>
        <div class="col-sm-6 col-lg-2">D</div>
        <div class="col-sm-6 col-lg-2">E</div>
        <div class="col-sm-6 col-lg-2">F</div>
    </div>

#HSLIDE
## La grille Bootstrap (2)

### Écran large ≥ 1200px :
    [A   B   C   D   E   F]

### Écran petit ≥  768px :
    [A   B]
    [C   D]
    [E   F]

#HSLIDE
## Les boucles jinja2

    t = Template('{% for onenews in news %}{{ onenews }} {% endfor %}')
    t.render(news=['news1', 'news2'])
    -------------------------------------------
    t = Template('{% for onenews in news %}{{ onenews["k"] }} {% endfor %}')
    t.render(news=[{'k' : 'v1'}, {'k' : 'v2'}])


#HSLIDE
## Encore des boucles

    class news:
        def __init__(self, content):
            self.content = content

    t = Template('{% for onenews in news %}{{ onenews.content }} {% endfor %}')
    print t.render(news=[news('v1'), news('v2')])

#HSLIDE
## Les macros jinja2

### hello.html:

    {% macro hello(username) -%}
        Hello {{ username }}
    {%- endmacro %}

### index.html:

    {% import "hello.html" as h %}
    {{ h.hello("Toulibre") }}

#HSLIDE
## i18n avec pybabel
- Pybabel permet d'extraire les chaînes marquées avec `{% trans %}Hello{% endtrans %}` dans les gabarits
- Ou marquées avec `_('Hello')` dans votre code python
- Créer un fichier babel.cfg pour lister les fichiers à traduire

#HSLIDE
## Conclusion
- Pour GCompris on a remplacé 100K lignes de PHP par 200 lignes de python et 400 lignes de gabarits Jinja2.
- Traduction plus simple, récupération des chaîne de GCompris.
- Création de la page screenshot à la volée.
- Génération et mise en ligne via make.
