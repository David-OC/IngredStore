from lxml import html
import requests

page = requests.get("http://www.jamieoliver.com/recipes/eggs-recipes/protein-pancakes/")
#page = requests.get("http://www.jamieoliver.com/recipes/vegetables-recipes/veggie-chilli/#vii0ZEWtgBcAe4vd.97")

tree = html.fromstring(page.content)


#ingredients = tree.xpath('//ul[@class="ingred-list"]/li')
ingredients = [li.xpath('normalize-space(.)') for li in tree.xpath('//ul[@class="ingred-list"]/li')]
#ingredients = tree.xpath('//ul[@class="ingred-list"]/li/text()')

for item in ingredients:
    print item

print "fuck you jamie oliver, you piece of shit"




