from flask import Flask, render_template, request, redirect, url_for, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

#Fake Catalog
categories = [{'name': 'Vegetables', 'id': '1'}, {'name': 'Meats', 'id': '2'}, {'name': 'Soups', 'id': '3'}, {'name': 'One Pot Meals', 'id': '4'}]

vegetables = []
for c in categories:
    print c

#Fake Recipes
recipes = [{'name':'Cheese Pizza', 'description':'made with fresh cheese', 'link':'https://example.com','category' :'Vegetables', 'id':'1', 'created_at': '11/22/2017'}, {'name':'Pepperoni Pizza', 'description':'made with fresh Pepperoni', 'link':'https://pepperoni.com', 'category' :'Meats', 'id':'2', 'created_at': '11/22/2017'}, {'name':'Supreme Pizza', 'description':'made with fresh cheese & meats', 'link':'https://supreme.com','category' :'One Pot Meals', 'id':'3', 'created_at': '11/23/2017'} ]

@app.route('/')
@app.route('/catalog')
def showAllCategories():
    return render_template('catalog.html', categories = categories, recipes = recipes)

@app.route('/catalog/<category>')
def showCategory(category):
    return render_template('category.html', category = category, recipes = recipes)

@app.route('/catalog/<category>/<recipe>')
def showRecipe(category,recipe):
    return render_template('recipe.html', recipe = recipe, recipes = recipes)

@app.route('/catalog/<category>/new')
def newRecipe(category):
    return 'This is the %s category page' % category

@app.route('/catalog/<category>/<recipe>/edit')
def editRecipe(category,recipe):
    return 'This is the %s category page' % category

@app.route('/catalog/<category>/<recipe>/delete')
def deleteRecipe(category,recipe):
    return 'This is the %s category page' % category

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
