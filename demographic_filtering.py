from flask import Flask, jsonify, request
import csv
articles=[]
with open('shared_articles.csv') as f:
  reader=csv.reader(f)
  data=list(reader)
  articles=data[1:]
  
  liked=[]
not_liked=[]

app=Flask(__name__)
@app.route("/getarticle")
def get_article():
  return jsonify({
      "data" : articles[0],
      "status" : "success"
        })

@app.route("/likedarticle",methods=["POST"])
def liked_article():
  article=articles[0]
  articles=articles[1:]
  liked.append(article)
  return jsonify({
      "status" : "success"
  }), 201

@app.route("/unlikedarticle",methods=["POST"])
def unliked_article():
  article=articles[0]
  articles=articles[1:]
  liked.append(article)
  return jsonify({
      "status" : "success"
  }), 201

if __name__=="__main__":
  app.run()